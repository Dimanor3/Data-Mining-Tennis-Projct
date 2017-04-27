'''
Created on Apr 19, 2017

@author: Alex Lee
@editor: Bijan Razavi
'''
from selenium import webdriver

# If I forget to remove the path, heads up, you may need to remove it ;)
# driver = webdriver.PhantomJS ()
# driver = webdriver.PhantomJS ('C:\phantomjs-2.1.1-windows\bin\phantomjs')
driver = webdriver.Chrome ()

url = 'http://www.itftennis.com/juniors/players/player/profile.aspx?playerid=100202212'

driver.get (url)

dataSave_text = ''

content = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[1]/strong')
age = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[2]/strong')

id = url.split ('=')[-1]

dataSave_text = id + ', ' + content.text + ', ' + age.text

driver.find_element_by_id ('__tab_tabActivities').click ()
driver.find_element_by_id ('btnViewAll').click ()

teamSize = driver.find_elements_by_css_selector ('.ulMatch li:nth-child(1)')
grade = driver.find_elements_by_css_selector ('.ulMatch li:nth-child(2)')
td30 = driver.find_elements_by_css_selector ('table tr:last-child .td-30')

gAP = 0
g1P = 0
gB1P = 0
gB2P = 0
g2P = 0
gAW = 0
g1W = 0
gB1W = 0
gB2W = 0
g2W = 0
gAL = 0
g1L = 0
gB1L = 0
gB2L = 0
g2L = 0

for i in range(int (teamSize.__len__())):
    if str (teamSize[i].text).__contains__('Doubles') or str (grade[i].text).__contains__ ('Grade 3') or str (grade[i].text).__contains__ ('Grade 4') or str (grade[i].text).__contains__ ('Grade 5'):
        continue

    if str (grade[i].text).__contains__ ('Grade A'):
        gAP += 1

        if str (td30[i].text).__contains__ ('W'):
            gAW += 1

        if str (td30[i].text).__contains__ ('L'):
            gAL += 1

    if str (grade[i].text).__contains__ ('Grade 1'):
        g1P += 1

        if str (td30[i].text).__contains__ ('W'):
            g1W += 1

        if str (td30[i].text).__contains__ ('L'):
            g1L += 1

    if str (grade[i].text).__contains__ ('Grade B1'):
        gB1P += 1

        if str (td30[i].text).__contains__ ('W'):
            gB1W += 1

        if str (td30[i].text).__contains__ ('L'):
            gB1L += 1

    if str (grade[i].text).__contains__ ('Grade B2'):
        gB2P += 1

        if str (td30[i].text).__contains__ ('W'):
            gB2W += 1

        if str (td30[i].text).__contains__ ('L'):
            gB2L += 1

    if str (grade[i].text).__contains__ ('Grade 2'):
        g2P += 1

        if str (td30[i].text).__contains__ ('W'):
            g2W += 1

        if str (td30[i].text).__contains__ ('L'):
            g2L += 1


dataSave_text = dataSave_text + ', ' + str (gAP) + ', ' + str (gAW) + ', ' + str (gAL) + ', ' + str (g1P) + ', ' + str (g1W) + ', ' + str (g1L) + ', ' + str (gB1P) + ', ' + str (gB1W) + ', ' + str (gB1L) + ', ' + str (gB2P) + ', ' + str (gB2W) + ', ' + str (gB2L) + ', ' + str (g2P) + ', ' + str (g2W) + ', ' + str (g2L)

print (dataSave_text)

driver.quit()