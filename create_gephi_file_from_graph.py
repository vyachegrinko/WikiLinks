#load graph from ec2 to local:
# scp -i Galvanize_Sean_ONeal.pem root@<mastersDNS>:/path_to_file/graph.pkl

import pickle
graph = pickle.load(open('graph.pkl','rb'))

!rm graph_2pct.csv
!touch graph_2pct
f = open('graph_2pct.csv','w')
f.write('Source\tTarget\n')
for k,v in graph.iteritems():
    for i in v:
        f.write(k.encode('utf-8'))
        f.write('\t')
        f.write(i.encode('utf-8'))
        f.write('\n')
f.close()
