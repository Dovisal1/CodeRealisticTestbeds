import matplotlib
matplotlib.use('Agg')
import pylab as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import sys
import pandas as pd
import numpy as np
pd.set_option('max_columns', 50)

full = pd.read_csv('dat/unit_report.csv', error_bad_lines=False)[['unit_id','speed','upload_speed']]
#csvmspeeddown = pd.read_csv('dat/curr_httpgetmt.csv', error_bad_lines=False)[['unit_id','bytes_sec']]
#csvmspeedup = pd.read_csv('dat/curr_httppostmt.csv', error_bad_lines=False)[['unit_id','bytes_sec']]

full = full.dropna()
uniquedown=list(full.unit_id)
#print full[full.unit_id==6]["Speed_down"]*.0000080
#downs = [float((full[full.unit_id == i]['Speed_down'])) * .0000080 for i in uniquedown]
downs=[]
for i in uniquedown:
	splitup=full[full.unit_id == i]["speed"].tolist()[0]
	downs.append(splitup*.0000080)


plt.xlabel('Advertised DL speed of households (Mbps)')
plt.ylabel('Frequency in MBA dataset')
weights = np.ones_like(downs)/len(downs)
plt.hist(downs, bins=50, weights=weights)
#sns.distplot(downs, bins=20, kde=False)
plt.show()
#sns_plot.savefig("seaborntry.png")
plt.savefig("percentDL.svg")


uniqueup=list(full.unit_id)#csvmspeedup.unit_id))
ups=[]

#ups = [float((full[full.unit_id == j]['Speed_up'][0])) * .0000080 for j in uniqueup]
for i in uniqueup:
        splitin=full[full.unit_id == i]["upload_speed"].tolist()[0]
        ups.append(splitin*.0000080)


plt.close()#clear old plot
#upplot=sns.barplot(x="speed range", y="percent", data=ups)
plt.xlabel('Advertised UL speed of households (Mbps)')
plt.ylabel('Frequency in MBA dataset')
weights = np.ones_like(ups)/len(ups)
plt.hist(ups, bins=50, weights=weights)
#plt.gca().yaxis.set_major_formatter(formatter)
#plt.show()
plt.savefig("percentUL.svg")
print "added"
