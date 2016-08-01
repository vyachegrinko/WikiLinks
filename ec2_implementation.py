#create gephi-importable wikilinks graph from one-line-articles.txt
import re

f = open('ola.txt.crdownload')
w = open('gephi_graph.tsv','w')

count = 0
w.write('Source\tTarget')
for line in f:
    if count == 50000:
        break
    if '<redirect title=' in line:
        continue
    if '</mediawiki' in line:
        continue
    wl = re.findall('\[\[(.*?)\]\]',line)
    title = re.findall('<title>(.*)</title>?',line)[0]
    if 'Wikipedia:' in title or 'Template:' in title or 'Portal:' in title or 'File:' in title or 'Category:' in title or '\t' in title or 'MediaWiki' in title:
        continue
    wikilinks = set()
    for link in wl:
        if 'File:' in link or 'User:' in link or 'Wikipedia:' in link or '\t' in link:
            continue
        if len(link) > 160:
            continue
        wikilinks.add(link.split('|')[0])
    if len(wikilinks) == 0:
        continue
    count += 1
    for link in wikilinks:
        w.write('\n')
        w.write(title)
        w.write('\t')
        w.write(link)

f.close()
w.close()



!touch gephi_graph2.tsv
f.close()
w.close()
f = open('gephi_graph.tsv')
w = open('gephi_graph2.tsv','w')

for line in f:
    if '\t\t' in line or '\t\n' in line or '\n\t' in line or line == '\n':
        continue
    if len(line.split('\t')) < 2:
        continue
    w.write(line)
w.write('test\ttest')






########create dictionary from one-line-articles.txt
import re

f = open('ola.txt.crdownload')
w = open('gephi_graph.tsv','w')

count = 0
w.write('Source\tTarget')
for line in f:
    if count == 50000:
        break
    if '<redirect title=' in line:
        continue
    if '</mediawiki' in line:
        continue
    wl = re.findall('\[\[(.*?)\]\]',line)
    title = re.findall('<title>(.*)</title>?',line)[0]
    if 'Wikipedia:' in title or 'Template:' in title or 'Portal:' in title or 'File:' in title or 'Category:' in title or '\t' in title or 'MediaWiki' in title:
        continue
    wikilinks = set()
    for link in wl:
        if 'File:' in link or 'User:' in link or 'Wikipedia:' in link or '\t' in link:
            continue
        if len(link) > 160:
            continue
        wikilinks.add(link.split('|')[0])
    if len(wikilinks) == 0:
        continue
    count += 1
    for link in wikilinks:
        w.write('\n')
        w.write(title)
        w.write('\t')
        w.write(link)

f.close()
w.close()











def get_title_and_wikilinks(line):
    title = re.findall('<title>(.*)</title>?',line)[0]
    wl = re.findall('\[\[(.*?)\]\]',line)
    wikilinks = set()
    for link in wl:
        if 'File:' in link or 'User:' in link:
            continue
        wikilinks.add(link.split('|')[0])
    return (title,wikilinks)

def update_paths_out(dist,Q,dist_dict,graph)
    next_Q = []
    for node in Q:
        if node not in path_dict_out:
            path_dict_out[node] = (path_dict_out[node][0],dist)
            for neighbor in graph[node]:
                if neighbor not in path_dict_out:
                    next_Q.append(neighbor)
    return next_Q


def find_all_nodes(path_dict_out,graph, start='Adolf Hitler'): #graph is a tuple of (node, (tuple of edges))
    Q = [start]
    dist = 1
    while Q:
        Q = update_dict(dist,Q, dist_dict,graph))
        dist += 1
    return dist_dict

if __main__=="__name__":
    import re

    ola = open('/ola.txt')
    graph = dict()
    for line in ola:
        a = get_title_and_wikilinks(line)
        graph[a[0]] = a[1]

    path_dict_out = {'Adolf Hitler':(['Adolf Hitler'],0)}

    find_all_nodes(path_dict_out,graph)
    for title in graph:
        if title not in path_dict_out:
            path_dict_out[title] = ([],-1)
