import pickle as pkl
import itertools

graph = pickle.load(open('gephi_docs/graph_50k.pkl','rb'))

common_links = {}
#counter = 0
for k,v in graph.iteritems():
    perms = itertools.permutations(v,2)
    for perm in perms:
        if perm[1] not in graph[perm[0]]:
            common_links[perm] = common_links.get(perm,0) + 1
#    counter += 1
#    print counter

for k,v in common_links:
    if k[1] in graph[k[0]]:
        common_links.pop(k)
