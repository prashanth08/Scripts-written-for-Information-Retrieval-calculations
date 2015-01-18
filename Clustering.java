import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;

public class Clustering {

	static Double docCount = Driver.docCount;
	//Only the terms pertaining to particular document
	static LinkedHashMap<String, LinkedHashMap<String,Double>>docColl = new LinkedHashMap<String, LinkedHashMap<String,Double>>(Driver.docColl);
	//All the terms in the document
	static LinkedHashMap<String, LinkedHashMap<String,Double>>docCollFull = new LinkedHashMap<String, LinkedHashMap<String,Double>>(UpdateDocVectors.docCollFull);
	//List of all unique terms
	static ArrayList<String> uniqueTerms = new ArrayList<String>(Driver.uniqueTerms);
	static HashMap<String,Double> docFrequency = new HashMap<String,Double>(Driver.docFrequency);


	//Number of final clusters
	static Double kValue = 1.0;
	static LinkedHashMap<String, ArrayList<String>> initialClusters = new LinkedHashMap<String, ArrayList<String>>();
	static linkageType linkType = linkageType.SINGLE; 


	public static void getInitialClusters() {

		int i = 1;
		for ( String key : docCollFull.keySet() )
		{
			ArrayList<String> cluster = new ArrayList<String>();
			cluster.add(key);
			initialClusters.put("Cluster"+ String.valueOf(i), cluster);
			i++;
		}		
	}

	public static void clusterLogic() { 

		System.out.println("******************************************************");
		System.out.println("Clustering");
		//Loop till K clusters
		Double loopClusters = docCount;
		while(loopClusters > kValue )
		{
			String candidateA = null, candidateB = null; 
			double maxSim = 0.0, simAB = 0.0; 

			for(String keyA: initialClusters.keySet()){
				for(String keyB: initialClusters.keySet()){				
					if (keyA != keyB){
						//Find the least similar documents between clusters
						simAB = findMaxSimbetweenClusters(keyA,keyB);
						//See if the similarity of the above clusters is the minimum
						if (simAB > maxSim){
							candidateA = keyA;
							candidateB = keyB;
							maxSim = simAB;
						}
					}
				}
			}
			//Combine the clusters from the complete linkage
			ArrayList<String> clusterA = initialClusters.get(candidateA);
			ArrayList<String> clusterB = initialClusters.get(candidateB);
			for ( String doc: clusterB){
				clusterA.add(doc);
			}
			loopClusters--;
			clusterB = null;
			initialClusters.put(candidateA,clusterA);
			initialClusters.put(candidateB, null);
			
			
			for (String cluster: initialClusters.keySet()) {
				System.out.println(cluster + " : " + initialClusters.get(cluster) );
			}			
			System.out.println();
		}
		System.out.println("******************************************************");
	}

	public static double findMaxSimbetweenClusters(String keyA, String keyB) {
		double maxSim = 0.0, simAB = 0.0;
		if ( linkType == linkageType.COMPLETE ) 
			maxSim = Double.MAX_VALUE;
		ArrayList<String> clusterA = initialClusters.get(keyA);
		ArrayList<String> clusterB = initialClusters.get(keyB);
		if (clusterA != null && clusterB != null ){
			for( String docA : clusterA){
				for (String docB : clusterB ){
					simAB = calculateSimilarity(docA,docB);
					if (linkType == linkageType.COMPLETE) {
						if (simAB < maxSim)
							maxSim = simAB;
					}
					else if (linkType == linkageType.SINGLE) {
						if (simAB > maxSim)
							maxSim = simAB;
					}

				}
			}
		}
		if ( linkType == linkageType.COMPLETE && maxSim == Double.MAX_VALUE )
			return 0.0;
		return maxSim;
	}

	private static Double calculateSimilarity(String doc1, String doc2) {

		double simScore = 0.0;
		HashMap<String, Double> doc1Vector = docCollFull.get(doc1);
		HashMap<String, Double> doc2Vector = docCollFull.get(doc2);

		for (String term : doc1Vector.keySet()){
			if ( doc2Vector.containsKey(term)){  
				simScore += doc1Vector.get(term) * doc2Vector.get(term); 
			}
		}
		return (simScore);		
	}
	
	public static void clusterDriver()
	{
		getInitialClusters();
		clusterLogic();
	}

	enum linkageType{
		COMPLETE,
		SINGLE
	}

}