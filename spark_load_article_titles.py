#do this in Spark!
#step 2-a: delete entries with redirect tags:
#step 2-b: load all article titles in a db
#step 2-c: load all connections into
f = open('one_line_articles')
for line in f:
    if '<redirect title=' in f:
        delete line from file ##########
