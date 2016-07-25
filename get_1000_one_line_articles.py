#f = urllib2.urlopen('https://s3.amazonaws.com/wiki-2016/one_l_a.txt')
f = open('one_line_articles.txt')
w = open('1000_one_line_articles.txt','w')

count = 0
for line in f:
    w.write(line)
    count += 1
    if count == 1000:
        break
w.close()
f.close()
