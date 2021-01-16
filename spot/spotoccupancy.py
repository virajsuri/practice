from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import csv
import time

url = "https://portal.rockgympro.com/portal/public/415a34a23151c6546419c1415d122b61/occupancy?&iframeid=occupancyCounter&fId=1038"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

while(True):
    s = soup.find_all('script')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)

    for x in s:
        if("BLD" in str(x)):
            array = (str(x).split("\n"))
            for units in array:
                if("count" in units):
                    print(int(re.search(r'\d+', units).group()))

                    with open('occupancy.csv', mode='a') as occupancy_file:
                        employee_writer = csv.writer(occupancy_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        employee_writer.writerow([int(re.search(r'\d+', units).group()), dt_string])
                    break

    time.sleep(60)