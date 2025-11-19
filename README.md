# GCP DLP Tokenization & Access Governance  
## Phase 1 – DLP Inspection and Data Classification Pipeline

## Purpose
This project implements the first phase of a Google Cloud data protection
pipeline using Cloud DLP. It performs automated inspection of sensitive
data, classifies findings, and exports results for analysis. This phase
lays the foundation for future tokenization and access governance controls.

The goal is to demonstrate how Cloud DLP can identify sensitive fields in
structured data and how Terraform can automate the infrastructure
required for a secure inspection workflow.

## What This Project Does
- Enables required Google Cloud APIs (DLP, Storage, Logging, Monitoring)
- Creates storage resources for inspection input and export results
- Builds a reusable Cloud DLP inspection template
- Runs a Python-based DLP inspection job (dlp_pipeline.py)
- Identifies sensitive fields such as emails, phone numbers, and IDs
- Exports findings to CSV for downstream processing or audit review
- Uses Terraform for automated setup and teardown
- Includes a diagram showing end-to-end inspection flow

## How It Works
1. A GCS bucket stores the file or dataset to be inspected.
2. Terraform deploys a DLP inspection template for PII detection.
3. The Python script (dlp_pipeline.py) calls the DLP API to scan the data.
4. DLP detects sensitive values based on the inspection template.
5. Findings are written to CSV for reporting or analysis.
6. Logs are captured in Cloud Logging for audit and traceability.
7. Teardown removes resources safely once testing is complete.

## Architecture
See **GCL_DLP_Diagram.png** for a visual overview of the process:
Input Data → DLP Scan → Findings Export → Logging → Governance Pipeline

## Files in This Repository
- main.tf – Core Terraform configuration
- variables.tf – Project input variables
- dlp_pipeline.py – Python script that runs the DLP inspection
- design_overview.md – Architectural description and business context
- technologies.md – Services and tools used
- security_requirements.md – Security controls and requirements
- compliance_mapping.md – Mapping to ISO/NIST controls
- risks_and_mitigations.md – Threats and safeguards
- lessonslearned.md – Summary of lessons from the project
- teardown.md – Instructions for safe resource removal
- GCL_DLP_Diagram.png – Inspection pipeline diagram

## Deployment
1. Update variables in terraform.tfvars.
2. Run:
   terraform init  
   terraform plan  
   terraform apply
3. Execute the Python pipeline:
   python3 dlp_pipeline.py

## Teardown
Use teardown.md for instructions to remove all project resources.

## Notes
This phase focuses on detection and classification.  
Phase 2 will add tokenization, de-identification, and IAM-based access
governance controls. This project is intended for portfolio and learning
purposes.

