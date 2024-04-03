import os
import random
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import yaml


SCRIPTDIR = os.path.dirname(__file__)
YAMLFILE = os.path.join(SCRIPTDIR, 'params.yaml')
with open(YAMLFILE, 'r') as file:
    params = yaml.safe_load(file)

year = params['year']
base_url = f'https://www.ncei.noaa.gov/data/local-climatological-data/access/{year}/'

# Make a request to the API
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find("table").find_all("tr")[2:-2]

# Select random files
selected_files = [rows[random.randint(0, len(rows))].find_all("td")[0].text for _ in range(params['no_locs'])]

# Write binary data to the local directory
for filename in selected_files:
    file_url = base_url + filename
    response = requests.get(file_url)
    open(filename, 'wb').write(response.content)
    print("done")

# Zip the files to be used by the next stage of the pipeline
with ZipFile(os.path.join(SCRIPTDIR, '/weather.zip'),'w') as zip_file:
    for filename in selected_files:
        zip_file.write(filename)