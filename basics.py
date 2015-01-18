#ngram genarator - term doc index - tf - inverse doc
collection = {
'doc1':"pretty kitty creighton had a cotton batten pretty cat",
'doc2':"the cotton batten cat was bitten by a rat",
'doc3':"the kitten that was bitten had a button for an eye",
'doc4':"and biting off the button made the cotton batten fly"
}

def ngramGenerator(n):
    ngramList = {}
    for doc in collection.keys():
        document = collection[doc].strip().split(' ');
        for i in range(0,len(document)):
            gram = " ".join(document[i:i+n])
            if len(gram) < n:
            	continue;
            else:
            	ngramList[gram] = ngramList.get(gram,0) + 1;

    print ngramList;

def termDocumentIndex():
	index = {}
	for doc in collection.keys():
		document = collection[doc].strip().split(' ');
		for term in document:
			index[term] = index.get(term, '') + " " + doc

	print index;

def termFrequency(term, doc):
	document = doc.strip().split(' ')
	count = 0;

	for word in document:
		if word == term:
			count = count + 1

	return count

def inverseDocumentFrequency(term):
	
	count = 0;
	for doc in collection.keys():
		document = collection[doc].strip().split(' ')
		if term in document:
			count = count + 1

	return count;


if __name__ == '__main__':
	ngramGenerator(2)
	termDocumentIndex()
	print termFrequency('pretty',collection['doc1'])
	print inverseDocumentFrequency('batten')
