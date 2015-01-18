import math

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
		tfidf = termFrequency(word,doc)*inverseDocumentFrequency(word)
		docVector.append(tfidf)

	return docVector
# subtract it by 1
def euclideanDistance(doc1, doc2):
	d1 = vectorizeDocument(doc1)
	d2 = vectorizeDocument(doc2)

	total = 0
	for i in range(0,len(d1)):
		total = total + math.pow((d1[i]-d2[i]),2)

	return math.sqrt(total)

def clusterCost(c1,c2):
	maximum = float('inf');

	for doc1 in c1:
		for doc2 in c2:
			cst = euclideanDistance(doc1,doc2)
			if cst < maximum:
				maximum = cst

	return maximum;

def singleLinkCluster(k):

	clusters = {}

	for doc in collection.keys():
		clusters[doc] = [doc]

	bestA = None
	bestB = None
	bestCost = None
	while len(clusters) > k:

		maximum = float('inf');
		for c1 in clusters.keys():
			for c2 in clusters.keys():
				if c1 == c2:
					continue
				else:
					mergeCost = clusterCost(clusters[c1],clusters[c2])
					# print mergeCost,c1,c2 # important
					if mergeCost < maximum:
						maximum = mergeCost
						bestA = c1;
						bestB = c2;
					#print maximum

		for doc in clusters[bestB]:
			clusters[bestA].append(doc)

		del clusters[bestB]
		bestCost = maximum

	print clusters,maximum

if __name__ == '__main__':
	buildVocabulary()
	#print clusterCost(['1'],['2'])
	print "cluster for 4"
	singleLinkCluster(4)
	print "cluster for 3"
	singleLinkCluster(3)
	print "cluster for 2"
	singleLinkCluster(2)
	print "cluster for 1"
	singleLinkCluster(1)