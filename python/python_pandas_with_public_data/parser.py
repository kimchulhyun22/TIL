import pandas as pd
import os

from db import *


CSV_FILE_PATH = os.path.dirname(__file__) + '/csv'
file_list = os.listdir(CSV_FILE_PATH)

KEYWORD = [
    ('노래방', 1),
    ('인터넷PC방', 2),
    ('실내골프연습장', 3),
    ('당구장', 4),
    ('커피전문점/카페/다방', 6),
]

for file in file_list:
    csv_data = pd.read_csv(CSV_FILE_PATH + '/' + file, low_memory=False)

    for word, category_id in KEYWORD:
        query_data = csv_data.query(f"상권업종소분류명 == '{word}'")

        for index, row in query_data.iterrows():
            try:
                if find_store_by_name(row['상호명']):
                    continue

                save_store(name=row['상호명'], x=float(row['경도']), y=float(row['위도']), category_id=category_id)
            except Exception as e:
                print(e)
                print(index, row)
                continue