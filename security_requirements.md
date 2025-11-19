# Security Requirements

## Identity and Access
- Use least-privilege IAM roles for DLP, Storage, and Logging.
- Restrict inspection jobs to approved identities.
- Apply IAM Conditions to limit high-risk access paths.
- Separate roles for data owners, DLP administrators, and readers.

## Data Protection
- All input and output data must be encrypted at rest.
- Sensitive values must be classified and tagged.
- Tokenization and masking to be added in Phase 2.
- De-tokenization must be restricted to authorized roles only.

## Logging and Monitoring
- Capture all DLP job events in Cloud Logging.
- Retain audit logs for evidence and review.
- Log exports must not contain sensitive values.
- Failed access attempts should be monitored.

## Governance Controls
- Findings must be traceable to inspection templates.
- DLP configurations must be managed through Terraform.
- Access governance policies must be documented.
- Changes to DLP templates must require approval.

## Compliance Requirements
- Support NIST 800-53 SC, AC, and AU families.
- Support ISO 27001 controls for access and data protection.
- Provide auditable evidence through logs and exported findings.
