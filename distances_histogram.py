import pickle
import seaborn as sns
import matplotlib.pyplot as plt
#find shortest path
#start at the target node and propogate out to all connected nodes
#this implementation is onparallelizable

graph = pickle.load(open('gephi_docs/graph_50k.pkl','rb'))

def update_paths_out(dist,Q,path_dict_out,graph):
    next_Q = []
    for node in Q:
        for neighbor in graph[node]:
            if neighbor not in path_dict_out:
                temp = list(path_dict_out[node][0])
                temp.append(neighbor)
                path_dict_out[neighbor] = (temp,dist)
                next_Q.append(neighbor)
    return next_Q, path_dict_out

#graph is a dicitonary containing nodes as keys and a set of outbound connections as values
def find_all_nodes(graph, start='Graph theory'): #graph is a tuple of (node, (tuple of edges))
    path_dict_out = {start:([start],0)}
    Q = [start]
    dist = 1
    while Q: #while Q is not empty
        Q, path_dict_out = update_paths_out(dist,Q,path_dict_out,graph)
        print dist, " degrees of separation completed" #monitor progress
        dist += 1
    titles = graph.keys() #integrate this into function after testing
    for title in titles:
        if title not in path_dict_out:
            path_dict_out[title] = ([],-1)
    return path_dict_out, dist

target = 'World War II'
path_dict_out, max_dist = find_all_nodes(graph,start=target)

#identify nodes that the target failed to connect with by labelling these nodes with an empty list and a degree of separation of -1


###calculate path length stats:
dist_dict = {}
for k,v in path_dict_out.iteritems():
    dist_dict[v[1]] = dist_dict.get(v[1],0) + 1

x = []
y = []
for k,v in dist_dict.iteritems():
    x.append(k)
    y.append(v)

current_palette = sns.color_palette(sns.diverging_palette(145, 280, s=85, l=25, n=max_dist))
sns.barplot(x,y,palette=current_palette)
plt.title('Path Distances from the "{}" Article'.format(target),fontsize=24)
plt.xlabel('distance',fontsize=15)
plt.ylabel('article count',fontsize=15)
plt.ylim(0,20000)
#plt.show()
