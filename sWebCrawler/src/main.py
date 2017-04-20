'''
Created on Apr 19, 2017

@author: Alex Lee
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.itftennis.com/juniors/players/player/profile.aspx?playerid=100202212")

content = []

content = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[1]/strong')

content_text = content.text
print('content_text: ' + content_text)
# for i 
#     print ('content: ' + i.get_attribute('strong'))
# dig_content = content.fin
