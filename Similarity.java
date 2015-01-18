import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;

public class Similarity {

	static Double docCount = Driver.docCount;
	//Only the terms pertaining to particular document
	static LinkedHashMap<String, LinkedHashMap<String,Double>>docColl = new LinkedHashMap<String, LinkedHashMap<String,Double>>(Driver.docColl);
	//All the terms in the document
	static LinkedHashMap<String, LinkedHashMap<String,Double>>docCollFull = new LinkedHashMap<String, LinkedHashMap<String,Double>>(UpdateDocVectors.docCollFull);
	//List of all unique terms
	static ArrayList<String> uniqueTerms = new ArrayList<String>(Driver.uniqueTerms);
	static HashMap<String,Double> docFrequency = new HashMap<String,Double>(Driver.docFrequency);

	public static void calcSimilarity() {
		System.out.println("******************************************************");
		System.out.println("Similairty Scores");
		for ( String doc : docCollFull.keySet())
			System.out.print("    "+doc);
		System.out.println();
		for ( String doc1 : docCollFull.keySet()) {
			StringBuffer docSimiScores = new StringBuffer(doc1);
			for ( String doc2 : docCollFull.keySet()) {
				docSimiScores.append("  "+similarityOfDoc1Doc2(doc1,doc2));
			}
			System.out.println(docSimiScores);
		}
		System.out.println("******************************************************");		
	}

	public static String similarityOfDoc1Doc2(String doc1, String doc2) {
		Double simiScore = 0.0;
		for ( String term: docCollFull.get(doc1).keySet()) {
			simiScore = simiScore + (docCollFull.get(doc1).get(term) * 
					docCollFull.get(doc2).get(term));
		}
		return simiScore.toString();
	}

	static void printDocVectors(LinkedHashMap<String, LinkedHashMap<String, Double>> docCollVectors)
	{
		System.out.println("*******************************************************");
		System.out.println("Updated Document Vectors");	
		for (String doc : docCollVectors.keySet()) {
			System.out.print(doc + ":: ");
			for ( String term : docCollVectors.get(doc).keySet()) {
				System.out.print(term+":"+docCollVectors.get(doc).get(term) + " ");
			}
			System.out.println();
		}
		System.out.println("******************************************************");
	}

	public static void similarityDriver () {
		printDocVectors(docCollFull);
		calcSimilarity();
	}

}