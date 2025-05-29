# WSL + Google Cloud CLI Setup

## Install GCloud SDK
```bash
sudo apt update && sudo apt install apt-transport-https ca-certificates gnupg curl -y
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /tmp/google.gpg
sudo install -o root -g root -m 644 /tmp/google.gpg /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt update && sudo apt install google-cloud-sdk -y
```

## Authenticate
```bash
gcloud init --console-only
```

## Enable APIs
```bash
gcloud services enable dlp.googleapis.com bigquery.googleapis.com secretmanager.googleapis.com iam.googleapis.com logging.googleapis.com
```
