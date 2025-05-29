resource "google_project_service" "dlp" {
  service = "dlp.googleapis.com"
}

resource "google_project_iam_member" "dlp_user" {
  role   = "roles/dlp.user"
  member = "serviceAccount:${var.service_account_email}"
}
