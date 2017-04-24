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

tables = []
tables = driver.find_elements_by_tag_name('table')

lastRow = []

for table in tables:
    lastRow.append (table.find_elements_by_xpath('//*[@id="ActivityDiv"]/ul/li[1]/table[1]/tbody/tr[position()=last()]'))

for row in lastRow:
    print (str (row))

match_text = []

temp = ''
#
# td20_text = []
# td30_text = []
# td120_text = []
#
# td20_temp = []
# td30_temp = []
# td120_temp = []
#
# start = int (td20[0].text)
# td20_temp.append(td20[0].text)
#
# numTraversed = 1
#
# len20 = td20.__len__()
# len30 = td30.__len__()
# len120 = td120.__len__()
#
# print ('Test 1 ' + str (td20_temp.__contains__(td20[11].text)))
# print ('Test 2 ' + str (str(td20[11].text).isdecimal() and start <= int(td20[11].text)))
# print ('Test 3 ' + str (str(td30[11].text) == 'l'))
# print ('Test 4 ' + str (str(td30[11].text) == 'L'))
#
# i = 1
#
# if (len20 == len30 == len120):
#     for i in range (1, len20):
#     while i < len20:
#         if ((td20[i].text in td20_temp) or str (td20[i].text).isdecimal() and start < int (td20[i].text) or str (td30[i].text) == 'l' or str (td30[i].text) == 'L'):
#             if (td30[i].text == 'l' or td30[i].text == 'L'):
#                 td20_temp.append(td20[i].text)
#                 numTraversed += 1
#
#             if (str (td20[i].text).isdecimal()):
#                 start = int (td20[i].text)
#             elif (str (td20[i + 1].text).isdecimal()):
#                 start = int (td20[i + 1].text)
#             elif (str (td20[i + 2].text).isdecimal()):
#                 start = int (td20[i + 2].text)
#
#             numTraversed -= 1
#
#             for j in range (numTraversed):
#                 # print ('before 1: ' + str (td20_temp.__len__()))
#                 td20_temp.pop(0)
#                 # print ('after 1: ' + str (td20_temp.__len__()))
#
#             # print ('before 2: ' + str (td20_temp.__len__()))
#             td20_text.append(td20_temp.pop(0))
#             # print ('after 2: ' + str (td20_temp.__len__()))
#
#             if (td30[i].text != 'l' and td30[i].text != 'L'):
#                 td20_temp.append(td20[i].text)
#                 numTraversed = 1
#                 i += 1
#             else:
#                 if (i + 1 != len20):
#                     td20_temp.append(td20[i + 1].text)
#                 i += 2
#                 numTraversed = 1
#             # print (str (i) + ' is our position! 1')
#             continue
#
#         td20_temp.append(td20[i].text)
#         # print (str (i) + ' is our position! 2')
#         numTraversed += 1
#         i += 1
#
# print ('Length: ' + str (td20_text.__len__()))
#
# for i in td20_text:
#     print (i)

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

driver.quit()

#driver.close()

# for i
#     print ('content: ' + i.get_attribute('strong'))
# dig_content = content.fin
