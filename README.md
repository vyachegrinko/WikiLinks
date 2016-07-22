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

3)  preprocess xml data (see preprocess_xml.py and ...... for code)
    log into master node:
    spark-1.6.1-bin-hadoop1/ec2/spark-ec2 -k Galvanize_Sean_ONeal -i ~/student_work/Sean/wikilinks/Galvanize_Sean_ONeal.pem -r us-east-1 login wiki_cluster

    navigate to the /mnt directory (ths directory has 300+GB of disk space):
    cd /mnt

    create new file (this will hold the processed xml data):
    touch one_line_articles.txt

    open new ipython notebook session:
    IPYTHON_OPTS="notebook --ip=0.0.0.0" /root/spark/bin/pyspark --packages HyukjinKwon:spark-xml:0.1.1-s_2.10 --executor-memory 5G --driver-memory 5G &

    run the script in preprocess_xml.py

#failed attempt to use databricks spark-xml tool... :(
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df = sqlContext.read.format('com.databricks.spark.xml').options(rowTag='page').load('enwiki-latest-pages-articles.xml')




##temp notes to myself
s3://wiki-2016/enwiki_2016.txt
f = urllib2.urlopen('https://s3.amazonaws.com/wiki-2016/enwiki_2016.txt')


import numpy as np
import pickle as pkl
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from pyspark.mllib.clustering import KMeans
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
PUNCTUATION = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))
