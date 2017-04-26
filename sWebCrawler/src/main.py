'''
Created on Apr 19, 2017

@author: Alex Lee
@editor: Bijan Razavi
'''
from selenium import webdriver
from bs4 import BeautifulSoup

# If I forget to remove the path, heads up, you may need to remove it ;)
# driver = webdriver.PhantomJS ()
# driver = webdriver.PhantomJS ('C:\phantomjs-2.1.1-windows\bin\phantomjs')
driver = webdriver.Chrome ()
driver.get ("http://www.itftennis.com/juniors/players/player/profile.aspx?playerid=100202212")
parser = BeautifulSoup (driver.page_source, 'html5lib')

dataSave_text = ''

content = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[1]/strong')
age = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[2]/strong')

dataSave_text = content.text + ', ' + age.text

driver.find_element_by_id ('__tab_tabActivities').click ()
driver.find_element_by_id ('btnViewAll').click ()

teamSize = driver.find_elements_by_css_selector ('.ulMatch li:nth-child(1)')
grade = driver.find_elements_by_css_selector ('.ulMatch li:nth-child(2)')
td20 = driver.find_elements_by_css_selector ('table tr:last-child .td-20')
td30 = driver.find_elements_by_css_selector ('table tr:last-child .td-30')
td120 = driver.find_elements_by_css_selector ('table tr:last-child .td-120')

for i in range(int (teamSize.__len__())):
    if str (teamSize[i].text).__contains__('Doubles'):
        continue

    dataSave_text = dataSave_text + ', ' + teamSize[i].text + ', ' + grade[i].text + ', ' + td20[i].text + ', ' + td30[i].text + ', ' + td120[i].text

print (dataSave_text)

driver.quit()