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
    right_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(right_now)

    for x in s:

        #If soup is for the Boulder gym
        if("BLD" in str(x)):
            array = (str(x).split("\n"))
            for units in array:

                #If on occupancy count line in soup
                if("count" in units):
                    current_occupancy = int(re.search(r'\d+', units).group())
                    print(current_occupancy)

                    #Append to CSV
                    with open('occupancy.csv', mode='a') as occupancy_file:
                        employee_writer = csv.writer(occupancy_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        employee_writer.writerow([current_occupancy, right_now])
                    print()
                    break

    time.sleep(60)