# Patch Intelligence

This project collects patch version data from PyPI (for the python-requests library) and links them to known vulnerabilities (CVEs) from the National Vulnerability Database (NVD). It helps identify which versions are affected or fixed.

## Features

- Web scraping patch history from PyPI
- CVE lookup using the NVD API
- Manual mapping of patch versions to related CVEs
- CSV report generation

## Files in this repository

- `patch_scraper.py` – Scrapes patch version info from PyPI
- `cve_fetcher.py` – Fetches related CVEs from NVD API
- `Patch_Intelligence_Report.csv` – Final table of versions and CVEs
- `Patch_Intelligence_Summary.txt` – Summary of the project

## How to Use

1. Run `patch_scraper.py` to fetch patch versions
2. Run `cve_fetcher.py` to get CVEs
3. Manually or automatically map CVEs to versions
4. View results in the CSV file
