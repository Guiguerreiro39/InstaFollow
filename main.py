import json

from getpass import getpass
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

def notfollowingme():
    with open('Followers.json') as fol1, open('Following.json') as fol2:
        followers = json.load(fol1)
        following = json.load(fol2)

    notFollowing = list()

    for person in following:
        if person not in followers:
            notFollowing.append(person)

    with open('Not_Following_me.json', 'w') as f:
        json.dump(notFollowing, f, indent=4)

def idontfollow():
    with open('Followers.json') as fol1, open('Following.json') as fol2:
        followers = json.load(fol1)
        following = json.load(fol2)

    dontfollow = list()

    for person in followers:
        if person not in following:
            dontfollow.append(person)

    with open('Dont_Follow.json', 'w') as f:
        json.dump(dontfollow, f, indent=4)


try:
    # Begin python script
    print('> Enter username: ')
    username = input()
    print('\n')
    print('> Enter password:')
    password = getpass()

    # Open Chrome with Instagram
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
    try:
        elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        elem.click()

        sleep(3)
        # Notification handling
        elem = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        elem.click()

        sleep(1)
    except Exception as error:
        print('Wrong password! Please try again.')
        quit()

    # Click on profile
    elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
    elem.click()

    sleep(2)
    # Click on followers
    elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    elem.click()

    sleep(1)
    # Scroll down the window
    elem = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
    scroll(elem, driver)

    # Save followers on json file
    links = elem.find_elements_by_tag_name('a')
    followers = [name.text for name in links if name.text != '']

    with open('Followers.json', 'w') as fol:
        json.dump(followers, fol, indent=4)

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

    # Save following on json file
    links = elem.find_elements_by_tag_name('a')
    following = [name.text for name in links if name.text != '']

    with open('Following.json', 'w') as fol:
        json.dump(following, fol, indent=4)

    sleep(1)
    # Close following window
    elem = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')
    elem.click()

    notfollowingme()
    idontfollow()

except Exception as error:
    print('Something weird as happened.. Sorry!')
    quit()