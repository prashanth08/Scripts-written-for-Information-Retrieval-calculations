import math;

collection = {
	"Document1":"one and one make two",
	"Document2":"one and two make three",
	"Document3":"two and three make five",
	"Document4":"three and five make eight",
	"Document5":"one and three make what two and two make"
}

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

def probablity(queryTerm, document):

	(f, D) = fqD(queryTerm, document);
	c = countTermInCollection(queryTerm);
	C = countWordCollection();

	return (f + (0.1)*(c/float(C)))/(0.1 + D);

def JMprobablity(queryTerm, document):

	(f, D) = fqD(queryTerm, document);
	c = countTermInCollection(queryTerm);
	C = countWordCollection(); 

	return ((1 - 0.1)*f)/float(D) + ((0.1)*c)/float(C);


def dirichletSmoothing():

	queries = ["one one two"];

	for key in collection.keys():

		document = collection[key];

		for query in queries:

			queryWordList = query.split(' ');

			prob = 1; plog = 0;
			for term in queryWordList:

				p = probablity(term, document);
				print term, p;
				prob = prob * p;
				plog = plog + math.log(p);

			print key, query, prob, plog;

if __name__ == '__main__':
	print "Dirichlet Smoothing";
	dirichletSmoothing();

	





