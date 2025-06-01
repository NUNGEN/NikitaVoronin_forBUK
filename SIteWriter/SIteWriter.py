import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title_elements = soup.find_all("span", class_="titleline")

    print("News Headlines:\n")
    for i, title in enumerate(title_elements[:30], start=1):
        link = title.find("a")
        if link:
            print(f"{i}. {link.text}")
else:
    print("Failed to load the page.")