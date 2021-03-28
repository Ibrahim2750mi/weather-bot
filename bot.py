from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#paste here

browser.get("https://darksky.net/")


x = input("enter location (city, state, country):")
elem1 = browser.find_element_by_xpath("/html/body/div/form/input")
for i in range(25):
    elem1.send_keys(Keys.BACKSPACE)
elem1.send_keys(x)
time.sleep(3)
elem1.send_keys(Keys.RETURN)

time.sleep(8)

elem2 = browser.find_element_by_xpath("//span[span/@class='summary swap']")

print(elem2.text)

y = input("do want to convert temp in Celsius(y/n)?:")
follow = True

if y == "y":
    temp = input("enter the temp:")
    try:
        int(temp)
    except:
        print("please enter a int")
        follow = False

    if follow:
        k = (int(temp)-32) * (5/9)
        print(str(int(k)) + "° C")
if y == "n":
    print("Thanks for using our weather service")
