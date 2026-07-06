# %%
from io import StringIO
import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://wikipedia.org"
response = requests.get(url)

# Parse with BeautifulSoup if you need to isolate a specific element
soup = BeautifulSoup(response.text, "html.parser")
target_table = soup.find("table")

# Convert the isolated element to string and wrap it in StringIO
html_stream = StringIO(str(target_table))

# Safely read into Pandas without warnings
dfs = pd.read_html(html_stream)
df = dfs[0]
df

# "Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a "
   