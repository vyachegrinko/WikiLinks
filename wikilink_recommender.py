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
