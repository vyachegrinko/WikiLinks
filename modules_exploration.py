import pandas as pd
import numpy as np

df = pd.read_csv('gephi_docs/nodes_50k.tsv',sep='\t')
df.groupby('modularity_class').count()
df = df[df['modularity_class'] < 24]
df = df[df['modularity_class'] != 18]
df = df[df['modularity_class'] != 19]
df = df[df['modularity_class'] != 20]
df = df[df['modularity_class'] != 21]
df = df[df['modularity_class'] != 22]
df = df.sort_values('pageranks',ascending=False)

zero = df[df['modularity_class'] == 0].head(50)['id']
one = df[df['modularity_class'] == 1].head(50)['id']
two = df[df['modularity_class'] == 2].head(50)['id']
three = df[df['modularity_class'] == 3].head(50)['id']
four = df[df['modularity_class'] == 4].head(50)['id']
five = df[df['modularity_class'] == 5].head(50)['id']
six = df[df['modularity_class'] == 6].head(50)['id']
seven = df[df['modularity_class'] == 7].head(50)['id']
eight = df[df['modularity_class'] == 8].head(50)['id']
nine = df[df['modularity_class'] == 9].head(50)['id']
ten = df[df['modularity_class'] == 10].head(50)['id']
eleven = df[df['modularity_class'] == 11].head(50)['id']
twelve = df[df['modularity_class'] == 12].head(50)['id']
thirteen = df[df['modularity_class'] == 13].head(50)['id']
fourteen = df[df['modularity_class'] == 14].head(50)['id']
fifteen = df[df['modularity_class'] == 15].head(50)['id']
sixteen = df[df['modularity_class'] == 16].head(50)['id']
seventeen = df[df['modularity_class'] == 17].head(50)['id']
twentythree = df[df['modularity_class'] == 23].head(50)['id']


'''#################ZERO###############################'''
tight bluish cluster in upper orange
2597/50000




'''#################ONE###############################'''
upper lighter orange
2923




'''#################TWO###############################'''
top dark pink
2945/50000



'''#################THREE###############################'''
upper light-ish blue
3887/50000

342                                               Italy
1096                                       Roman Empire
87                                         Christianity
742                                                Rome
634                                         Middle Ages
1608                                            Judaism
3507                            Eastern Orthodox Church
16                                                Bible
3147                                          Jerusalem
1887                                     Constantinople
700                                       New Testament
1875                                             Sicily
2639                                             Venice
1097                                    Julian calendar
6637                                           Holy See
770                                            Augustus
437                                         Charlemagne
277                                     Hebrew language
4680                                           Florence
550                                                Pope
189                                               Milan
826                                         Anno Domini
3509                                      Old Testament
1645                                         Alexandria
215                                         Mesopotamia
440                                  Holy Roman Emperor



'''#################FOUR###############################'''
lower darker orange cluster
4090/50000
654                            Time (magazine)
1861                       The Washington Post
2123                               Los Angeles
1057                                       CBS
32                                         NBC
854                                        CNN
426              American Broadcasting Company
593                             The New Yorker
53                              Academy Awards
47                                Warner Bros.
2538                             Rolling Stone
6498                                Amazon.com
7177                            Pulitzer Prize
4695                               The Beatles
54                                   Hollywood
2264                              The Simpsons
2562                              Grammy Award
4266                  Fox Broadcasting Company
4224                                 Channel 4
1063                                  Brooklyn
7156                                       MTV
3849     University of California, Los Angeles
10146                  The Walt Disney Company
5232                                James Bond
7404                             Elvis Presley
3304                          Steven Spielberg
8306                                 Coca-Cola
3709                     Madison Square Garden
3333                    Guinness World Records
3775                                Rock music
1039                                Tony Award
1353                                Doctor Who


'''#################FIVE###############################'''
middle pink
958/50000



'''#################SIX###############################'''
left blue ball
1371/50,000

5467                                      1967
5375                                      1933
5326                                      2014
5316                                      1942
5319                                      1941
5321                                      1944
5318                                      1940
5342                                      1968
5317                                      1943
5471                                      1963
5504                                      2007
5403                                      1939
5444                                      1978
5498                                      1973
November 20
March 15
February 27
August 25
December 25
March 2
December 30
1819
1886
February 12

'''#################SEVEN###############################'''
upper right gold
744/50000

310                    Old Norse
2787            J. R. R. Tolkien
1719                Isaac Asimov
1927          Robert A. Heinlein
312                   Prose Edda
3327             Science fiction
2785       The Lord of the Rings
307                  Poetic Edda
233                      Beowulf
5735      Dungeons &amp; Dragons
2792                  The Hobbit
24349                  Greg Egan
3414                        Loki
5155            Michael Moorcock
5100             Terry Pratchett

'''#################EIGHT###############################'''
large bottom pink
6613/50000



'''#################NINE###############################'''
lower, poorly clustered bright green
475/50000

