#process xml data to .txt file where each line is one article
#run this somewhere with at least 60GB of free disk space

f = open('enwiki_2016_ect.txt')
w = open('one_line_articles.txt','w')

#counter = 0
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
#    counter += 1
#    if counter > 999:
#        w.flush()
f.close()
w.close()

#articles = sc.textFile("s3n://{}:{}@wiki-2016/enwiki_2016.txt".format(access-key,secret-key))
articles.first()

#try one of these
#samples = sc.textFile('file///root/articles_sample.txt')
#samples = sc.textFile('file///articles_sample.txt')
#samples = sc.textFile('file//articles_sample.txt')
