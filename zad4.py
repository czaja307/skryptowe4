import subprocess
import sys
import json


def read_file(filename):
    class_path = r"C:\Pola\WorkscapceP\SK4java\src"
    library_path = r"C:\Pola\WorkscapceP\SK4java\lib\gson-2.10.1.jar"
    java_command = ["java", "-cp", class_path + ";" + library_path, "Analyzer", filename]
    try:
        results = subprocess.run(java_command, check=True, capture_output=True, text=True)
        print(results.stdout)
        return json.loads(results.stdout)
    except subprocess.CalledProcessError as e:
        print("Błąd podczas uruchamiania skryptu Java:", e)


def analyze_output(result):
    read_files = 0
    total_number_of_characters = 0
    total_number_of_words = 0
    total_number_of_lines = 0
    char_frequency = 0
    word_frequency = 0
    most_common_character = ''
    most_common_word = ""

    read_files = len(result)

    for dictionary in result:
        total_number_of_characters += dictionary["number_of_characters"]
        total_number_of_words += dictionary["number_of_words"]
        total_number_of_lines += dictionary["number_of_lines"]
        new_character_frequency = dictionary["character_frequency"]
        if new_character_frequency > char_frequency:
            char_frequency = new_character_frequency
            most_common_character = dictionary.get("most_common_character")
        new_word_frequency = dictionary["word_frequency"]
        if new_word_frequency > word_frequency:
            word_frequency = new_word_frequency
            most_common_word = dictionary.get("most_common_word")

    print("Przecytane pilki: ", read_files)
    print("Liczba slow: ", total_number_of_words)
    print("Liczba znakow: ", total_number_of_characters)
    print("Liczba wierszy: ", total_number_of_lines)
    print("Najczesciej wystepujacy znak: ", most_common_character)
    print("Najczesciej wystepujace slowo: ", most_common_word)


if __name__ == "__main__":
    list_of_dictionaries = []
    if len(sys.argv) < 2:
        print("Niewlasciwa ilosc argumentow")
    else:
        for i, filename in enumerate(sys.argv[1:], start=1):
            list_of_dictionaries.append(read_file(filename))
        analyze_output(list_of_dictionaries)
