'''
touch ola.txt
aws s3 cp s3://wiki-2016/one_l_a.txt ola.txt

ipython
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

def update_paths_out(dist,Q,dist_dict,graph)
    next_Q = []
    for node in Q:
        if node not in path_dict_out:
            path_dict_out[node] = (path_dict_out[node][0],dist)
            for neighbor in graph[node]:
                if neighbor not in path_dict_out:
                    next_Q.append(neighbor)
    return next_Q


def find_all_nodes(path_dict_out,graph, start='Hitler'): #graph is a tuple of (node, (tuple of edges))
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

    path_dict_out = {'Hitler':(['Hitler'],0)}

    find_all_nodes(path_dict_out,graph)
    for title in graph:
        if title not in path_dict_out:
            path_dict_out[title] = ([],-1)
