# Technologies Used

## Google Cloud DLP API
Used to scan BigQuery tables for sensitive information.

## BigQuery
Stores the dataset containing potentially sensitive records.

## Python
Used for scripting DLP job creation and result retrieval.

## Terraform
Used to automate the setup of APIs and permissions.

## CSV
Export format for findings.

## How it Works
- A DLP job is initiated to scan a BigQuery table.
- The DLP API identifies sensitive data types.
- The job results are saved to a CSV file.
