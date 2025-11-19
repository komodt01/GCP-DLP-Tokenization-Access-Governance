# Technologies Used

## Google Cloud DLP
Provides inspection, classification, and data de-identification.
Used here to identify sensitive values such as email, phone, and ID
patterns from an input dataset.

## DLP Inspection Template
Defines which infotypes to scan for and ensures scans are repeatable.

## Python DLP Pipeline (dlp_pipeline.py)
Calls the DLP API, runs the inspection job, and exports results to CSV.

## Cloud Storage (GCS)
Stores source data for inspection and stores exported findings.

## IAM Conditions
Forms the basis for future access governance. Conditions allow access
rules based on identity, request time, IP address, or resource properties.

## Access Context Manager (Planned)
Future support for Access Levels and Access Policies if an organization
node becomes available.

## Cloud Logging
Captures DLP job activity, API calls, and audit logs for monitoring.

## Terraform
Automates deployment, configuration, and teardown of all resources.
Ensures that the DLP pipeline can be recreated consistently.

## Cloud Monitoring (Planned)
Will support alerting on sensitive data access or DLP job anomalies in
later phases.
