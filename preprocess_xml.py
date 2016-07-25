#process xml data to .txt file where each line is one article
#run this somewhere with at least 60GB of free disk space

f = open('enwiki_2016_ect.txt')
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
