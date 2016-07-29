import re
import urllib2
import pickle as pkl
import itertools
from pyspark import SparkConf, SparkContext

# In Jupyter you have to stop the current context first
sc.stop()
# Create new config
conf = (SparkConf().set("spark.driver.maxResultSize", "50g"))
# Create new context
sc = SparkContext(conf=conf)

load_s3_data = sc.textFile("s3n://{}:{}@wiki-2016/one_l_a.txt".format(access-key,secret-key),100)

ten_thousand = sc.parallelize(load_s3_data.take(10000),100)
ten_thousand.getNumPartitions()

ten_thousand.toDebugString()

ten_thousand = ten_thousand.filter(lambda line: '<redirect title=' not in line).filter(lambda x: x.startswith('</mediawiki')==False)
ten_thousand.count()

'''
#find all titles, check that titles are valid
def get_titles(line):
    title = re.findall('<title>(.*)</title>?',line)
    title_len = len(title)
    if title_len == 1: return title[0]
    elif title_len == 0: return '__no_title__'
    else: return '__weird...__'

titles = articles_less_redirects.map(lambda line: get_titles(line))
titles.count()
#output 8984694

titles.filter(lambda x: x == '__weird...__').count()
    #this output 0 when I ran it
titles.filter(lambda x: x == '__no_title__').count()
    #this output 1 when I ran it
no_name_article.first()
    #output '</mediawiki> '
#delete unwanted '</mediawii> ' title
titles = titles.filter(lambda x: x != '__no_title__')
titles.count() #confirm that count has dropped by 1
articles = articles.filter(lambda x: x != '</mediawiki> ')
articles.count() #confirm that count has dropped by 1
'''

def get_title_and_wikilinks(line):
    title = re.findall('<title>(.*)</title>?',line)[0]
    wl = re.findall('\[\[(.*?)\]\]',line)
    wikilinks = set()
    for link in wl:
        if 'File:' in link or 'User:' in link:
            continue
        wikilinks.add(link.split('|')[0])
    return (title,wikilinks)

titles_links = ten_thousand.map(get_title_and_wikilinks)
t_broadcast = sc.broadcast(titles_links.map(lambda x: x[0]).collect())

'''
bad_links = titles_links.flatMap(lambda x: x[1]).filter(lambda x: x not in t_broadcast.value).distinct()
bad_links.count()

good_links = titles_links.flatMap(lambda x: x[1]).filter(lambda x: x in t_broadcast.value).distinct()
good_links.count()
'''

def filter_bad_links(links,b):
    good_links = set()
    for link in links:
        if link in b:
            good_links.add(link)
    return good_links

#remove links that do not match to a tile
good_titles_links = titles_links.map(lambda x: (x[0],filter_bad_links(x[1],t_broadcast.value)))

t_broadcast.unpersist()

def make_graph(a,b):
    a.update(b)
    return a

#create a broadcasted dictionary representing wikipedia's article graph
#note: do not filter out titles with no wikilinks! although they do not link to anything, other articles may link to them,
#wwhich will cause an error in the find_end function when the links for an artilce reference this graph_broadcast variable.
#titles with no links are filtered out below, right before being passed to the find_end function
graph_broadcast = sc.broadcast(good_titles_links.map(lambda x:{x[0]:x[1]}).reduce(lambda a,b: make_graph(a,b)))

def find_end(title,graph,end='Anarchism'):
    start = title
    Q = [start]
    paths = {start:[start]}
    while Q:
        q_update = []
        for node in Q:
            if node == end: #######repair this part
                return (start,paths[node],len(paths[node]))
            for neighbor in graph[node]:
                if neighbor in paths:
                    continue
                temp = list(paths[node])
                temp.append(neighbor)
                paths[neighbor] = temp
                q_update.append(neighbor)
            Q = q_update
    return (start,[],-1)

#filter out titles with no wikilinks, then find shortest path to target
paths = good_titles_links.filter(lambda x: len(x[1]) != 0).map(lambda x: find_end(x[0],graph_broadcast.value))

connecting_paths = paths.filter(lambda x: x[2] != -1)

connecting_paths.map(lambda x: x[2]).mean()

x,y = paths.map(lambda x: x[2]).histogram([-1.5,0,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5])

paths.coalesce(4).saveAsTextFile('s3n://{}:{}@wiki-2016/paths_coalesce4'.format(access-key,secret-key))

pkl.dump(graph, open("//root/graph.pkl", "wb"))

#calculate avg number of links in an article
good_titles_links.map(lambda x: len(x[0])).mean()

def link_dicts(x):
    temp_dict = {}
    perms = itertools.permutations(x,2)
    for i in perms:
        temp_dict[i] = 1
    return temp_dict

def link_counts(a,b):
    for k,v in b.iteritems():
        a[k] = a.get(k,0) + 1
    return a

def find_common_links(links):
    common_links = []
    perms = itertools.permutations(links,2)
    for i in perms:
        common_links.append((i,1))
    return common_links

#create common-links pair rdd
#filter out pairs with less than 3 shared links
#the risk of filtering is removing useful recommendations for articles with very few links
shared_links_dict = good_titles_links.flatMap(lambda x: find_common_links(x[1])).reduceByKey(lambda a,b: a+b).filter(lambda x: x[1] > 2)

#this took about 10 seconds to run on 7,800 lines
shared_links_dict.count()

#remove existing links, then sort by value (the - in the lambda function reverses the sort)
shared_links_dict.filter(lambda x: x[0][1] not in graph[x[0][0]]).sortBy(lambda x:-x[1]).take(1000)

#sort by value (the - in the lambda function reverses the sort)
shared_links_dict = shared_links_dict.sortBy(lambda x:-x[1])
