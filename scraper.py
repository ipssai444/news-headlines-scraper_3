import requests
from bs4 import BeautifulSoup

# Step 1: Send GET request to BBC News
url = "https://www.bbc.com/news"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Find all headlines
headlines = soup.find_all("h2", {"data-testid": "card-headline"})

# Step 4: Print the headlines
for i, headline in enumerate(headlines, start=1):
    print(f"{i}. {headline.text.strip()}")
# Step 5: Save the headlines to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines, start=1):
        file.write(f"{i}. {headline.text.strip()}\n")
