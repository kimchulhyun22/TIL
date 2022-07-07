from scheduler import scheduler
from database import database
from bigquery_uploader import bigquery_uploader

import os
import time


def test():

    result = database.execute_query(f"SELECT * FROM bigquery_test")
    data = []

    for res in result:
        data.append(
            {"id": res.id, "number": res.number, "created_at": str(res.created_at)}
        )
        print(res)

    bigquery_uploader.upload_bigquery_table(os.getenv("BIGQUERY_TABLE_NAME"), data)
    print("\n\n\n")


scheduler.execute_interval_job_by_minutes(test, minutes=1)
