from bs4 import BeautifulSoup
import requests

url = "https://aqicn.org/city/usa/colorado/boulder-cu/athens/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
aqi = soup.find_all(id='aqiwgtvalue')
updated_time = soup.find_all(id='aqiwgtutime')

for elements in aqi:
    print(elements.text)
    print(elements['title'])

for elements in updated_time:
    print(elements.text)