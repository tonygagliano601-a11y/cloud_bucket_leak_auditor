# ☁️ Cloud Bucket Leak Auditor (VaultMedia Storage Guardrail)

An enterprise-tier object storage exposure scanner designed to analyze public access control lists (ACLs) across decentralized cloud hosting servers (AWS S3 & Google Cloud Storage) holding unreleased tracking stems and media assets.

---

## 📊 Automated Cloud Exposure Mapping
Modern recording studios and creative management teams heavily rely on cloud buckets to share high-volume media files. This script isolates target object configurations and simulates unauthorized external user requests to check if data boundaries are leaking information to anonymous browsers.

```mermaid
graph TD
    classDef target fill:#ef4444,stroke:#991b1b,stroke-width:2px,color:#fff;
    classDef gate fill:#00758f,stroke:#003545,stroke-width:2px,color:#fff;
    classDef secure fill:#1679a7,stroke:#003545,stroke-width:2px,color:#fff;

    A[Target Bucket URL Identified]:::gate --> B{Unauthenticated GET Request}:::gate
    B -->|HTTP 200: Public Read/List Allowed| C[STATUS: HIGH LEAK RISK]:::target
    B -->|HTTP 403: Access Denied ACL| D[STATUS: CLOUD BORDER SECURED]:::secure
    B -->|HTTP 404: Namespace Not Found| E[STATUS: CONFIGURATION ERROR]:::gate
```

---

## 🧰 Core Technical Capabilities
*   **Multi-Cloud Format Detection:** Seamlessly formats target URL endpoints based on the underlying cloud architecture rules for both AWS and GCP.
*   **Anonymous Request Emulation:** Tests real-time endpoint boundaries by sending native, unauthorized directory reads to analyze HTTP server status headers.

---

## 🚀 Execution Profile Syntax
Execute the audit script using standard terminal parameter definitions:
```bash
python3 cloud_bucket_leak_auditor.py -b [BUCKET_NAME] -p [aws/gcp]
```
