from numpy import random, array

#Create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
#    random.seed(1)
    pointsPerCluster = float(N)/k
    X = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        print incomeCentroid, ' ', ageCentroid
        for j in range(int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])
    X = array(X)    
    return X
    
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

print 'Initial centroids:'
data = createClusteredData(500, 5)

nclusters=5
model = KMeans(n_clusters=nclusters)

# Note I'm scaling the data to normalize it! Important for good results.
model = model.fit(scale(data))

# We can look at the clusters each data point was assigned to
print '\nK-means with '+str(nclusters)+' clusters:'
print model.labels_ 

# visualize the data:
col=['r','g','b','y','black','purple']
plt.figure(figsize=(8, 6))
for i in range(model.n_clusters):
    plt.scatter(data[model.labels_==i,0], data[model.labels_==i,1], c=col[i],label=i)
plt.legend()
plt.show()

