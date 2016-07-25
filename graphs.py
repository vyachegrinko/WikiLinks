#start at end node and propogate out to all connected nodes
#nonparallelizable implementation
def update_paths_out(dist,Q,dist_dict,graph)
    next_Q = []
    for node in Q:
        if node not in path_dict_out:
            path_dict_out[node] = (path_dict_out[node][0],dist)
            for neighbor in graph[node]:
                if neighbor not in path_dict_out:
                    next_Q.append(neighbor)
    return next_Q

path_dict_out = {'Hitler':(['Hitler'],0)}
broadcasted_graph #this already exists in my spark program

def find_all_nodes(path_dict_out,graph, start='Hitler'): #graph is a tuple of (node, (tuple of edges))
    Q = [start]
    dist = 1
    while Q:
        Q = update_dict(dist,Q, dist_dict,graph))
        dist += 1
    return dist_dict
#after calling these functions, do this to update node not within reach of the end node:
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

path_dict_in = {'Hitler':([],0)}
broadcasted_graph #this already exists in my spark program

def find_end(line,path_dict_in,graph,end='Hitler'): #graph needs to be a dictionary
    start = line[0]
    Q = [start]
    paths = {start:[start]}
    current_best = -1
    while Q:
        q_update = []
        for node in Q:
            if node is end #######repair this part
                update_paths(paths[node],path_dict_in)
                return
            for neighbor in graph[node]:
                if neighbor is in paths:
                    continue
                paths[neighbor] = paths[node].append(neighbor)
                q_update.append(neighbor)
            Q = q_update
    path_dict_in[start] = ([],-1)

#after calling these functions, do this to update node not within reach of the end node:
for title in titles:
    if title not in path_dict_in:
        path_dict_in[title] = ([],-1)

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
            if node is end #######repair this part
                update_paths(paths[node],path_dict_in)
                return
            if node is in path_dict_in:
                if shortest_path and shortest_len < path_dict_in[node][1]:
                    continue
                shortest_path = paths[node].extend(path_dict_in[node][0])
                shortest_len = len(shortest_path)
                continue
            for neighbor in graph[node]:
                if neighbor is in paths:
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
