#put all pages on one line

f = open('enwiki-latest-pages-articles.xml') #this is the unzipped direct download from
w = open('one_line_articles.txt','w')

for line in f:
    if line.startswith('  </page>'):
        w.write('\n'')
    w.write(line," ") #######figure out how to suppress the newline

w.close()
f.close()

#next steps: see spark_load_article_titles.py
