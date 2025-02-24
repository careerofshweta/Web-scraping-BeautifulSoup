from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


# url = "https://example.com"
@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": f"Failed to fetch the webpage, Status Code: {response.status_code}"}), 400
    
    soup = BeautifulSoup(response.text, "lxml")
    
    title = soup.title.text if soup.title else "No Title Found"
    headings = [h.text.strip() for h in soup.find_all("h1")]
    paragraphs = [p.text.strip() for p in soup.find_all("p", class_="example-class")]
    links = [link.get("href") for link in soup.find_all("a")]
    
    return jsonify({
        "title": title,
        "headings": headings,
        "paragraphs": paragraphs,
        "links": links
    })

if __name__ == '__main__':
    app.run(debug=True)


