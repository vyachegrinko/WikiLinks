#set up aws_creds in bash profile:
nano .zshrc
export AWS_ACCESS_KEY_ID=  (no quotes...)
export AWS_SECRET_ACCESS_KEY=  (none here either...)
source .zshrc
echo $AWS_SECRET_ACCESS_KEY
echo $AWS__ACCESS_KEY_ID

#update .pem file permissions
chmod 400 "student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem"

#launch ec2 cluster with 6 slaves
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 -s 6 --copy-aws-credentials --ebs-vol-size=64 launch wiki_cluster

-k: Name of your key-pair
-i: Path to your (.pem) file
-r: AWS region for your key-pair
-s: The number of workers

#secure-copy over the install script to master node
scp -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem student_work/Sean/wikilinks/install_scripts/install_these root@<masters public DNS>:/root/.

#log into master node
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i ~/student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 login wiki_cluster

#run install script
source install_these

#open new tmux session called 'notebook'
tmux new -s notebook

#open new python notebook sever
IPYTHON_OPTS="notebook --ip=0.0.0.0" /root/spark/bin/pyspark --executor-memory 4G --driver-memory 4G &

when specifying the executor and driver memory, allocate it so that you use 60-75% of your memory (driver memory + executor memory * # of slaves)

#update permissions to port 8080
go to AWS security groups, select master node, add rule to inbound security rules, give all ip addresses (0.0.0.0/0) access to port 8080

#open notebook server:
go here:
http://<masters public DNS>:8888

#open cluster user interface
go here:
http://<masters public DNS>:8080

#pause a cluster:
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 stop wiki_cluster

when paused, the cluster is only charged for storage space (not ec2 rental space)

#un-pause a cluster:
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 start wiki_cluster

#ssh into EC2 instance:
ssh -i "Galvanize_Sean_ONeal.pem" root@<masters public DNS>


# DOWNLOAD WIKI FROM AWS!!!
here is the link to the database:

http://aws.amazon.com/datasets/wikipedia-xml-data/?tag=datasets%23keywords%23encyclopedic

US Snapshot ID (Linux/Unix): snap-8041f2e9
Size: 500GB
Source: Wikimedia Foundation (http://download.wikipedia.org/backup-index.html)

for this project, I used the version that was last updated November 24, 2015

the snapshot is saved in the us-east-1 region (important for later)

#steps on how to use this dataset:
#http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-public-data-sets.html#using-public-data-sets-launching-set

#access S3 container:
('s3n://{}:{}@wikisample10/sample2'.format('access-key','secret-key'))

#Download Wikipedia Here!!!
https://dumps.wikimedia.org/enwiki/latest/

for this project, I used the version created on Jul 6, 2016:
https://dumps.wikimedia.org/enwiki/20160706/
