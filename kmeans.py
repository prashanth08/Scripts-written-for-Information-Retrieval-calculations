import math
import numpy as np

collection = {
	'1':"ash ketchum pokemon pikachu professor oak",
	'2':"ash leaves pokemon pikachu ash sad pikachu sad",
	'3':"ash tree elm tree oak tree maple tree",
	'4':"white ash tree orange tree leaves",
	'5':"orange apple grapefruit orange juice"
}

vocabulary = []

def buildVocabulary():
	for doc in collection.keys():
		document = collection[doc].strip().split(' ')
		for word in document:
			if word not in vocabulary:
				vocabulary.append(word)

	print "Vocabulary"
	print vocabulary

def termFrequency(word, doc):
	count = 0
	document = collection[doc].strip().split(' ')
	for term in document:
		if word == term:
			count = count + 1;

	return count

def inverseDocumentFrequency(word):
	count = 0;
	for doc in collection.keys():
		document = collection[doc].strip().split(' ')
		if word in document:
			count = count + 1

	if count == 0:
		return 0
	else:
		return math.log(len(collection)/float(count))

def vectorizeDocument(doc):
	docVector = []

	for word in vocabulary:
		tfidf = termFrequency(word,doc)*inverseDocumentFrequency(word)
		docVector.append(tfidf)

	return docVector

def euclideanDistance(doc1, doc2):
	#d1 = vectorizeDocument(doc1)
	#d2 = vectorizeDocument(doc2)

	total = 0
	for i in range(0,len(doc1)):
		total = total + math.pow((doc1[i]-doc2[i]),2)

	return math.sqrt(total)

def tfCosineSimilarity(doc1,doc2):
	d1 = vectorizeDocument(doc1)
	d2 = vectorizeDocument(doc2)

	similarity = np.dot(d1,d2)/(np.linalg.norm(d1)*np.linalg.norm(d2));
	return similarity

def mapToCluster(centroids):

	clusters = {}

	for doc in collection.keys():
		document = vectorizeDocument(doc)
		minimum = float('inf')
		center = None
		for centroid in centroids:
			distance = euclideanDistance(document,centroid)
			#print distance
			if distance < minimum:
				minimum = distance
				center = centroid

		clusters[doc] = center

	return clusters

def reduceCluster(centroids,clusters):

	newCentroids = []
	count = 0

	for center in centroids:
		count = 0
		C = [0 for x in range(0,len(center))]
		for doc in clusters.keys():
			if np.subtract(clusters[doc],center).all()==0:
				C = np.add(C,center)
				count = count + 1

		newCentroids.append(np.dot(1/float(count),C))

	return newCentroids

def printClusters(centroids):
	for doc in collection.keys():
		document = vectorizeDocument(doc)
		minimum = float('inf')
		center = None
		for i in range(0,len(centroids)):
			distance = euclideanDistance(document,centroids[i])
			#print distance
			if distance < minimum:
				minimum = distance
				center = i

		print doc, center+1
		

def kmeansCluster(k):

	centroids = [vectorizeDocument('1'),vectorizeDocument('3'),vectorizeDocument('5')]#vector#random initializartion
	print centroids
	iteration = 0
	while iteration < 5:

		print "iteration",iteration

		clusters = mapToCluster(centroids)
		centroids = reduceCluster(centroids,clusters)
		iteration = iteration + 1
		
		#print clusters

	print "Final Clusters"
	print clusters
	print "Final Centroids"
	print centroids

	printClusters(centroids)

if __name__ == '__main__':
	buildVocabulary()
	kmeansCluster(3)
