# Phase 2 Roadmap – Tokenization & Access Governance

## Purpose
Extend the Phase 1 DLP inspection pipeline into a full tokenization and
access governance solution.

## Planned Enhancements

### Tokenization and De-Identification
- Apply deterministic encryption to sensitive values.
- Support reversible tokenization for approved roles.
- Use DLP de-identification templates for consistency.

### Access Governance
- Restrict de-tokenization to privileged roles.
- Apply IAM Conditions for request-based access restrictions.
- Use Access Levels if organization support becomes available.

### Detokenization Workflow
- Add a controlled process for restoring original sensitive values.
- Require explicit approvals or break-glass workflows where needed.

### Monitoring and Alerting
- Create Monitoring alerts for DLP job failures or anomalies.
- Alert on unauthorized access attempts or sensitive data reads.

### Evidence and Reporting
- Store DLP job history for audit readiness.
- Produce automated security posture reports.

### Possible Integrations
- BigQuery governance
- Data Catalog tagging
- VPC Service Controls
