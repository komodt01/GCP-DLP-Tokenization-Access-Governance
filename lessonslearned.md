# Lessons Learned

## DLP Inspection Before Tokenization
Running inspection first helps identify exactly which fields require
tokenization, reducing unnecessary transformations.

## IAM Conditions Are More Flexible Than Expected
Conditions allow fine-grained control over who can run inspection jobs
and view results. They will play a major role in Phase 2 governance.

## Limitations Without an Organization Node
Access Levels and Access Policies require an organization node. This
limits advanced conditional access until an org-level environment is
available.

## Terraform Simplifies Repeatability
Terraform ensures the DLP pipeline can be deployed, tested, and removed
easily, improving development speed and auditability.

## Importance of Clear Separation of Duties
DLP administrators, data owners, and report consumers must remain
separated to avoid privilege escalation or unauthorized data exposure.

## DLP Job Performance Considerations
Large datasets significantly increase scan time. Using smaller input
files is useful for testing.

## Export Formats Matter
Exporting findings to CSV supports downstream audit, reporting, and
governance workflows.
