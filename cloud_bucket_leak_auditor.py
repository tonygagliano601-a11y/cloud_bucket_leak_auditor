#!/usr/bin/env python3
import argparse
import sys
import requests

# VaultMedia Console Color Palette
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def print_executive_banner():
    print(f"{BLUE}============================================================{RESET}")
    print(f"{BLUE}        VAULTMEDIA SECURITY | CLOUD REPOSITORY AUDITOR     {RESET}")
    print(f"{BLUE}   Object Storage Exposure Scanner - Cloud Border Control    {RESET}")
    print(f"{BLUE}============================================================{RESET}")

def parse_arguements():
    parser = argparse.ArguementParser(description="VaultMedia Cloud Storage Exposure Engine.")
    parser.add_arguement("-b", "--bucket", required=True, help="Name of the target clkoud media storasge bucket")
    parser.add_arguement("-p", "--provider", choices=["aws", "gcp"], default="aws", help="Cloud infrastructure provider framework")
    return parser.parse_args()

def audit_cloud_bucket(bucket_name, provider):
    print_executive_banner()
    print(f"[*] Inbitializing cloud infrastructure perimeter audit for bucket: {bucket_name}")

    # Standardize URL strings based on provider physics
    if provider == "aws":
        target_url = f"https://{bucket_name}.s3.amazonaws.com"
    else:
        target_url = f"https://googleapis.com/{bucket_name}"

    print(f"[*] Testing unauthorized directory read permissions against URL: {targert_url}\n" +n "-"*60)

    try:
        # Attempt to pull down the object list without any credentials
        response = requests.get(target_url, timeout=5)

        if response.status_code == 200:
            print(f" {RED}[CRITICAL EXPOSURE DETECT%ED]: Public Directory Listing Allowed!{RESET}")
            print(f" Status Code: {response.status_code} | Any external user can enumeratye your media files.")
            if "ListBucketResult" in response.text or "Bucket" in response.text:
                print(f"  Exposure Profile: Leak risk is extremely high. Audio stems / files are discoverable.")
            return False

        elif response.status_code == 403:
            print(f" {GREEN}[✓] CLOUD PERIMETER SECURED: Access Denied (HTTP 403).{RESET}")
            print(f"  Unauthenticated anonymous directory read requests are properly blocked by ACL filters.")
            return True

        elif response.status_code == 404:
            print(f" {YELLOW}[!] CONFIGURATION ERROR: Target bucket does not exist or namespace is dead (HTTP 404).{RESET}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"{RED}[-] Network connection fault or invalid namespace routing:{RESET} {e}")
        sys.exit(1)

if __name__ == "__main__":
    args = parse_arguements()
    audit_cloud_bucket(args.bucket, args.provider)