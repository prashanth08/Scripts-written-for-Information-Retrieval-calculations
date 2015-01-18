import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;

public class Driver {
	final static String inputFile = "Input/inputCollection.txt";
	final static Charset ENCODING = Charset.forName("UTF-8");
	static Double docCount = 0.0;
	//Only the terms pertaining to particular document
	static LinkedHashMap<String, LinkedHashMap<String,Double>>docColl = new LinkedHashMap<String, LinkedHashMap<String,Double>>();
	//All the terms in the document
	static LinkedHashMap<String, LinkedHashMap<String,Double>>docCollFull = new LinkedHashMap<String, LinkedHashMap<String,Double>>();
	//List of all unique terms
	static ArrayList<String> uniqueTerms = new ArrayList<String>();
	//Document Frequency 
	static HashMap<String,Double> docFrequency = new HashMap<String,Double>();

	static void fillDocColl(String line)
	{
		String []docTerms = line.split(" ");
		LinkedHashMap<String,Double> innerMap = new LinkedHashMap<String,Double>();
		for (String term : docTerms) {
			//Put the terms and the frequency in the Hashmap
			if(!innerMap.containsKey(term)) {
				innerMap.put(term,1.0);
			} else {
				Double termCount = innerMap.get(term);
				innerMap.put(term,termCount+1.0);
			}
			//Update list of unique terms
			if (!uniqueTerms.contains(term))
				uniqueTerms.add(term);
		}
		docCount++;
		docColl.put("d"+docCount.toString(), innerMap);
	}

	static void fillDocCollFull()
	{
		for (String doc : docColl.keySet()) {
			LinkedHashMap<String,Double> innerMap = new LinkedHashMap<String,Double>(docColl.get(doc));
			for (String term: uniqueTerms ) {
				if(!innerMap.containsKey(term))
					innerMap.put(term, 0.0);
			}
			docCollFull.put(doc, innerMap);		
		}
	}

	static void printDocVectors(LinkedHashMap<String, LinkedHashMap<String, Double>> docCollVectors)
	{
		System.out.println("*******************************************************");
		System.out.println("Initial Document Vectors");	
		for (String doc : docCollVectors.keySet()) {
			System.out.print(doc + ":: ");
			for ( String term : docCollVectors.get(doc).keySet()) {
				System.out.print(term+":"+docCollVectors.get(doc).get(term) + " ");
			}
			System.out.println();
		}
		System.out.println("******************************************************");
	}

	static void readInputFile() throws IOException {
		Path path = Paths.get(inputFile);
		try (BufferedReader reader = Files.newBufferedReader(path, ENCODING)) {
			String line = null;
			while ((line = reader.readLine()) != null) {
				fillDocColl(line);
			}     
		}
	}

	public static void calcDocFrequency() {
		for ( String term: uniqueTerms) {
			for ( String doc: docColl.keySet() ) {
				if ( docColl.get(doc).containsKey(term)) {
				if(!docFrequency.containsKey(term))
					docFrequency.put(term, 1.0);
				else
					docFrequency.put(term, docFrequency.get(term) + 1.0);
				}
			}
		}
	}


	public static void main(String []args) throws IOException
	{
		readInputFile();
		fillDocCollFull();
		calcDocFrequency();
		System.out.println("Number of documents = " + docCount);
		System.out.println("Number of unique terms = " + uniqueTerms.size());
		printDocVectors(docCollFull);
		UpdateDocVectors.updateDriver();
		Similarity.similarityDriver();
	//	Clustering.clusterDriver();
	}
}