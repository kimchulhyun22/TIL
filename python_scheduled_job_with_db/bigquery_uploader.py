import glob
import os

from typing import List
from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime, date
from dotenv import load_dotenv

load_dotenv()


class BigQueryUploader:
    def __init__(self) -> None:
        key_path = glob.glob("./*.json")[0]

        self._credentials = service_account.Credentials.from_service_account_file(
            key_path
        )
        self._big_query_client = bigquery.Client(
            credentials=self._credentials, project=self._credentials.project_id
        )

    def upload_bigquery_table(self, table_name: str, data: List):
        try:
            table = self._big_query_client.get_table(table_name)
            errors = self._big_query_client.insert_rows_json(
                table,
                data,
            )

            if errors:
                raise Exception(f"BigQuery Upload Error {errors}")

        except Exception as e:
            print(e)


bigquery_uploader = BigQueryUploader()


def main():
    test_data = [
        {
            "id": f"test_{datetime.now()}",
            "number": 1,
            "created_at": str(datetime.now()),
        },
        {
            "id": f"test_{datetime.now()}",
            "number": 2,
            "created_at": str(datetime.now()),
        },
        {
            "id": f"test_{datetime.now()}",
            "number": 3,
            "created_at": str(datetime.now()),
        },
    ]

    bigquery_uploader.upload_bigquery_table(
        table_name=os.getenv("BIGQUERY_TABLE_NAME"),
        data=test_data,
    )


if __name__ == "__main__":
    main()
