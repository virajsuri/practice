#!/usr/bin/python   

import os, time
import urllib.request

import pandas as pd
import csv

from selenium import webdriver
from openpyxl import load_workbook

def editCSV():
    headers =  ['country_region_code','country_region','sub_region_1','sub_region_2','iso_3166_2_code','census_fips_code',
    'date','retail_and_recreation_percent_change_from_baseline', 'grocery_and_pharmacy_percent_change_from_baseline',
    'parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline',
    'residential_percent_change_from_baseline']

    country_indentifier = 'US'

    with open('../data/googleAppended.csv','w', newline='') as appendFile:
        appendWriter = csv.writer(appendFile, delimiter=",")
        appendWriter.writerow(headers)
        with open('../data/google.csv', mode='r', errors='ignore')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if(lines[0]==country_indentifier and lines[2]==""):                    
                    print(lines)
                    appendWriter.writerow(lines)
                

def getOAGCSVLink():
    executable_path = r'..\GeckoDriver\geckodriver.exe'

    driver=webdriver.Firefox(executable_path=executable_path)

    url = "https://www.oag.com/coronavirus-airline-schedules-data"

    #//*[@id="cta_button_490937_9fbac4e8-8ecf-4471-b7b4-e81d1eb84177"]
    #/html/body/div[1]/div/ui-main-pane/div[2]/div[3]/div[2]/a

    driver.get(url)
    time.sleep(.5)

    downloadButton = driver.find_element_by_link_text("Download Datae")
    targetLink = downloadButton.get_attribute("href")

    print(targetLink)
    driver.quit()

    # return targetLink

getOAGCSVLink()