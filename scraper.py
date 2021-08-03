from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import itertools
from selenium.common.exceptions import NoSuchElementException
from explicit import waiter, XPATH
import random

class InstaBot():
    def __init__(self, username, password):
        self.driver = webdriver.Edge("D://Edge Driver//msedgedriver.exe")
        self.username = username
        self.password = password
        self.driver.get('https://instagram.com')
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
        sleep(5)
        notnow = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(10)
        notnow2 = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a').click()
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        sleep(5)
        followers = self.get_followers()  
        driver.quit()     
        return followers
    
    def get_followers(self):
        number_of_followers = int(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text)
        print(number_of_followers)
        fBody  = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        number_in_list = 0
        while number_in_list < number_of_followers: # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            sleep(5)
            scroll += 1
            links = fBody.find_elements_by_tag_name('a')
            names = [name.text for name in links if name.text != '']
            number_in_list = len(names)
            fList  = self.driver.find_elements_by_xpath("//div[@class='isgrP']//li")
        print("fList len is {}".format(len(fList)))
        return names


# if __name__ == '__main__':
	# InstaBot("epic.valo.fails", "EpicValoFails")