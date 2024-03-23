import os
import sys


def display_environment_variables(cmd_params):
    env_vars = sorted(os.environ.items())

    if not cmd_params:
        for key, value in env_vars:
            print(f"{key}={value}")
    else:
        for key, value in env_vars:
            if key in cmd_params:
                print(f"{key}={value}")


if __name__ == "__main__":
    # Pobierz parametry z linii poleceń, pomijając nazwę skryptu
    params = sys.argv[1:]
    display_environment_variables(params)
