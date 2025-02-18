import requests 
from bs4 import BeautifulSoup 

url = "https://example.com"  
response = requests.get(url)  

# Check if request was successful (Status code 200 means success)
if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print(f"Failed to fetch the webpage, Status Code: {response.status_code}")

soup = BeautifulSoup(response.text, "lxml")  # Parse HTML using lxml parser
print(soup.prettify())  # Print formatted HTML

title = soup.title.text  # Extract title text
print("Page Title:", title)

headings = soup.find_all("h1")  # Extract all <h1> tags
for h in headings:
    print("Heading:", h.text.strip())  # Remove extra spaces

paragraphs = soup.find_all("p", class_="example-class")  # Replace with actual class name
for p in paragraphs:
    print("Paragraph:", p.text.strip())

links = soup.find_all("a")  # Find all <a> (anchor) tags
for link in links:
    print("Link:", link.get("href"))  # Extract href attribute

