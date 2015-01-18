import math

collection = {
	'1':"cornell cayuga bigred bears",
	'2':"cornell cornell nyc bigred bigred",
	'3':"cornell bells ring everyday",
	'4':"cornell cornell cold ring ring",
	'5':"bigred bigred bells ring everyday very cool"
}

rcollection = {
	'4':"cornell cornell cold ring ring",
	'2':"cornell cornell nyc bigred bigred",
	'5':"bigred bigred bells ring everyday very cool"
}

def termFrequency(word, doc):
	count = 0
	document = doc.strip().split(' ')
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

	return count

def avgLength():
	count = 0
	for doc in collection.keys():
		count = count + len(collection[doc].strip().split(' '))

	return count/float(len(collection))

def getK(k1,dl,avgdl,b):
	return k1*((1-b)+b*(dl/avgdl))

def inverseDocumentFrequencyRelevant(word):
	count = 0;
	for doc in rcollection.keys():
		document = rcollection[doc].strip().split(' ')
		if word in document:
			count = count + 1

	return count

def bm25Score(qry,k1,k2,b,doc,avgdl):

	document = collection[doc].strip().split(' ')
	query = qry.strip().split();
	#print query
	total = 0

	K = getK(k1,len(document),avgdl,b)
	for word in query:
		fi = termFrequency(word,collection[doc])
		ni = inverseDocumentFrequency(word)
		qfi = termFrequency(word, qry)
		ri = inverseDocumentFrequencyRelevant(word)

		p1 = math.log(((ri+0.5)/(len(rcollection)-ri+0.5))/((ni-ri+0.5)/(len(collection)-ni-len(rcollection)+ri+0.5)))
		p2 = ((k1+1)*fi)/float(K+fi)
		p3 = ((k2+1)*qfi)/float(k2+qfi)

		total = total + (p1*p2*p3)

	return total

def main():

	query = "cornell cayuga bigred"
	k1=1.2
	k2=100
	b=0.75
	avgdl = avgLength()

	docScores = []

	for doc in collection.keys():
		docScores.append((bm25Score(query,k1,k2,b,doc,avgdl),doc))

	docScores.sort()
	docScores.reverse()
	print docScores

if __name__ == '__main__':
	main()