###set up aws_creds in bash profile:
nano .zshrc
export AWS_ACCESS_KEY_ID=(no quotes...)
export AWS_SECRET_ACCESS_KEY=(none here either...)
source .zshrc
echo $AWS_SECRET_ACCESS_KEY
echo $AWS__ACCESS_KEY_ID

--------reorder pause, unpause, notebook sessions, etc to the bottom- make a section called useful notes


###update .pem file permissions
chmod 400 "student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem"

###launch ec2 cluster
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 -s 1 --instance-type=cr1.8xlarge --copy-aws-credentials --ebs-vol-size=200 launch wiki_cluster_1s

-k: Name of your key-pair
-i: Path to your (.pem) file
-r: AWS region for your key-pair
--instance-type: instance type (I tried these configerations: 18 slaves m1.large, 9 slaves m4.xlarge, 1 slave cr1.8xlarge)
-s: The number of workers

###secure-copy over the install script to master node
scp -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem student_work/Sean/wikilinks/install_scripts/install_these root@<masters public DNS>:/root/.

###log into master node
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i ~/student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 login wiki_cluster_1s

###run install script
source install_these

###open new tmux session called 'notebook'
tmux new -s notebook

###open new python notebook sever
IPYTHON_OPTS="notebook --ip=0.0.0.0" /root/spark/bin/pyspark --executor-memory 180G --driver-memory 180G &

when specifying the executor and driver memory, allocate it so that you use 60-75% of your memory. In this example, the master (driver) and slaves are all of EC2 instance type M1-large (the default), which have 7.5GB of RAM each. You can specify different instance types by adding the --

###update permissions and access notebook server and spark UI
update file permissions for ports 8080 and 8888:
go to AWS security groups, select master node, add rule to inbound security rules, give all ip addresses (0.0.0.0/0) access to port 8080

go here to open notebook server:
<masters public DNS>:8888

go here to access Spark's UI:
<masters public DNS>:8080

###open cluster user interface
go here:
http://<masters public DNS>:8080

###pause a cluster:
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 stop wiki_cluster

when paused, the cluster is only charged for storage space (not ec2 rental space)

###un-pause a cluster:
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 start wiki_cluster_1s

###ssh into EC2 instance:
ssh -i "Galvanize_Sean_ONeal.pem" root@<masters public DNS>




#steps on how to use this dataset:
#http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-public-data-sets.html#using-public-data-sets-launching-set

###access S3 container:
('s3n://{}:{}@wikisample10/sample2'.format('access-key','secret-key'))