2852                                 Toronto
3118                                 Ontario
4589                  National Hockey League
4163                        British Columbia
3769                               Vancouver
3494                                  Ottawa
4157                                 Alberta
4168                                Manitoba
4640               Newfoundland and Labrador
2031       Canadian Broadcasting Corporation
8061                             Quebec City
4159                            Saskatchewan
11199                    Toronto Maple Leafs
5056                              Hudson Bay
5053     Provinces and territories of Canada
5659                   Northwest Territories
8521                    Prince Edward Island
1661                         Canadian dollar
18177               Canadian Football League
4536                             Stanley Cup
8819                                   Yukon
15738                      Canadian football
10363                       Canadian English
1060                Canadian Pacific Railway



'''#################TEN###############################'''
gold (contains largest PageRank node)
3663/50000

149               World War II
407                    Germany
147               Soviet Union
943                     Europe
171                     Russia
67                       Paris
671                Switzerland
126                     Poland
83                Nazi Germany
531          French Revolution
120          Holy Roman Empire
577                    Belgium
3571                   Ukraine
1985                    Vienna
1115                   Romania
104              German Empire
1194                   Hungary
586                    Finland
100                   Napoleon
318                     Moscow

'''#################ELEVEN###############################'''
3506/50000
dark red on the right

130                 Oxford University Press
143              Cambridge University Press
2180                                  Earth
1705                        Albert Einstein
1026                    Columbia University
1698                           Isaac Newton
336                                    Moon
4843                   Princeton University
1348                                    Sun
1776                                Ptolemy
12088                     Set (mathematics)
3840                  University of Chicago
3608          International System of Units
6236                        Euclidean space
10699                   Scientific American
7306                            Mathematics
7924     United States Department of Energy
9211                                Physics
6937            International Space Station
1357                                  Venus
8271                         René Descartes
338                                 Jupiter

'''#################TWELVE###############################'''
bottom right dull blue
3848/50000

658                                           Microsoft
1557                                  Microsoft Windows
2362                                           Internet
602                                             Unicode
1320                           C (programming language)
3283                                         Apple Inc.
935                                 Stanford University
1226              Massachusetts Institute of Technology
2208                                     World Wide Web
5042                                              ASCII
1738                                              Intel
2188                        Java (programming language)
2364                           Portable Document Format
1219                 University of California, Berkeley
4103                                                C++
1050                                   General Electric
4834                  Federal Communications Commission
4470                             Federal Standard 1037C
8691     National Institute of Standards and Technology
10700         International Electrotechnical Commission
2235                                   Wired (magazine)
1726                      Digital Equipment Corporation
8932                      Python (programming language)
4318                                           Ethernet
3301                                               Sony
8926                                               HTML


'''#################THIRTEEN###############################'''
upper middle light purple
2273/50000

44                                Latin
165                                China
1130                               India
260                       Greek language
276                      French language
1103                               Japan
205                      German language
1397             Encyclopedia Britannica
4132                              Muslim
2929                    Italian language
678                             Hinduism
1278                            Sanskrit
202                     Russian language
1403                 Portuguese language
1372           Oxford English Dictionary
957                            Hong Kong
6338             Indo-European languages
1385                    Chinese language

'''#################FOURTEEN###############################'''
small lower, bright, light blue cluster between large pink and large dark blue
82/50000

33873            Texas hold 'em
20597           Lowball (poker)
23548            Omaha hold 'em
22787       Declaration (poker)
23546             Bluff (poker)
32449     World Series of Poker
34701    List of poker variants
10376              Draw (poker)
33450               Out (poker)
38535                  Nut hand
38797              Playing card
23547            High-low split
32083            Precision Club
6890                Cards speak
41411        Aggression (poker)

'''#################FIFTEEN###############################'''
center bright green
4883/50000

more geography stuff



'''#################SIXTEEN###############################'''
light blue somewhere
16=3/50000

SKIP



'''#################SEVENTEEN###############################'''
green ball of mess in the middle
37/50000

24050    Wikipedia:Complete list of encyclopedia topics...
41604    Wikipedia:Complete list of encyclopedia topics...
48233    Wikipedia:Complete list of encyclopedia topics...
48221    Wikipedia:Complete list of encyclopedia topics...
40755    Wikipedia:Complete list of encyclopedia topics...
45238    Wikipedia:Complete list of encyclopedia topics...
48234    Wikipedia:Complete list of encyclopedia topics...
48232    Wikipedia:Complete list of encyclopedia topics...
48231    Wikipedia:Complete list of encyclopedia topics...

'''#################TWENTYTHREE###############################'''
dark green in the middle/right
3579/50000

1623                                                DNA
2754                                   Nature (journal)
1417                                        Nobel Prize
2100                                      Carl Linnaeus
1615                                        Pleistocene
2591                                                RNA
4145                                                HIV
2383            United States Department of Agriculture
823                                               X-ray
1853                                         Cretaceous
9504                                   Escherichia coli
1628                                           Holocene
1455                       Food and Drug Administration
6692                                      New Scientist
1614                                            Miocene
Adenosine triphosphate
Paleozoic
