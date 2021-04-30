import datetime as datetime
from selenium import webdriver
import xlwt
from xlwt import Workbook
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

while True:# forever loop
    wb = xlwt.Workbook()# making a workbook

    sheet1 = wb.add_sheet('Sheet1')# add a new sheet in workbook
    driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Downloads\\chromedriver.exe")# access latest chromedriver from my downloads folder
    a=0# row number in excel sheet
    for i in range(1,3):# loop for two pages of the website
        driver.get("https://floodlist.com/asia/page/" + str(i))# accessing individual website pages

        articles = driver.find_elements_by_class_name('post-img')# get list of articles by class name = post-img

        for article in articles:#iterate for each article
            link = article.find_element_by_css_selector("a").get_attribute('href')# get first link in individual article
            sheet1.write(a,0,link)# write the link in row of sheet
            a=a+1
    today = datetime.now().strftime("date-%d-%m-%Y-time-%H.%M.%S")# get today's timestamp
    wb.save('test-'+today+'.xls')# save workbook in format of timestamp TASK:1
    driver.close()
    time.sleep(14400)# pause for 4 hours then execute same loop TASK:2
