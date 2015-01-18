import math

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
	d1 = vectorizeDocument(doc1)
	d2 = vectorizeDocument(doc2)

	total = 0
	for i in range(0,len(d1)):
		total = total + math.pow((d1[i]-d2[i]),2)

	return math.sqrt(total)

def clusterCost(c1,c2):
	avgCost = 0;

	for doc1 in c1:
		for doc2 in c2:
			cst = euclideanDistance(doc1,doc2)
			avgCost = avgCost + cst;

	avgCost = avgCost / (len(c1)*len(c2));
	return avgCost;

def avgLinkCluster(k):

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
					print mergeCost,c1,c2
					if mergeCost < maximum:
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
	#print clusterCost(['1'],['2'])
	print "cluster for 4"
	avgLinkCluster(4)
	print "cluster for 3"
	avgLinkCluster(3)
	print "cluster for 2"
	avgLinkCluster(2)
	print "cluster for 1"
	avgLinkCluster(1)