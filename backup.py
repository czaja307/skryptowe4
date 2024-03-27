import csv
import os.path
import shutil
import subprocess
import sys
import time


def create_backup(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    dirname = os.path.basename(directory)
    ext = ".zip"
    backup_filename = f"{timestamp}-{dirname}{ext}"

    subprocess.run(["zip", "-r", backup_filename, directory])

    backup_dir = os.getenv("BACKUPS_DIR", os.path.join(os.path.expanduser("~"), ".backups"))

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_path = os.path.join(backup_dir, backup_filename)
    shutil.move(backup_filename, backup_path)

    history_file = os.path.join(backup_dir, "backup_history.csv")
    backup_record = {"date": timestamp, "directory": directory, "backup_filename": backup_filename}
    write_to_history(history_file, backup_record)


def write_to_history(history_file, record):
    fieldnames = ["date", "directory", "backup_filename"]
    file_exists = os.path.exists(history_file)

    with open(history_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(record)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        create_backup(sys.argv[1])
    else:
        print("Użycie: python backup.py [path]")
