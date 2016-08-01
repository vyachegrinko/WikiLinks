import matplotlib.pyplot as plt
import seaborn as sns

#create wikilinks-per-article histogram
x =['0-5','6-20','21-50','51-100','101-200','201-300','301-400','401-500', '501-600','601-35,000']
y = [1554026, 2463944, 1808199, 557805, 191023, 43115, 15638, 6537, 3448, 7634]

current_palette = sns.color_palette(sns.cubehelix_palette(8))
sns.barplot(x,y,palette=current_palette)
plt.title('Wikilinks per Article',fontsize=24)
plt.xlabel('wikilinks per article',fontsize=15)
plt.ylabel('article count',fontsize=15)
plt.show()


###calculate path length stats:
dist_dict = {}
for k,v in path_dict_out.iteritems():
    dist_dict[v[1]] = dist_dict.get(v[1],0) + 1

x = []
y = []
for k,v in dist_dict.iteritems():
    x.append(k)
    y.append(v)

current_palette = sns.color_palette(sns.cubehelix_palette(8,n=12))
sns.barplot(x,y,palette=current_palette)
plt.title('Path Distances from the Graph Theory Article',fontsize=24)
plt.xlabel('distance',fontsize=15)
plt.ylabel('article count',fontsize=15)
plt.show()
