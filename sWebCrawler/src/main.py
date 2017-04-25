'''
Created on Apr 19, 2017

@author: Alex Lee
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import html5lib

# If I forget to remove the path, heads up, you may need to remove it ;)
# driver = webdriver.PhantomJS ()
# driver = webdriver.PhantomJS ('C:\phantomjs-2.1.1-windows\bin\phantomjs')
driver = webdriver.Chrome ()
driver.get ("http://www.itftennis.com/juniors/players/player/profile.aspx?playerid=100202212")
parser = BeautifulSoup (driver.page_source, 'html5lib')

content = []
age = []
match = []
td20 = []
td30 = []
td120 = []

content = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[1]/strong')
age = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[2]/strong')
content_text = content.text
age_text = age.text
print('content_text: ' + content_text)
print (age_text)

driver.find_element_by_id ('__tab_tabActivities').click ()
driver.find_element_by_id ('btnViewAll').click ()

match = driver.find_elements_by_class_name ('ulMatch')

lastRow = driver.find_elements_by_css_selector ('table tr:last-child')

lastRow.pop ()
lastRow.pop ()
lastRow.pop (0)
lastRow.pop (0)

lastRowCleaned = []

temp = ''

match_text = []
lastRow_text = []

for i in range(int (match.__len__())):
    if str (match[i].text).__contains__('Doubles'):
        continue

    match_text.append (match[i].text)
    lastRow_text.append (lastRow[i].text)

for x in range (int (match_text.__len__())):
    print ('Match: ' + match_text[x])
    print ('Last Row: ' + lastRow_text[x])

print ('Match Len: ' + str (match_text.__len__()))
print ('Last Row Len: ' + str (lastRow_text.__len__()))

driver.quit()

# driver.close()

# for i
#     print ('content: ' + i.get_attribute('strong'))
# dig_content = content.fin
