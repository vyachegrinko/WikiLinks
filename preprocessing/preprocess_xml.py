#process xml data to .txt file where each line is one article
#unzip the wikipedia xml download (gunzip <file_name>, or bzip2 -d <file_name>)

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
