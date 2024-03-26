import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.io.*;
import com.google.gson.Gson;

public class Analyzer {

    public static void main(String[] args) throws FileNotFoundException {
        if (args.length != 1) {
            System.out.println("Nieprwaidlowa liczba argumentow");
            return;
        }
        String path = args[0];
        analyze(path);

    }

    private static void analyze(String path) throws FileNotFoundException{
        try(BufferedReader reader = new BufferedReader(new FileReader(path))) {
            int characterCount = 0;
            int wordsCount = 0;
            int linesCount = 0;
            char mostCommonCharacter;
            String mostCommonWord;

            HashMap<Character, Integer> charFreq = new HashMap<>();
            HashMap<String, Integer> wordFreq = new HashMap<>();

            String line;

            while ((line= reader.readLine())!=null){
                linesCount++;
                characterCount = characterCount+line.length();
                wordsCount = wordsCount + line.split("\\s+").length;

                for(char c: line.toCharArray()){
                    charFreq.put(c,charFreq.getOrDefault(c,0)+1);
                }
                for(String word: line.split("\\s+")){
                    wordFreq.put(word,wordFreq.getOrDefault(word,0)+1);
                }
            }
            mostCommonCharacter = Collections.max(charFreq.entrySet(), Map.Entry.comparingByValue()).getKey();
            mostCommonWord = Collections.max(wordFreq.entrySet(), Map.Entry.comparingByValue()).getKey();

            HashMap<String,Object> results = new HashMap<>();

            results.put("path",path);
            results.put("number_of_characters", characterCount);
            results.put("number_of_words", wordsCount);
            results.put("number_of_lines", linesCount);
            results.put("most_common_character", mostCommonCharacter);
            results.put("most_common_word", mostCommonWord);
            results.put("character_frequency", charFreq.get(mostCommonCharacter));
            results.put("word_frequency", wordFreq.get(mostCommonWord));

            Gson gson = new Gson();
            String jsonOutput = gson.toJson(results);
            System.out.println(jsonOutput);




        }
        catch (IOException e){
            throw new FileNotFoundException("Nieprawidlowa sciezka do pliku");
        }
    }

}
