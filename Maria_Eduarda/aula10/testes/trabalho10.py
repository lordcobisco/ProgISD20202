print(__doc__)

import csv
from time import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn import datasets
#from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import pandas as pd
import math
from sklearn.preprocessing import MinMaxScaler

def ler():
     with open('C:\\Users\\eduar\\OneDrive\\Documentos\\GitHub\\ProgISD20202-1\\Maria_Eduarda\\aula10\\Trabalho\\dados10.csv','r') as fileObject:
             dataset=[]
             for line in fileObject:
                for dadosEsp1 in line.split(","):
                     #print(float(dadosEsp1))
                     dataset.append(float(dadosEsp1)) 
             return dataset
def GetX():
    coleta=ler()
    X=[]
    for i in range (0, int((len(coleta)/2))):
        X.append(coleta[i])
    return X

def GetY():
    coleta=ler()
    Y=[]
    for i in range (int((len(coleta)/2)), int(len(coleta))):
        Y.append(coleta[i])
    return Y

def calculate_wcss(data):
    wcss = []
    X=data
    for n in range(2, 21):
        kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
        wcss.append(kmeans.inertia_)

    return wcss
def optimal_number_of_clusters(data):
    wcss=calculate_wcss(data)
    x1, y1 = 2, wcss[0]
    x2, y2 = 20, wcss[len(wcss)-1]
    distances = []
    for i in range(len(wcss)):
        x0 = i+2
        y0 = wcss[i]
        numerator = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
        denominator = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
        distances.append(numerator/denominator)
    
    return distances.index(max(distances)) + 2

X_digits = np.array([GetX()])
y_digits=np.array(GetY())
dataset=np.array([ler()])
i,j=dataset.shape 
tam=int(j/4)
dataset=dataset.reshape(4,tam)
data = scale(X_digits) 
i,j=data.shape
data=data.reshape(j,i)
n_samples, n_features = X_digits.shape #rows, and Colums.
n_digits = optimal_number_of_clusters(dataset)
labels = y_digits
print(n_digits)
sample_size = 300

print("n_digits: %d, \t n_samples %d, \t n_features %d"
      % (n_digits, n_samples, n_features))

def bench_k_means(estimator, name, data,y):
    t0 = time()
    estimator.fit(data,y)
    print('%-9s\t%.2fs\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(labels, estimator.labels_),
             metrics.completeness_score(labels, estimator.labels_),
             metrics.v_measure_score(labels, estimator.labels_),
             metrics.adjusted_rand_score(labels, estimator.labels_),
             metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean',
                                      sample_size=sample_size)))

bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10),
              name="k-means++", data=data,y=y_digits)

bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10),
              name="random", data=data,y=y_digits)
#in this case the seeding of the centers is deterministic, hence we run the
# kmeans algorithm only once with n_init=1
pca = PCA(n_components=n_digits).fit(data)
bench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1),
              name="PCA-based",
              data=data)
print(82 * '_')

# #############################################################################
# Visualize the results on PCA-reduced data

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
kmeans.fit(reduced_data)

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='red', zorder=10, label = 'Cluster 1')
plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
          'Centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()