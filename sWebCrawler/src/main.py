'''
Created on Apr 19, 2017

@author: Alex Lee
@editor: Bijan Razavi
'''
from selenium import webdriver
from datetime import datetime
from datetime import date

# If I forget to remove the path, heads up, you may need to remove it ;)
driver = webdriver.PhantomJS ('C:\Python27\phantomjs')
# driver = webdriver.Chrome ('C:\Python27\chromedriver.exe')

def scoreCalc (grade, position, result):
    score = 0

    if (str (grade).__contains__ ('Grade A')):
        if (str (position).__contains__ ('FR') and str (result).__contains__ ('W')):
            score = 250
        if (str (position).__contains__ ('FR') and str (result).__contains__('L')):
            score = 180
        if (str (position).__contains__ ('SF')):
            score = 120
        if (str (position).__contains__ ('QF')):
            score = 80
        if (str (position).__contains__ ('16')):
            score = 50
        if (str (position).__contains__ ('32')):
            score = 30

    if (str (grade).__contains__ ('Grade 1')):
        if (str (position).__contains__ ('FR') and str (result).__contains__ ('W')):
            score = 150
        if (str (position).__contains__ ('FR') and str (result).__contains__ ('L')):
            score = 100
        if (str (position).__contains__ ('SF')):
            score = 80
        if (str (position).__contains__ ('QF')):
            score = 60
        if (str (position).__contains__ ('16')):
            score = 30
        if (str (position).__contains__ ('32')):
            score = 20

    if (str (grade).__contains__ ('Grade 2')):
        if (str (position).__contains__ ('FR') and str (result).__contains__ ('W')):
            score = 100
        if (str (position).__contains__ ('FR') and str (result).__contains__ ('L')):
            score = 75
        if (str (position).__contains__ ('SF')):
            score = 50
        if (str (position).__contains__ ('QF')):
            score = 30
        if (str (position).__contains__ ('16')):
            score = 20
        if (str (position).__contains__ ('32')):
            score = 10

    if (str (grade).__contains__ ('Grade B1')):
        if (str (position).__contains__ ('FR') and str (result).__contains__ ('W')):
            score = 180
        if (str (position).__contains__ ('FR') and str (result).__contains__('L')):
            score = 120
        if (str (position).__contains__ ('SF')):
            score = 80
        if (str (position).__contains__ ('QF')):
            score = 60
        if (str (position).__contains__ ('16')):
            score = 30
        if (str (position).__contains__ ('32')):
            score = 20

    if (str (grade).__contains__ ('Grade B2')):
        if (str (position).__contains__ ('FR') and str (result).__contains__ ('W')):
            score = 120
        if (str (position).__contains__ ('FR') and str (result).__contains__('L')):
            score = 80
        if (str (position).__contains__ ('SF')):
            score = 60
        if (str (position).__contains__ ('QF')):
            score = 40
        if (str (position).__contains__ ('16')):
            score = 25
        if (str (position).__contains__ ('32')):
            score = 10

    return score

url = 'http://www.itftennis.com/juniors/players/player/profile.aspx?playerid=100202212'

driver.get (url)

data_save_text = ''

name = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[1]/strong')
born = driver.find_element_by_xpath('//*[@id="PlayerDiv"]/div[1]/div/div[2]/ul/li[2]/strong')

id = url.split ('=')[-1]

if not str(name.text):
    print ('Fail 1')
    driver.quit()

if str(born.text):
    born = datetime.strptime(str(born.text), '%d %b %Y')

    today = date.today()

    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    data_save_text = id + ', ' + name.text + ', ' + age.__str__()
else:
    print ('Fail 2')
    driver.quit()

driver.find_element_by_id ('__tab_tabActivities').click ()
driver.find_element_by_id ('btnViewAll').click ()

teamSize = driver.find_elements_by_css_selector ('.ulMatch li:nth-child(1)')
grade = driver.find_elements_by_css_selector ('.ulMatch li:nth-child(2)')
td20 = driver.find_elements_by_css_selector ('table tr:last-child .td-20')
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

count = 0

score = 0

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

    count += 1

    score += scoreCalc (grade[i].text, td20[i].text, td30[i].text)

score = score / count

data_save_text = data_save_text + ', ' + str (gAP) + ', ' + str (gAW) + ', ' + str (gAL) + ', ' + str (g1P) + ', ' + str (g1W) + ', ' + str (g1L) + ', ' + str (gB1P) + ', ' + str (gB1W) + ', ' + str (gB1L) + ', ' + str (gB2P) + ', ' + str (gB2W) + ', ' + str (gB2L) + ', ' + str (g2P) + ', ' + str (g2W) + ', ' + str (g2L) + ', ' + str (score)

print (data_save_text)

driver.quit()