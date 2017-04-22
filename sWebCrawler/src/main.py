'''
Created on Apr 19, 2017

@author: Alex Lee
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import html5lib

# If I forget to remove the path, heads up, you may need to remove it ;)
driver = webdriver.Chrome('C:\chromedriver\chromedriver')
driver.get("http://www.itftennis.com/juniors/players/player/profile.aspx?playerid=100202212")
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



driver.find_element_by_id('__tab_tabActivities').click()
driver.find_element_by_id('btnViewAll').click()


match = driver.find_elements_by_class_name('ulMatch')
td20 = driver.find_elements_by_class_name('td-20')
td30 = driver.find_elements_by_class_name('td-30')
td120 = driver.find_elements_by_class_name('td-120')

td20_text = []
td30_text = []
td120_text = []
match_text = []

td20_temp = []
td30_temp = []
td120_temp = []

temp = ''

start = td20[0].text

numTraversed = 0

len20 = td20.__len__()
len30 = td30.__len__()
len120 = td120.__len__()

# if (len20 == len30 == len120):
#     for i in range (len20):
#         if ((i + 1) != len20 and start == td20[i + 1].text):
#             start = td20[i + 1].text
#
#             numTraversed -= 1
#
#             for i in range (numTraversed):
#                 td20_temp.pop(0)
#
#             td20_text.append(td20_temp.pop(0))
#
#             numTraversed = 0
#             continue
#
#         td20_temp.append(td20[i].text)
#         numTraversed += 1

for i in range (len20):
    td20_text.append(td20[i].text)
    td30_text.append(td30[i].text)
    td120_text.append(td120[i].text)

for i in range (len20):
    print (td20_text[i] + ' ' + td30_text[i] + ' ' + td120_text[i])

for i in match:
    temp = str(i.text)

    if temp.__contains__('Doubles'):
        continue

    match_text.append(i.text)
x = 0
for i in match_text:
    x += 1
    print (i)

print (x)

driver.close()

# for i
#     print ('content: ' + i.get_attribute('strong'))
# dig_content = content.fin
