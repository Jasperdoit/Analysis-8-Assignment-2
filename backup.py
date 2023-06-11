import os.path
import shutil
import zipfile
import glob
from datetime import datetime

DATABASE_NAME = 'fitplus.db'
ZIP_TEMP_NAME = 'temp.zip'
LOGS_FOLDER_NAME ='./logs'


class Backup:

    @staticmethod
    def get_current_date() -> str:
        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def get_path(count: int) -> str:
        return f'./backup/Backup-FitPlus-{Backup.get_current_date()}-{count}.zip'

    @staticmethod
    def zip_dir(path, zip_object):
        for root, dirs, files in os.walk(path):
            for file in files:
                zip_object.write(os.path.join(root, file),
                                 os.path.relpath(os.path.join(root, file),
                                                 os.path.join(path, '..')))

    @staticmethod
    def create_backup():
        count = 1
        while True:
            if not os.path.exists(Backup.get_path(count)):
                break
            count += 1
        try:
            with zipfile.ZipFile(ZIP_TEMP_NAME, 'w', zipfile.ZIP_DEFLATED) as zip_object:
                Backup.zip_dir(zip_object)
                zip_object.write(DATABASE_NAME)
        except Exception as e:
            return print(e)
        shutil.move('./temp.zip', './backup')
        os.rename('./backup/temp.zip', Backup.get_path(count))

    @staticmethod
    def get_latest_backup() -> str:
        try:
            list_of_files = glob.glob('./backup/*.zip')
            latest_file = max(list_of_files, key=os.path.getctime)
        except ValueError:
            print("[!] Backup folder was empty, no backups restored.")
            return ""

        return latest_file

    @staticmethod
    def restore_backup():
        latest_backup = Backup.get_latest_backup()
        if not len(latest_backup) > 0:
            return

        Backup.create_backup()
        with zipfile.ZipFile(latest_backup, 'r', zipfile.ZIP_DEFLATED) as zip_object:
            zipfile.ZipFile.extractall(zip_object, '.')