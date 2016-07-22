#put all pages on one line

#f = open('enwiki-latest-pages-articles.xml') #this is the unzipped direct download from
f = open('articles_sample.txt')
w = open('one_line_articles.txt','w')

for line in f:
    if line.startswith('  <page>'):
        w.write(line.strip())
        w.write(' ')
#        print 'found the start!'
        break

for line in f:
    if line.startswith('  </page>'):
        w.write(line)
#        print 'found an article!'
        continue
    w.write(line.strip())
    w.write(' ')

f.close()
w.close()
#next steps: see spark_load_article_titles.py
