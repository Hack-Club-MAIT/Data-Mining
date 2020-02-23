from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import urllib.request
import sys
from urllib.error import HTTPError
options = Options()
#options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
parm = sys.argv[1]

url = 'https://timesofindia.indiatimes.com/' + param1 + '/' + param2 '/' param3 '/archivelist/year-' + param1 ',month-' + param2 ',starttime-43831.cms'
driver.get(url)

search_bar = driver.find_element_by_xpath("//input[@name='q']")
search_bar.send_keys(parm)
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
driver.find_element_by_xpath("//a[contains(text(),'Images')]").click()
d=0
imgs = driver.find_elements_by_class_name("rg_ic.rg_i")
for i in imgs:
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    i.click()
    print(i)
    dow = i.find_element_by_xpath("//img[@class='irc_mi']")
    down = (dow.get_attribute("src"))
    print(down)
    try:
        filename = "images/file_%d.jpg"%d
        urllib.request.urlretrieve(down, filename)
        d+=1
    except TypeError:
        print("skip")
    except HTTPError:
        print("HTTPError")
    



#links = driver.find_elements_by_xpath("//div[@class='r']/a")
#print(links[4].get_attribute('href')) #first link
##for i in links:
##    print(i.get_attribute('href'))
    
    
#driver.quit()



