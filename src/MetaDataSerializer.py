import pandas as pd
import os
import csv
from collections import deque


class MataDataSerializer:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def check_or_create_id(self, name):
        pass

    def add_entry(self, record):
        with open(self.csv_path, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=vars(record).keys())
            writer.writerow(vars(record))

    def _add_value(self, value, column_name):
        df = pd.read_csv(self.csv_path)
        if value in df[column_name].values:
            pass
        else:
            df = df.append({column_name: value})
            df.to_csv(self.csv_path, index=False)

    @staticmethod
    def check_csv_file_existence(file_name, entry_model):
        base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/crawl_result/'
        csv_path = base_dir + file_name
        if not os.path.exists(csv_path):
            with open(csv_path, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(entry_model('', '').__dict__.keys())
        else:
            print('The CSV already_exist')
        return csv_path

    @staticmethod
    def generate_value_last_exist_row(file_name, column_index):
        with open(file_name, 'r') as csv_file:
            datareader = csv.reader(csv_file)
            next(datareader) # skip the header
            last_row = deque(datareader, maxlen=1)
        if last_row:
            return last_row.pop()[column_index]
        else:
            return 100000

