import math;
import numpy as np;
#precision at k
result = ['R1','X','X','R2','X','R3','X','R4','R5','X']
nonrel = ['X']

rlist = [3, 0, 0, 2, 0, 1, 0, 1, 1, 0]

def precisionAtK():
	precision = []
	avgPrecision = 0;
	docCount = 0;
	relCount = 0;
	for doc in result:
		docCount = docCount + 1;
		if doc not in nonrel:
			relCount = relCount + 1;
			avgPrecision = avgPrecision + relCount/float(docCount)

		precision.append(relCount/float(docCount));

	print "Average Precision",avgPrecision/float(relCount)
	print precision

def DCG(rel):
	docCount = 0;
	dcgScores = [];

	for doc in rel:
		docCount = docCount + 1;
		if docCount == 1:
			dcgScores.append(rel[docCount-1])
		else:
			score = dcgScores[-1] + rel[docCount-1]/math.log(docCount,2)
			dcgScores.append(score)

	print "DCG Scores"
	print dcgScores; 
	return dcgScores;

def NDCG(rel):
	s1 = DCG(rlist)
	nlist = sorted(rlist);
	nlist.reverse()
	s2 = DCG(nlist)

	result = []
	for i in range(0,len(s1)):
		result.append(s1[i]/s2[i])

	print "NDCG Scores"
	print result;

def pageRank(l,N,L,R):
	T = l/N + np.dot((1-l),L);
	return np.dot(T,R);

def runPageRank(l,N,L,R,k):
	for i in range(0,k):
		R = pageRank(l,N,L,R)
		print ("iteration",i)
		print (R);

if __name__ == '__main__':
	precisionAtK()
	NDCG(rlist)
	L = [[1/2.,1/3.,0,0],[1/2.,0,0,0],[0,1/3.,0,0],
		[0,1/3.,1,0]]
	R = [[0.25],[0.25],[0.25],[0.25]]
	runPageRank(0.1,4,L,R,2)

