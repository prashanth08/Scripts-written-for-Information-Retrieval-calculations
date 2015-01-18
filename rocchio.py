import math;

collection = {
	"Document1":"computer science theory computing algorithm",
	"Document2":"programming computing algorithm",
	"Document3":"computing information computing machine",
	"Document4":"machine learning theory learning computing science",
	"Document5":"efficient computing algorithm efficient",
	"Document6":"problem greedy algorithm greedy"
}

RelevantCollection = {
	"Document1":"computer science theory computing algorithm",
	"Document2":"programming computing algorithm",
	"Document4":"machine learning theory learning computing science"

}

vocabulary = [];

def buildVocabulary():
	for key in collection.keys():
		document = collection[key].split(' ');

		for word in document:
			if word not in vocabulary:
				vocabulary.append(word);

def termFrequency(term,document):
	document = document.split(' ');
	count = 0;
	for word in document:
		if word == term:
			count = count + 1;

	return count;

def inverseDocFrequency(term):
	count = 0;
	for key in collection.keys():
		document = collection[key].split(' ');

		if term in document:
			count = count + 1;

	if count == 0:
		return 0;
	else:
		return math.log(len(collection)/float(count))

def vectorizeDocument(document):

	vector = [];
	for word in vocabulary:
		tf = termFrequency(word,document);
		idf = inverseDocFrequency(word);

		temp = tf*idf;
		vector.append(temp);

	return vector;

def documentTermWeight(term, document):

	f = termFrequency(term,document);
	idf = inverseDocFrequency(term);

	d = 0; num = 0; den = 0;
	if f == 0:
		num = idf;
	else:
		num = (math.log(f)+1)*idf;

	total = 0;

	print document,f, idf;

	for word in document.split(' '):
		tf = termFrequency(word,document);
		idf1 = inverseDocFrequency(word);

		if tf == 0:
			total = total + idf**2;
		else:
			total = total + ((math.log(tf)+1)*idf1)**2;

	print total;

	den = math.sqrt(total);

	d = num/den;

	return d;

def main():

	query = "programming computing algorithm";

	buildVocabulary();
	print vocabulary;

	queryVector = vectorizeDocument(query);

	newQuery = []
	for i in range(0,len(queryVector)):
		word = vocabulary[i];
		print word;

		dt = 0;

		for key in RelevantCollection.keys():

			document = RelevantCollection[key];

			#dt = dt + documentTermWeight(word, document);
			dt = dt + (termFrequency(word,document)*inverseDocFrequency(word))

		q = 4*queryVector[i] + 4*dt;

		newQuery.append(q);

	print "Query Vector";
	print queryVector;

	print "New Query"
	print newQuery;

	rank(newQuery);

def test():
	word = "computer"
	document = collection["Document1"];

	print "tf:",termFrequency(word, document);
	print "idf:",inverseDocFrequency(word);

	print documentTermWeight(word,document);

def rank(query):

	for key in collection.keys():
		document = vectorizeDocument(collection[key]);

		total = 0;
		for i in range(0,len(query)):
			total = total + (document[i]*query[i])

		print key, total;

def displayTfidf():

	print vocabulary;
	print vectorizeDocument("programming computing algorithm");

	for key in collection.keys():
		print vectorizeDocument(collection[key]);

if __name__ == '__main__':
	main()
	#test()
	displayTfidf()
