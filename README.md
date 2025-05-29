# GCP DLP Inspection Project

## Overview
This project demonstrates how to use Google Cloud's Data Loss Prevention (DLP) API to inspect a BigQuery table for sensitive information types (e.g., PERSON_NAME, EMAIL_ADDRESS). The findings are exported to a CSV file for further analysis.

## Files Included
- `dlp_pipeline.py`: Initiates the DLP inspection job on a BigQuery table.
- `dlp_results.py`: Retrieves and prints the results of the DLP job, also exporting findings to a CSV.
- `main.tf`: Terraform configuration to enable DLP API and required IAM roles.
- `variables.tf`: Variables for Terraform configuration.
- `lessonslearned.md`: Key learnings and troubleshooting tips.
- `technologies.md`: Explains the technologies used and how they work.
- `comparison.md`: Compares DLP on GCP vs AWS Macie vs Azure Purview.
- `diagram.png`: Architectural diagram of the DLP inspection flow.
- `acronyms.md`: Definitions of common acronyms used.

## Business Use Cases
- Compliance validation for GDPR, HIPAA, PCI-DSS.
- Identifying and remediating sensitive data exposure.
- Automating audits and reporting in data governance programs.
