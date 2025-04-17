import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://pypi.org/project/requests/#history"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

data = []
cards = soup.select('.release__card')
for card in cards:
    version = card.select_one('.release__version').text.strip()
    description_tag = card.select_one('.release__description')
    description = description_tag.text.strip() if description_tag else "No description"
    data.append({"version": version, "description": description})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("requests_patch_data.csv", index=False)

print("✅ Data saved to requests_patch_data.csv")
