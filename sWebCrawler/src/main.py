'''
Created on Apr 19, 2017

@author: Alex Lee
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# If I forget to remove the path, heads up, you may need to remove it ;)
driver = webdriver.Chrome('C:\chromedriver\chromedriver')
driver.get("http://www.itftennis.com/juniors/players/player/profile.aspx?playerid=100202212")

content = []
age = []
match = []

content = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[1]/strong')
age = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[2]/strong')
content_text = content.text
age_text = age.text
print('content_text: ' + content_text)
print (age_text)



driver.find_element_by_id('__tab_tabActivities').click()
driver.find_element_by_id('btnViewAll').click()


match = driver.find_elements_by_class_name('ulMatch')

match_text = []
temp = ''
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

# for i
#     print ('content: ' + i.get_attribute('strong'))
# dig_content = content.fin
