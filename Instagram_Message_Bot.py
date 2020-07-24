from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from getpass import getpass
from PIL import Image
from tkinter import filedialog
from time import sleep
import tkinter as tk

class InstaBot:
    def __init__(self, username, password, message1, finalURL, searchID, var):

        self.driver = webdriver.Chrome("C:\Milan\python\chromedriver.exe")  #Enter complete address of chromedriver.exe
        self.username = username                                            #Host userID
        self.password = password                                            #Host password. Password will not be visible when typed.
        self.message1 = message1                                            #Text message to be sent.
        self.finalURL = finalURL                                            #Local URL of the image to be sent.
        self.searchID = searchID                                            #Target userID
        self.var = var                                                      #Variable to decide text/image.

        self.driver.get("https://instagram.com")                            #Instagram URL
        sleep(2)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)        #Username is entered

        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)        #Password is entered

        self.driver.find_element_by_xpath('//button[@type="submit"]').click()                       #User is logged in provided input is valid.
        sleep(4)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

        self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]").send_keys(searchID)   #Searches target 
        sleep(2)
        
        K = "https://www.instagram.com/" + searchID + "/"
        
        self.driver.get(K)                                                                          #Visit target's Instagram profile
        sleep(2)
        
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span").click()
        sleep(2)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Message')]").click()  
        sleep(2)

        if (self.var == 1):                                                                         #If (choice == text)

            self.driver.find_element_by_xpath("//*[@placeholder=\"Message...\"]").send_keys(message1)
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()         #Send Text

        else:                                                                                       #If (choice == image)

            self.driver.execute_script("window.open('');")
            
            self.driver.switch_to.window(self.driver.window_handles[1])                             # Switch to the new window and open image URL
            self.driver.get(finalURL)
            img = self.driver.find_element_by_xpath('/html/body/img')

            actionChains = ActionChains(self.driver)
            actionChains.move_to_element(img).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  #Copy Image
            self.driver.switch_to.window(self.driver.window_handles[0])                                             #Switch to original Instagram tab

            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(Keys.CONTROL + "v")
            self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()                         #Send Image


username = input("Insta username: ")
password = getpass("Password: ")
searchID = input("Insta username of target: ")
choice = input("text or image? : ")

if (choice == "text"):
    var = 1
    finalURL = ""
    message1 = input("Type message to be sent: ")
    my_bot = InstaBot(username, password, message1, finalURL, searchID, var)

elif (choice == "image"):  
    var = 0
    message1 = ""
    from pwdvkn import *
    finalURL = "file:///" + imageAddr + imageJPG
    my_bot = InstaBot(username, password, message1, finalURL, searchID, var)



        
