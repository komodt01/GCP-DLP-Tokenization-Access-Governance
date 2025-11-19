# Design Overview

## Purpose
This project demonstrates how Google Cloud DLP can identify and classify
sensitive data, and how this inspection capability forms the first step
toward a larger tokenization and access governance framework. The design
uses Terraform and a Python-based DLP pipeline to automate the discovery
of sensitive fields in stored data.

## Phase 1 Scope
Phase 1 focuses on inspection and classification:
- Detect sensitive values in structured data
- Export findings for audit or downstream controls
- Use Cloud Logging for monitoring and traceability
- Prepare resources required for tokenization and governance

## Future Phase 2 Scope
Phase 2 will extend the design to include:
- Deterministic tokenization of sensitive fields
- Access governance based on IAM Conditions
- Optional Access Levels for request-based restrictions
- Role separation for detokenization operations
- Policy-driven data access workflows

## How It Works
1. Terraform deploys required APIs and storage resources.
2. A DLP inspection template defines the sensitive types to detect.
3. The Python script (dlp_pipeline.py) runs an inspection job.
4. Findings are exported to a CSV file for analysis.
5. Logs and activity are captured in Cloud Logging.
6. Teardown removes resources when testing is complete.

## Architecture Summary
Input Data → DLP Inspection Template → DLP API Scan  
→ Findings Export → Logging → Governance Pipeline (Phase 2)

## Design Constraints
- No Access Context Manager features without a GCP organization node.
- Tokenization and de-identification are planned for Phase 2.
- Inspection jobs may take time on large datasets.

## Intended Outcome
This phase establishes the foundation for a full data protection
solution that includes classification, tokenization, and access
governance using built-in GCP services.
