import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
url = "https://www.pokemasters.net/tcg/artist/Yuka%20Morii"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with class "table table-striped"
table = soup.find('table', class_='table table-striped')

# Initialize empty lists to store table data
data = {'Number': [], 'Card Name': [], 'Set Name': []}

# Extract data from the table rows
for row in table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    data['Number'].append(columns[0].text.strip())
    data['Card Name'].append(columns[2].text.strip())
    data['Set Name'].append(columns[3].text.strip())

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_filename = "scraped_data.csv"
df.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename}")
