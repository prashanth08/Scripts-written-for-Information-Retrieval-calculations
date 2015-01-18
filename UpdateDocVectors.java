import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;

public class UpdateDocVectors {

	static final String[] weights = {"tf","df"};
	static Double docCount = Driver.docCount;
	//Only the terms pertaining to particular document
	static LinkedHashMap<String, LinkedHashMap<String,Double>>docColl = new LinkedHashMap<String, LinkedHashMap<String,Double>>(Driver.docColl);
	//All the terms in the document
	static LinkedHashMap<String, LinkedHashMap<String,Double>>docCollFull = new LinkedHashMap<String, LinkedHashMap<String,Double>>(Driver.docCollFull);
	//List of all unique terms
	static ArrayList<String> uniqueTerms = new ArrayList<String>(Driver.uniqueTerms);
	static HashMap<String,Double> docFrequency = new HashMap<String,Double>(Driver.docFrequency);

	public static Double calcNorCoefficient(String doc) {
		Double sumSquareValue = 0.0;
		for ( String term : docCollFull.get(doc).keySet()) { 
			Double termValue = docCollFull.get(doc).get(term);
			sumSquareValue += termValue * termValue  ;
		}
		return ((Double)1.0/Math.sqrt(sumSquareValue)); 
	}

	private static void updateDocVectors() {
		if (weights!= null) {
			for ( String doc : docCollFull.keySet()) {
				Double docNormCoefficient = calcNorCoefficient(doc);
				for ( String term : docCollFull.get(doc).keySet()) {
					Double termWeight = docCollFull.get(doc).get(term);
					for (String weightType : weights) { 
						switch (weightType) {
						case "tf":
							//Don't do anything
							break;
						case "df":
							termWeight *= ((Double)1.0/docFrequency.get(term));  
							break;
						case "norm":
							termWeight *= docNormCoefficient;
							break;
						}
					}
					docCollFull.get(doc).put(term,termWeight);	
				}
			}
		}
	}	

	public static void updateDriver() {
		updateDocVectors();
	}


}
