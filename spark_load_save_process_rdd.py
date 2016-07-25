import re
import urllib2

load_s3_data = sc.textFile("s3n://{}:{}@wiki-2016/one_l_a.txt".format(access_key,secret_key))
#I think this will work as well:
#articles = sc.textFile("hdfs://ec2-107-23-213-96.compute-1.amazonaws.com:9000/mnt/one_line_articles.txt")

#save articles across cluster
load_s3_data.saveAsTextFile("/root/persistent-hdfs/wiki_test")

#open partitioned rdd!
articles = sc.textFile("hdfs://ec2-107-23-213-96.compute-1.amazonaws.com:9000/root/persistent-hdfs/wiki_test")

articles.count()

#filter out redirected 'articles'
articles_less_redirects = articles.filter(lambda line: '<redirect title=' not in line)

articles_less_redirects.count()

#find all titles
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

#function that returns a tuple of article title and a tuple of inter-wiki page links
def get_title_and_wikilinks(line):
    title = re.findall('<title>(.*)</title>?',line)[0]
    wl = re.findall('\[\[(.*?)\]\]',line)
    wikilinks = set()
    for link in wl:
        if 'File:' in link or 'User:' in link:
            continue
        wikilinks.add(link.split('|')[0])
    return (title,wikilinks)
t_l = articles.map(get_title_and_wikilinks)

titles_broadcast = sc.broadcast(titles.collect())

#bad_links = t_l.flatMap(lambda x: x[1]).filter(lambda x: x not in titles_broadcast.value)
#bad_links.count()

f.close()
f = open('1000_one_line_articles.txt')
rdd = []
for line in f:
    rdd.append(get_title_and_wikilinks(line))
for i in rdd:
    print i
    raw_input()
CHECK TO SEE IF ANY WIKILINKS ARE NOT INCLUDED IN TITLES:
SAVE TITLES AS A BROADCAST VARIABLE AND THEN DO A CHECK





import re
import urllib2

def get_title_and_wikilinks(line):
    title = re.findall('<title>(.*)</title>?',line)[0]
    wl = re.findall('\[\[(.*?)\]\]',line)
    wikilinks = set()
    for link in wl:
        if 'File:' in link or 'User:' in link:
            continue
        wikilinks.add(link.split('|')[0])
    return (title,wikilinks)

articles = sc.textFile("hdfs://ec2-107-23-213-96.compute-1.amazonaws.com:9000/root/persistent-hdfs/wiki_test")
articles_less_redirects = articles.filter(lambda line: '<redirect title=' not in line)
articles = articles.filter(lambda x: x != '</mediawiki> ')
titles_links_broadcast = sc.broadcast(articles.map(get_title_and_wikilinks).collect())
