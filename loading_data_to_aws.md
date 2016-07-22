#load wiki to S3 bucket
-create S3 bucket named wiki-2016

-use this command from local project file:
aws s3 cp enwiki-latest-pages-articles.xml s3://wiki-2016/enwiki-latest-pages-articles.xml.bz2

#copy wiki to ec2 from S3
log into ec2 instance:
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 login wiki_cluster

update aws cli with this command:
yum update

enter new tmux session in case the network goes down mid-transfer:
tmux

enter your volume with 300GB of storage:
cd /mnt

create file to copy S3 data into:
touch enwiki-latest-pages-articles.xml.bz2

copy data into newly created file:
aws s3 cp s3://wiki-2016/enwiki-latest-pages-articles.xml.bz2 enwiki-latest-pages-articles.xml.bz2

unzip file:
bzip2 -d enwiki-latest-pages-articles.xml.bz2

exit tmux session:
exit
