import os
from google.cloud import dlp_v2

def inspect_bigquery_table(project_id, dataset_id, table_id):
    dlp = dlp_v2.DlpServiceClient()
    parent = f"projects/{project_id}"
    table_ref = {
        "project_id": project_id,
        "dataset_id": dataset_id,
        "table_id": table_id
    }
    config = {
        "info_types": [{"name": "PERSON_NAME"}, {"name": "EMAIL_ADDRESS"}],
        "include_quote": True,
    }
    storage_config = {"big_query_options": {"table_reference": table_ref}}
    inspect_job = {
        "inspect_config": config,
        "storage_config": storage_config
    }
    response = dlp.create_dlp_job(parent=parent, inspect_job=inspect_job)
    print(f"DLP job created: {response.name}")

# Replace these before running
inspect_bigquery_table("your-project-id", "your_dataset", "your_table")
