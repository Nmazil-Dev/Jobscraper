from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests

#Search Values and Url for Indeed.com
search_val = "python"
indeed_url = "https://www.indeed.com/jobs?q=" + search_val + "\&l=60513&sort=date"

# #Selenium automation settings
# driver = webdriver.Chrome()
# driver.get(indeed_url)
# time.sleep(5)
# driver.quit()

page = requests.get(indeed_url)
soup =  BeautifulSoup(page.content, 'html.parser')
result = soup.find_all(True, {'class':["jobsearch-SerpJobCard", "unifiedRow"]})

#If href="/rc/":
#   url_body = "/rc/"
#   url = indeed.com + url_body

#Else:
#Get the id for the div and use it to click the link with selenium
#copy the url from selenium after clicking the link
job_listings = []
for item in result:
    try:
        job_div = item.find(class_="turnstileLink", text=True)
        job_link = item.find('a', href=True).get('href')
        job_title = job_div.text
        if job_link[:4] == '/rc/':
            job_listings.append({'title': job_title[1:], 'job_link': "http://www.indeed.com" + job_link})
        #TODO get the inner href and tell if /rc/ or not 
            #If it is save it
            #Else use selenium to get the proper url for the listing 

        
    except AttributeError:
        pass

print(job_listings)