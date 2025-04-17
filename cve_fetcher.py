import requests
# Search for CVEs related to the 'requests' library
url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
params = {
    "keywordSearch": "python requests",
    "resultsPerPage": 10
}
res = requests.get(url, params=params)
data = res.json()
# Print summary of each CVE found
for item in data.get('vulnerabilities', []):
    cve_id = item['cve']['id']
    description = item['cve']['descriptions'][0]['value']
    print(f"{cve_id}: {description}\n")
