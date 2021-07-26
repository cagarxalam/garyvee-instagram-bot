from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import random
import getpass

class URL:
    username = ''
    password = ''
    hashtags = []
    links    = []

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.login()
        self.TopPost()
        self.finalize()

    def login(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(1)


        user_text = self.browser.find_element_by_xpath("//input[@name='username']")
        user_text.clear()
        user_text.send_keys(self.username)
        time.sleep(1)
        
        pass_text = self.browser.find_element_by_xpath("//input[@name='password']")
        pass_text.clear()
        pass_text.send_keys(self.password)
        time.sleep(1)

        button = self.browser.find_element_by_xpath("//button[@type='submit']")
        button.click()
        time.sleep(5)

    def TopPost(self):
        for hashtag in self.hashtags:
            self.browser.get("https://www.instagram.com/explore/tags/"+hashtag)
            time.sleep(5)

            links = self.browser.find_elements_by_tag_name("a")
            condition = lambda urls: "https://www.instagram.com/p/" in urls.get_attribute("href")
            valid_links = list(filter(condition,links))

            for i in range(0,9):
                click_link = valid_links[i].get_attribute("href").replace("https://www.instagram.com","")
                post_click = self.browser.find_element_by_xpath("//a[@href='"+click_link+"' and @tabindex='0']").find_element_by_xpath("..")
                post_click.click()
                time.sleep(3)

                like = self.browser.find_element_by_xpath("//div[@class='QBdPU ']/span/*[name()='svg']").get_attribute("aria-label")
                if like == "Like":
                    like_links = click_link.replace("/p/",'').replace('/','')
                    if like_links not in self.links:
                        self.links.append(like_links)

                close_click = self.browser.find_element_by_xpath("/html/body/div[5]/div[3]/button")
                close_click.click()
                time.sleep(3)

    def finalize(self):
        print(self.links)
        self.browser.close()
        sys.exit()
scrapt = URL()