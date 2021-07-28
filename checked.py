from selenium import webdriver
import sys
import getpass
import time

class Checked:
    links = [
    	'CRiBZ-jJ58g', 'CR058esJZhx', 'CRN7nVJNCgZ', 'CRv3OZiAit1', 'CRjMzBriTDx', 'CRikGGzMpzT', 'CPoGi1UjKR1', 'CRuQRYxB2aF', 'CRg9kd_BXAe', 
    	'CR096rRNDPv', 'CQ36Lz9MJrf', 'CLcpkdDFFzW', 'CN2Vkp3DEkf', 'CRwdn_1thkT', 'CR1SKAagXAW', 'CR3Bj13M7_M', 'CRtqI2Yreas', 'CRkriiZJ1jT', 
    	'CRKy3K3nFj9', 'CQ2-Hddrq-V', 'CRIOQWyL3V-', 'CRJWL5-AOn6', 'CRLMeMFtH7s', 'CRa6_4EJcgX', 'CRQ7TQXLxWC', 'CRtVvMQsh1b', 'CRykNIslfrV', 
    	'CRabSGlrVCy', 'CR22BBkB6PP', 'CR1g7eiM49L', 'CR3iN6LnU8R', 'CR20ew8snn8', 'CRF3yNiMfOz', 'CRdsa-fDCMe', 'CRTXvWFJ2Dw', 'CRVMjlhp1tZ', 
    	'CRvLvgOhrVn', 'CR3vVBcrl2x', 'CR00Hs-LgHT', 'CR0Ll-bMtWD', 'CRyYP_vFT0e', 'CRvsvmpJ8fO', 'CR1KujeJO98', 'CR0IQ-8jkr1', 'CR2eSV-Lsqv', 
    	'CR3q7GvDVrG', 'CR1G_5LrKw9', 'CR2hzaKtdYx', 'CRseyOpDjDt', 'CRvMsJolQsS', 'CR3jvAMJQIJ', 'CR0etM2s8N-', 'CR3s3_lLO-L', 'CRnTt3sr2Vq', 
    	'CR2LamxlxxA', 'CR3M-hxpBzu', 'CR0YDktrD--', 'CR3kUs-pAGF', 'CR3XL9-pKbL', 'CRyRtxzhbqo'
    ]

    final_links = []
    comments = []

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.checked_post()
        self.finish()

    def checked_post(self):
        for i, link in enumerate(self.links):
            self.browser.get("https://www.instagram.com/p/"+link+"/")
            i+=1
            
            print("Apakah postingan "+link+" "+str(i)+" of "+str(len(self.links))+" akan anda like atau komen? y/n")
            time.sleep(3)

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
