import csv
import os.path
import shutil
import subprocess
import sys
from datetime import datetime


def restore(path):
    if not os.path.exists(path):
        print("Ścieżka nie istnieje")
        return
    os.chdir(path)
    saved_backups = os.path.join(path, "backup_history.csv")
    if os.path.exists(saved_backups):
        with open(saved_backups, "r", newline='') as file:
            reader = csv.DictReader(file)
            backups = sorted(list(reader), key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'),
                             reverse=True)
            if len(backups) == 0:
                print("Brak utworzonych kopii zapasowych")
                return
            print("Otworzone kopie zapasowe:")
            for i, backup in enumerate(backups):
                print(f"{i + 1}, {backup['date']} - {backup['directory']}")
            try:
                choice = int(input("Prosze wybrac kopie do odtworzenia"))
                if choice < 1 or choice > len(backups):
                    print("Nieprawidlowy wybor")
                    return
            except TypeError:
                print("Nieprawidlowy typ")
                return
            backup_to_restore = backups[choice - 1]
            print(backup_to_restore)

            backup_path = os.path.join(path, backup_to_restore['filename'])
            shutil.rmtree(backup_path)

            if backup_path.endswith(".zip"):
                subprocess.run(['unzip', backup_path])
            elif backup_path.endswith(".tar.gz"):
                subprocess.run(['tar', 'xyf', backup_path])


if __name__ == "__main__":
    backup_dir = os.getenv("BACKUP_DIR", os.path.join(os.getcwd(), "backups"))
    if len(sys.argv) > 1:
        restore(sys.argv[1])
    else:
        restore(backup_dir)
