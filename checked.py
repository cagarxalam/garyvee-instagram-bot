from selenium import webdriver
import sys
import getpass
import time

class Checked:
    links = [
        
    ]

    final_links = []
    comments = []

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.checked_post()
        self.finish()

    def checked_post(self):
        for i,link in enumerate(self.links):
            self.browser.get("https://www.instagram.com/p/"+link+"/")
            i+=1
            
            print("Apakah postingan "+link+" "+str(i)+" of "+str(len(self.links))+" akan anda like atau komen? y/n")

            next = getpass.getpass(prompt = "")
            if next == "y":
                if link not in self.final_links:
                    self.final_links.append(link)
                
                comment = input("")
                if comment == "":
                    self.comments.append("null")
                else:
                    self.comments.append(comment)

    def finish(self):
        self.browser.close()
        print(self.comments)
        print(self.final_links)
        sys.exit()

check = Checked()
