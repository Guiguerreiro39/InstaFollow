import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def scroll(elem, driver):
    last_ht, ht = 0, 1
    while(last_ht != ht):
        last_ht = ht
        sleep(1)
        ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, elem)

with open('./Credentials.json', 'r') as json_file:
    jfile = json_file.read()

parsed_json = json.loads(jfile)

username = parsed_json['Account'][0]['Username']
password = parsed_json['Account'][0]['Password']

driver_path = "./env/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.instagram.com")

sleep(2)
assert "Instagram" in driver.title

# Clicks on Log In button
elem = driver.find_element_by_link_text('Log in')
elem.click()

sleep(2)
# Enter username
elem = driver.find_element_by_name('username')
elem.send_keys(username)

sleep(1)
# Enter password
elem = driver.find_element_by_name('password')
elem.send_keys(password)

sleep(1)
# Clicks on Log In button
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
elem.click()

sleep(3)
# Notification handling
elem = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
elem.click()

sleep(1)
# Click on profile
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
elem.click()

sleep(2)
# Click on followers
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
elem.click()

sleep(1)
# Save followers on json file


# Scroll down the window
elem = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
scroll(elem, driver)

sleep(1)
# Close followers window
elem = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')
elem.click()

sleep(1)
# Click on following
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
elem.click()

sleep(1)
# Scroll down the window
elem = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
scroll(elem, driver)

sleep(1)
# Close following window
elem = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')
elem.click()
