# Teardown Guide for GCP DLP Inspection Job Project

This guide provides a step-by-step process to safely and completely remove all GCP resources created during the DLP inspection job project.

---

## ⚠️ Important Notes
- Ensure you no longer need the results or logs before deleting.
- This operation is irreversible.

---

## Step-by-Step Teardown

### 1. Deactivate Virtual Environment (If Active)
```bash
deactivate
```

---

### 2. Delete the BigQuery Dataset (Optional)
If you created a dataset for test purposes:
```bash
bq rm -r -f -d [PROJECT_ID]:[DATASET_NAME]
```

---

### 3. Remove DLP Jobs
List and delete jobs as needed:
```bash
gcloud alpha dlp jobs list --project=[PROJECT_ID]
gcloud alpha dlp jobs delete [JOB_ID] --project=[PROJECT_ID]
```

---

### 4. Delete Terraform-managed Resources
```bash
terraform destroy
```

---

### 5. Clean Up Local Files (Optional)
```bash
rm -rf .terraform terraform.tfstate* dlp_findings.csv
```

---

## Summary
You have now fully torn down the GCP DLP inspection infrastructure. Make sure billing is not incurred on leftover resources.
