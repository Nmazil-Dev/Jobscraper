from bs4 import BeautifulSoup
import requests

search_val = "python"
indeed_url = "https://www.indeed.com/jobs?q=" + search_val + "\&l=60513"
page = requests.get(indeed_url)
soup =  BeautifulSoup(page.content, 'html.parser')
result = soup.find(id="sja0")
print(result)