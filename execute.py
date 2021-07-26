from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import random
import getpass

class Execute:
    username = ''
    password = ''

    links = [
        
    ]

    comments = [
        
    ]
    def __init__(self):
        self.InputBefore()
        self.browser = webdriver.Firefox()
        self.login()
        self.goToPost()
        self.selesai()

    def InputBefore(self):
        print("Input Username")
        username = input("")

        print("Input Password")
        password = getpass.getpass(prompt = "")

        if (input == "" or password == ""):
            sys.exit()
        else:
            self.username = username
            self.password = password

    def login(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(4)

        user_text = self.browser.find_element_by_xpath("//input[@name='username']")
        user_text.clear()
        user_text.send_keys(self.username)
        time.sleep(3)

        pass_text = self.browser.find_element_by_xpath("//input[@name='password']")
        pass_text.clear()
        pass_text.send_keys(self.password)
        time.sleep(3)

        button = self.browser.find_element_by_xpath("//button[@type='submit']")
        button.click()
        time.sleep(7)

    def goToPost(self):
        for i,posts in enumerate(self.links):
            self.browser.get("https://www.instagram.com/p/"+posts+"/")
            time.sleep(3)
            
            self.browser.execute_script("window.scrollTo(0,200);")
            time.sleep(4)

            if self.comments[i] != 'null':
                comment = lambda: self.browser.find_element_by_tag_name("textarea")
                comment().click()
                comment().send_keys(self.comments[i])
                time.sleep(4)

                comment().send_keys(Keys.RETURN)
                time.sleep(3)
            
            self.like()

            i+=1
            print("execute "+str(i)+" of "+str(len(self.links)))
            sleeptime = random.randint(90,105)
            time.sleep(sleeptime)

    def like(self):
        like_button = lambda: self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
        like_button().click()

    def selesai(self):
        self.browser.close()
        sys.exit()

bost = Execute()
