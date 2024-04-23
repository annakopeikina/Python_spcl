import os
import datetime

def find_files_by_creation_date(root_directory, start_timestamp, end_timestamp):
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            creation_time = os.path.getctime(file_path)
            if start_timestamp <= creation_time <= end_timestamp:
                print("Найден файл:", file_path)

if __name__ == "__main__":
    root_directory = "C:\\"  
    today = datetime.datetime.now().date()
    start_time = datetime.datetime(today.year, today.month, today.day, 9, 0)
    end_time = datetime.datetime(today.year, today.month, today.day, 11, 30)
    start_timestamp = int(start_time.timestamp())
    end_timestamp = int(end_time.timestamp())

    print(" файлы, созданные сегодня с 9:00 до 11:30...")
    find_files_by_creation_date(root_directory, start_timestamp, end_timestamp)
