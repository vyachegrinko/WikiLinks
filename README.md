# WikiLinks
This project explores the connections between pages in wikipedia. It also serves as my capstone project for the Galvanize Data Science Immersive program. The project consists of three parts: (1) a page link recommender system that identifies pages that aren't linked together that should be (2) A solution to the game popularized by Reddit, 6 degrees of separation from Hitler (3) a 'fraud detection' program that predicts whether or not a new wikipedia edit will be labeled as "non-constructive"

##Steps

1)  Download Wikipedia!
    do it here!!!:
    https://dumps.wikimedia.org/enwiki/latest/

    for this project, I used the dump from Jul 6, 2016:
    https://dumps.wikimedia.org/enwiki/20160706/

    ...and I utilized the following files:
        enwiki-latest-pages-articles.xml.bz2 #53GB once unzipped!
        enwiki-latest-pagelinks.sql.gz-rss.xml
        enwiki-latest-all-titles.gz

    this wikipedia dump contains just shy of 15 million articles!

2)  launch a spark cluster (see spark_cluster_initialization.md)
    ------------put in a brief description of cluster here--------

3)  load data into S3 bucket and onto spark cluster master node:
    follow the steps described in loading_data_to_aws.md

4)  preprocess xml data (see preprocess_xml.py and ...... for code)
    log into master node:
    spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i ~/student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 login wiki_cluster

    navigate to the /mnt directory (ths directory has 300+GB of disk space):
    cd /mnt

    create new file (this will hold the processed xml data):
    touch one_line_articles.txt

    open new ipython notebook session:
    IPYTHON_OPTS="notebook --ip=0.0.0.0" /root/spark/bin/pyspark --packages HyukjinKwon:spark-xml:0.1.1-s_2.10 --executor-memory 5G --driver-memory 5G &

    run the script in preprocess_xml.py. This script moves each wikipedia article and all of its xml lines into a single line. This is necessary for Spark to be able to parallelize the transformations to come.

    ***note*** there is also this really cool tool developed by databricks that allows you to read xml directly into a Spark SQL context, however I was unable to get it to work with pyspark...in any case, here are a few commands:

    open ipython notebook session with the spark-xml package included:
    IPYTHON_OPTS="notebook --ip=0.0.0.0" /root/spark/bin/pyspark --packages HyukjinKwon:spark-xml:0.1.1-s_2.10 --executor-memory 5G --driver-memory 5G &

    load xml into SQL context:
    from pyspark.sql import SQLContext
    sqlContext = SQLContext(sc)

5)  and finally, we are in a position to leverage the power of Spark!!!
