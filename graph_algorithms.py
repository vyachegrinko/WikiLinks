import pickle

#find shortest path
#start at the target node and propogate out to all connected nodes
#this implementation is onparallelizable
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
    return path_dict_out

graph = pickle.load(open('graph_50k.pkl','rb'))
path_dict_out = find_all_nodes(graph,start='Graph theory')

#identify nodes that the target failed to connect with by labelling these nodes with an empty list and a degree of separation of -1
titles = graph.keys() #integrate this into function after testing
for title in titles:
    if title not in path_dict_out:
        path_dict_out[title] = ([],-1)

#start at every node and work in towards the end node
#parallelizable implementation:
def update_paths_in(path,path_dict_in):
    indexer = len(path)
    for k in path:
        if k in path_dict_in:
            return
        path_dict_in[k] = (path[-indexer:],indexer)
        indexer -= 1

def find_end(line,path_dict_in,graph,end='Hitler'): #graph needs to be a dictionary
    start = line[0]
    Q = [start]
    paths = {start:[start]}
    current_best = -1
    while Q:
        q_update = []
        for node in Q:
            if node is end: #######repair this part
                update_paths(paths[node],path_dict_in)
                return
            for neighbor in graph[node]:
                if neighbor in paths:
                    continue
                paths[neighbor] = paths[node].append(neighbor)
                q_update.append(neighbor)
            Q = q_update
    path_dict_in[start] = ([],-1)

path_dict_in = {'Hitler':([],0)}
broadcasted_graph #this already exists in my spark program



#after calling these functions, do this to update node not within reach of the end node:
for title in titles:
    if title not in path_dict_in:
        path_dict_in[title] = ([],-1)

##########################################
##########################################
#############fixing problem above#########
def find_end(line,path_dict_in,graph,end='Hitler'): #graph needs to be a dictionary
    start = line[0]
    Q = [start]
    paths = {start:[start]}
    shortest_path = []
    shortest_len = 1
    counter = 0
    while Q:
        if shortest_path:
            counter += 1
        q_update = []
        for node in Q:
            if node is end: #######repair this part
                update_paths(paths[node],path_dict_in)
                return
            if node in path_dict_in:
                if shortest_path and shortest_len < path_dict_in[node][1]:
                    continue
                shortest_path = paths[node].extend(path_dict_in[node][0])
                shortest_len = len(shortest_path)
                continue
            for neighbor in graph[node]:
                if neighbor in paths:
                    continue
                paths[neighbor] = paths[node].append(neighbor)
                q_update.append(neighbor)
            Q = q_update
            if shortest_path:
                if counter = shortest_len:
                    update_paths(shortest_path,path_dict_in)
    path_dict_in[start] = ([],-1)

#after calling these functions, do this to update node not within reach of the end node:
for title in titles:
    if title not in path_dict_in:
        path_dict_in[title] = ([],-1)

##########################################
#####one row at a time implementation#####
##########################################
def find_end(line,graph,end='Anarchism'):
    start = line.keys()[0]
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
    return ([],-1)
