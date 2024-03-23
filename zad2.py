import os
import sys


def list_path_directories():
    path = os.getenv("PATH")
    if path:
        directories = path.split(os.pathsep)
        for directory in directories:
            print(directory)


def list_executables_in_path():
    path = os.getenv("PATH")

    if path:
        directories = path.split(os.pathsep)
        for directory in directories:
            print(f"Directory: {directory}")
            try:
                files = os.listdir(directory)
                for file in files:
                    print(f"\t{file}")
            except OSError:
                pass


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "-d":
            # Wypisz tylko katalogi ze zmiennej PATH
            list_path_directories()
        elif sys.argv[1] == "-e":
            # Wypisz pliki wykonywalne w katalogach ze zmiennej PATH
            list_executables_in_path()
        else:
            print("Niepoprawny argument. Użycie: python nazwa_skryptu.py [-d | -e]")
    else:
        print("Użycie: python nazwa_skryptu.py [-d | -e]")
