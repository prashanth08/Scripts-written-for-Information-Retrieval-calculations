import math
import numpy as np

# copy paste input TODO
collection1 = {
	'1':"ash ketchum pokemon pikachu professor oak",
	'2':"ash leaves pokemon pikachu ash sad pikachu sad",
	'3':"ash tree elm tree oak tree maple tree",
	'4':"white ash tree orange tree leaves",
	'5':"orange apple grapefruit orange juice"
}

collection = {
	'1':"cornell cayuga bigred bears",
	'2':"cornell cornell nyc bigred bigred",
	'3':"cornell bells ring everyday",
	'4':"cornell cornell cold ring ring",
	'5':"bigred bigred bells ring everyday very cool"
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
		tfidf = termFrequency(word,doc)#*inverseDocumentFrequency(word)
		docVector.append(tfidf)

	return docVector

def euclideanDistance(doc1, doc2):
	d1 = vectorizeDocument(doc1)
	d2 = vectorizeDocument(doc2)

	total = 0
	for i in range(0,len(d1)):
		total = total + math.pow((d1[i]-d2[i]),2)

	return math.sqrt(total)

def tfCosineSimilarity(doc1,doc2):
	d1 = vectorizeDocument(doc1)
	d2 = vectorizeDocument(doc2)

	similarity = np.dot(d1,d2)/(np.linalg.norm(d1)*np.linalg.norm(d2));
	return similarity

#TODO change the cluster , when using cosine similarity, reverse the direction of 
def clusterCost(c1,c2):
	minimum = float('inf');

	for doc1 in c1:
		for doc2 in c2: 
			cst = tfCosineSimilarity(doc1,doc2)#euclideanDistance(doc1,doc2)
			# change < to > if euclidean , minimum to 0 , 
			if cst < minimum:
				minimum = cst

	return minimum;

def completeLinkCluster(k):

	clusters = {}

	for doc in collection.keys():
		clusters[doc] = [doc]

	bestA = None
	bestB = None
	bestCost = None
	while len(clusters) > k:

		maximum = 0;  #set maximun as infinity
		for c1 in clusters.keys():
			for c2 in clusters.keys():
				if c1 == c2:
					continue
				else:
					mergeCost = clusterCost(clusters[c1],clusters[c2])
					# print mergeCost,c1,c2 # reverse the sign for euclidena
					if mergeCost > maximum:
						maximum = mergeCost
						bestA = c1;
						bestB = c2;

		for doc in clusters[bestB]:
			clusters[bestA].append(doc)

		del clusters[bestB]
		bestCost = maximum

	print clusters,maximum

if __name__ == '__main__':
	buildVocabulary()
	print clusterCost(['1'],['2'])
	print clusterCost(['5'],['4'])
	print "cluster for 4"
	completeLinkCluster(4)
	print "cluster for 3"
	completeLinkCluster(3)
	print "cluster for 2"
	completeLinkCluster(2)
	print "cluster for 1"
	completeLinkCluster(1)