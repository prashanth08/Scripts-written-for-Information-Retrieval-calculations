import math;

collection = {
	"Document1":"one and one make two",
	"Document2":"one and two make three",
	"Document3":"two and three make five",
	"Document4":"three and five make eight",
	"Document5":"one and three make what two and two make"
}

RelevantCollection = {
	"Document1":"one and one make two",
	"Document2":"one and two make three",
	"Document5":"one and three make what two and two make"
}

vocabulary = [];

def buildVocabulary():
	for key in collection.keys():
		document = collection[key].split(' ');
		for word in document:
			if word not in vocabulary:
				vocabulary.append(word);

def fqD(term, document):
	count = 0;

	document = document.split(' ');
	for word in document:
		if word == term:
			count = count + 1;

	return (count, len(document));

def countTermInCollection(term):
	count = 0;

	for key in collection.keys():
		document = collection[key].split(' ');

		for word in document:
			if word == term:
				count = count + 1;

	return count;


def countWordCollection():
	count = 0;

	for key in collection.keys():
		count = count + len(collection[key].split(' '));

	return count;

def countTermInRelevantCollection(term):
	count = 0;

	for key in RelevantCollection.keys():
		document = RelevantCollection[key].split(' ');

		for word in document:
			if word == term:
				count = count + 1;

	return count;

def countWordRelevantCollection():
	count = 0;

	for key in RelevantCollection.keys():
		count = count + len(RelevantCollection[key].split(' '));

	return count;


def probablityQD(queryTerm, document):

	(f, D) = fqD(queryTerm, document);
	c = countTermInCollection(queryTerm);
	C = countWordCollection();

	return (f + (0.1)*(c/float(C)))/(0.1 + D);

def probD():
	return 1/float(3) ;

def probWD(word, document):
	
	(f, D) = fqD(word, document);
	c = countTermInRelevantCollection(word);
	C = countWordRelevantCollection();

	return (f + (0.1)*(c/float(C)))/(0.1 + D);

def partProbWQ(query,document,word):

	#print document;
	prob = 1;
	for term in query:
		#print "pQD", probablityQD(term, document);
		#print "Document in part prob", document;
		temp = probWD(term, document);
		print "prob q",term,temp;
		prob = prob * temp;


	prob = prob * probD() * probWD(word, document);

	print word,probWD(word, document);

	#print "prob of WD", probWD(word, document);
	#print "Prob of D", probD();

	return prob;


def jointProbablity(word, query):

	total = 0;
	for key in RelevantCollection.keys():

		print key;
		document = RelevantCollection[key];
		#print document;
		total = total + partProbWQ(query, document, word);
		#print "part prob", partProbWQ(query, word, document);

	#print total;
	return total;

def KLDivergence(langModel, probQ):

	for key in collection.keys():
		document = collection[key];

		temp1 = 0;
		temp2 = 0;

		for word in vocabulary:

			temp = probablityQD(word, document)
			if temp != float(0):
				temp = math.log(temp);
	

			temp1 = temp1 + ((langModel[word]/probQ)*temp);
			tmp = langModel[word]
			if tmp == float(0):
				temp2 = temp2 + 0;
			else:
				temp2 = temp2 + ((langModel[word]/probQ)*math.log(langModel[word]/probQ));

		print key, temp1, (temp1 - temp2)

def main():

	buildVocabulary();

	print vocabulary;

	query = ["one","one","two"];

	langModel = {};

	for word in vocabulary:

		temp = jointProbablity(word, query);
		#print word, temp;
		langModel[word] = temp;
		
	probQ = 0;

	for key in langModel.keys():
		probQ = probQ + langModel[key];

	for key in langModel.keys():
		print key, langModel[key], langModel[key]/probQ;


	print "KL Divergence"
	KLDivergence(langModel,probQ)

def test():

	buildVocabulary();
	for word in vocabulary:

		vector = [];
		for key in RelevantCollection.keys():
			document = RelevantCollection[key];

			vector.append(probWD(word,document));

		print word, vector;



if __name__ == '__main__':
	main()
	#test()



	