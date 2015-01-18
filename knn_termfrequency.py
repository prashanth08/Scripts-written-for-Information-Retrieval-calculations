import math
from scipy.stats import mode

#TODO input
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
	document = doc.strip().split(' ')#collection[doc].strip().split(' ')
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
		print "doc--> ", doc,":: word :: ", word,  ":: term frequency:: ", termFrequency(word,doc), ":: inverse Document Frequency:: ",inverseDocumentFrequency(word)
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

def kNearestNeighbor(k):

# TODO input documents and interger nos
	clusters = [('1',1),('2',1),('3',3),('4',3),('5',5)]
#copy paste the calculation
	testDocument = "cornell cornell cornell bears bears nyc cayuga cool";

	votes = []

	for (docId, cId) in clusters:
		cost = euclideanDistance(collection[docId], testDocument)
		votes.append((cost,cId))

	print votes
	votes.sort();
	print "sorted clusters : cost,clusterid"
	print votes
	kvotes = votes[:k]
	print "Top ", k, " cluster(s)"
	print kvotes
	clist = []
	for (cost, i) in kvotes:
		clist.append(i)

	cluster = mode(clist)[0];

	print "closest cluster:",cluster

if __name__ == '__main__':
	buildVocabulary()
	kNearestNeighbor(3)


