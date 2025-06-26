import requests
from bs4 import BeautifulSoup
import os

def scrape_scholarships():
    url = "https://www.buddy4study.com/scholarships"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    scholarships = []

    # Updated selector for scholarship cards
    for link in soup.select("a[class*=ScholarshipCard_card__]"):
        title = link.get("title")
        href = link.get("href")
        if title and href:
            scholarships.append(f"{title}\nLink: https://www.buddy4study.com{href}\n\n")

    os.makedirs("data", exist_ok=True)
    with open("data/scholarships.txt", "w", encoding="utf-8") as f:
        f.writelines(scholarships)

    print("✅ Scraped and saved to data/scholarships.txt")
    

if __name__ == "__main__":
    scrape_scholarships()
