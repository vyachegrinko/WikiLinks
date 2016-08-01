#f = urllib2.urlopen('https://s3.amazonaws.com/wiki-2016/one_l_a.txt')
f = open('enwiki-latest-pages-articles.xml')
w = open('articles_sample.txt','w')

count = 0
for line in f:
    if line.startswith('  </page>'):
        count += 1
    w.write(line)
    if count == 1000:
        break
w.close()
f.close()

'''
for line in f:
    if line.startswith('  <'):
        tags.add(line)

tags
>{'  </page>\n', '  </siteinfo>\n', '  <page>\n', '  <siteinfo>\n'}
'''
