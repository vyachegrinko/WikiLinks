# WikiLinks
This project explores the connections between pages in wikipedia and serves as my capstone project for completion of the Galvanize Data Science Immersive program. The project consists of three parts: (1) a wikipedia "concept" clusterer, which identifies clusters of articles that are strongly linked together via wikilinks (2) a page link recommender system that identifies pages that aren't linked together that should be (3) A solution to the game popularized by the internet, 6 degrees of separation from <article title>. The following steps will allow you to reproduce the project:

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

2)  preprocess xml data (see preprocess_xml.py for code). Preprocessing includes placing every article on its own line. This is necessary in order for Spark to run computations in parallel on the data set

3)  load data into S3 bucket and onto spark cluster master node (see moving_data_in_aws.md).

4)  launch a spark cluster (see spark_cluster_initialization.md). For this project, I used two AWS EC2 instances, both of type cr1.8xlarge, which have 240GB of RAM and are optimized for in-memory computations- ideal settings for dealing with large networks.


    ***note*** there is a useful tool developed by databricks that allows you to read xml directly into a Spark SQL context, however it is not compatible with pyspark

5)  create wikilinks graph, find shortest path between any article and the chosen target article, and create page link recommendations (see spark_make_graph.py).

6)  copy graph data to local machine and create graph plot in gephi (see create_gephi_file_from_graph.py)
