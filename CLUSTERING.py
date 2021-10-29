# -*- coding: utf-8 -*-
"""stock-market.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vpIL4m7frA0l40iS8GaZ_Jvmkqw-n2Wj
"""

import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt


data = pd.read_csv('projectdata.csv')
data.head()

X = data[["Stock Price","Crude Price"]]
#Visualise data points
plt.scatter(X["Stock Price"],X["Crude Price"],c='black')
plt.xlabel('Crude Price')
plt.ylabel('Stock Price')
plt.show()

# Step 1 and 2 - Choose the number of clusters (k) and select random centroid for each cluster

#number of clusters
K=4

# Select random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["Crude Price"],X["Stock Price"],c='black')
plt.scatter(Centroids["Crude Price"],Centroids["Stock Price"],c='red')
plt.xlabel('Crude Price')
plt.ylabel('Stock Price')
plt.show()

# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4

diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["Crude Price"]-row_d["Crude Price"])**2
            d2=(row_c["Stock Price"]-row_d["Stock Price"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["Stock Price","Crude Price"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['Stock Price'] - Centroids['Stock Price']).sum() + (Centroids_new['Crude Price'] - Centroids['Crude Price']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["Stock Price","Crude Price"]]


color=['blue','green','cyan','yellow']
for k in range(K):
    data=X[X["Cluster"]==k+1]
    plt.scatter(data["Crude Price"],data["Stock Price"],c=color[k])
plt.scatter(Centroids["Crude Price"],Centroids["Stock Price"],c='red')
plt.xlabel('Crude Price')
plt.ylabel('Stock Prices')
plt.show()

import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
data = pd.read_csv('projectdata.csv')
data.head()
X = data[["Stock Price","Gold Price"]]
#Visualise data points
plt.scatter(X["Stock Price"],X["Gold Price"],c='black')
plt.xlabel('Gold Price')
plt.ylabel('Stock Price')
plt.show()
# Step 1 and 2 - Choose the number of clusters (k) and select random centroid for each cluster
#number of clusters
K=4
# Select random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["Gold Price"],X["Stock Price"],c='black')
plt.scatter(Centroids["Gold Price"],Centroids["Stock Price"],c='red')
plt.xlabel('Gold Price')
plt.ylabel('Stock Price')
plt.show()
# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4
diff = 1
j=0
while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["Gold Price"]-row_d["Gold Price"])**2
            d2=(row_c["Stock Price"]-row_d["Stock Price"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["Stock Price","Gold Price"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['Stock Price'] - Centroids['Stock Price']).sum() + (Centroids_new['Gold Price'] - Centroids['Gold Price']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["Stock Price","Gold Price"]]
color=['blue','green','cyan','yellow']
for k in range(K):
    data=X[X["Cluster"]==k+1]
    plt.scatter(data["Gold Price"],data["Stock Price"],c=color[k])
plt.scatter(Centroids["Gold Price"],Centroids["Stock Price"],c='red')
plt.xlabel('Gold Price')
plt.ylabel('Stock Prices')
plt.show()