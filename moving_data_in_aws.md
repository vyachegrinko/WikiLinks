###load wiki to S3 bucket
-create S3 bucket named wiki-2016

-use this command from local project file:
aws s3 cp enwiki-latest-pages-articles.xml s3://wiki-2016/enwiki-latest-pages-articles.xml.bz2

-make file public (right click it and click on "make public")

###copy wiki from S3 to ec2
-log into ec2 instance:
spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 login wiki_cluster

-update aws cli with this command:
yum update

-enter new tmux session (important step to do so that if a connection is dropped, the data transfer will not be interrupted):
tmux

-enter your volume with 300GB of storage:
cd /mnt

-create file to copy S3 data into:
touch enwiki-latest-pages-articles.xml.bz2

-copy data into newly created file:
aws s3 cp s3://wiki-2016/enwiki-latest-pages-articles.xml.bz2 enwiki-latest-pages-articles.xml.bz2

-unzip file:
bzip2 -d enwiki-latest-pages-articles.xml.bz2

###copy file from ec2 to S3 (if need be...)
aws s3 cp one_line_articles.txt s3://wiki-2016/one_line_articles.txt

-exit tmux session:
exit

###copy file from ec2 to local:
scp -i Galvanize_Sean_ONeal.pem root@<mastersDNS>:/path_to_file/file .

###attach a volume
go to the volume in the AWS console and under actions, select 'attach.' choose the ec2 instance to attach to


###mount a volume
once the volume is attached, it must be mounted. ssh into your instance:
ssh -i "filename.pem" root@<master's public DNS>

list attached volumes:
lsblk

determine if your volume has a file structure (if it does not, then we will need to make one ourselves):
sudo file -s device

If the output of the previous command shows simply data for the device, then there is no file system on the device and you need to create one like so:

sudo mkfs -t ext4 device_name

make a directory to mount the volume to:
sudo mkdir mount_point

mount the device:
sudo mount device_name mount_point

and finally...update file permissions:
sudo chmod 777
