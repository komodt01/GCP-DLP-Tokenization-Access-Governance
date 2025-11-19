# Compliance Mapping

## NIST 800-53
AC-3: Access Enforcement
IAM Conditions establish policy-based access control.

AC-6: Least Privilege
Terraform assigns minimum required roles for DLP jobs.

SC-13: Cryptographic Protection
DLP de-identification and tokenization (Phase 2) enforce cryptographic
protection of sensitive fields.

SC-28: Protection of Data at Rest
GCS encryption and restricted access protect stored data.

AU-6: Audit Review
Cloud Logging captures all DLP job actions and access attempts.

## ISO 27001 Annex A
A.9 Access Control
IAM policies and role separation support controlled access.

A.10 Cryptography
Tokenization and deterministic encryption (Phase 2) protect sensitive
values.

A.12 Operations Security
Logging and monitoring provide operational oversight.

A.18 Compliance
DLP inspection results help maintain evidence of data protection
activities.

## CIS GCP Benchmark (Relevant Sections)
1.1: Ensure DLP API is enabled
Terraform ensures required APIs are active.

4.2: Ensure logging is enabled for all services
DLP job logs and Storage access logs are captured.

6.1: Ensure least-privilege usage
Service accounts follow minimal IAM role assignments.
