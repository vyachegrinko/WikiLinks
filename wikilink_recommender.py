import pickle as pkl
import itertools
import operator

graph = pkl.load(open('gephi_docs/graph_50k.pkl','rb'))

common_links = {}
counter = 0
for k,v in graph.iteritems():
    perms = itertools.permutations(v,2)
    for perm in perms:
        if perm[0] == 'World War II':
            common_links[perm] = common_links.get(perm,0) + 1
    counter += 1
    print counter

for k,v in common_links.items():
    if k[1] in graph[k[0]]:
        del common_links[k]

for k,v in common_links.iteritems():
    common_links[k] = float(v)/len(graph[k[0]])

sorted_common_links = sorted(common_links.items(), key=operator.itemgetter(1),reverse=True)


'''
for k,v in path_dict_out.iteritems():
    try:
        important_nodes[v[0][1]] = important_nodes.get(v[0][1],0) + 1
    except:
        continue

sorted_important_nodes = sorted(important_nodes.items(), key=operator.itemgetter(1),reverse=True)

most important nodes into WWII:
[(u'Romani people', 5313),
 (u'Charles de Gaulle', 2412),
 (u'Netherlands', 2309),
 (u'Second Sino-Japanese War', 1866),
 (u'Mongolia', 1842),
 (u'Manhattan Project', 1734),
 (u'Molotov\u2013Ribbentrop Pact', 1543),
 (u'Attack on Pearl Harbor', 1208),
 (u'Battle of Okinawa', 1135),
 (u'Battle of Britain', 1088),
 (u'Norway', 902),
 (u'United Kingdom', 776),
 (u'Asia', 732),
 (u'Ukraine', 616),
'''
