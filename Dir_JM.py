collection = {
	"Document1":"cornell students enjoyed the halloween in the past weekend",
	"Document2":"cornell students from across campus attended the state of the university delivered by president david skorton",
	"Document3":"a three alarm fire affected dozens of dormitory residing students on friday",
	"Document4":"students from cornell university are celebrating the end of the semester",
	"Document5":"cornell may be a good fit for people who likes to swim in the lakes"
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

	queries = ["cornell","students", "cornell students"];

	for key in collection.keys():

		document = collection[key];

		for query in queries:

			queryWordList = query.split(' ');

			prob = 1;
			for term in queryWordList:

				p = probablity(term, document);
				prob = prob * p;

			print key, query, prob;

def mercerSmoothing():

	queries = ["cornell","students", "cornell students"];

	for key in collection.keys():

		document = collection[key];

		for query in queries:

			queryWordList = query.split(' ');

			prob = 1;
			for term in queryWordList:

				p = JMprobablity(term, document);
				prob = prob * p;

			print key, query, prob;


if __name__ == '__main__':
	print "Dirichlet Smoothing";
	dirichletSmoothing()
	print "JM Smoothing";
	mercerSmoothing()

	





