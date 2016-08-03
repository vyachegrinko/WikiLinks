import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#create wikilinks-per-article histogram
x =['0-5','6-20','21-50','51-100','101-200','201-300','301-400','401-500', '501-600','601-35,000']
y = [1554026, 2463944, 1808199, 557805, 191023, 43115, 15638, 6537, 3448, 7634]
y_round = [rount(float(i)/sum(y)*100,2) for i in y]
#current_palette = sns.color_palette(sns.cubehelix_palette(8))
sns.set_color_codes('deep')

sns.barplot(x,y,color='b')
sns.set_color_codes('deep')
plt.title('Wikilinks per Article',fontsize=30)
plt.xlabel('wikilinks per article',fontsize=18)
plt.ylabel('article count',fontsize=18)
plt.tick_params(labelsize=15)
plt.xticks(rotation=50)
plt.show()

#create PageRank distribution histogram
df = pd.read_csv('gephi_docs/nodes_50k.tsv',sep='\t')
x = np.array(df['pageranks'])

sns.distplot(x,bins=10**np.linspace(-6,-2,50),color='blue')
plt.xscale('log')
plt.xlim(.000003,.004)
plt.title('PageRank Distribution',fontsize=30)
plt.xlabel('PageRank',fontsize=18)
plt.ylabel('article count',fontsize=18)
plt.tick_params(labelsize=15)
