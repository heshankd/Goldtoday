from typing import Container
#pip install beautifulsoup4
#pip install requests
from bs4 import BeautifulSoup as soup
import requests

##Recomended Tutorial https://www.youtube.com/watch?v=87Gx3U0BDlo

myUrl='https://devijewellers.lk/'
#myUrl=input("Enter the website in this format (https://xyz.com) : ",)
page = requests.get(myUrl) #get content from webpage
#print(page) #shows request suceessful or not , ex: <Response [200]>
content = page.content #we can use "page.text" also, this takes page content, but this is unstructured version
soup = soup(page.text,"lxml") #This is same as content but this is structured to XML
#print(soup.prettify()) #nicely formatted to HTML
#print(page.status_code)  #prints page code, Ex: 200
#print(page.headers) #prints page header
ourguy = soup.find_all("script") #Get all script tags in HTML >> this comes as a list
ourguy = soup.find_all("script")[16] #Get 16th element of the list, which has the needed information
ourguystr=str(ourguy) #convert the "bs4.element.Tag" to string

#print(type(ourguystr))

split = ourguystr.split() #split the string type script output to elements using lists
#print(split)
#print(type(split))
Current_Date = split[8] #get 8th elemnt of that as date
twentytwo = split[14] #get 14th elemnt of that as 22Kt price
twentyfour = split[20] #get 20th elemnt of that as 24Kt price
DateStr = str(Current_Date); TwentyTwoStr = str(twentytwo); TwentyFourStr = str(twentyfour)
Date1 = Current_Date.replace("'","")
TwentyTwo1 = TwentyTwoStr.replace("'","")
TwentyFour1 = TwentyFourStr.replace("'","")
Date = Date1.replace(";","")
TwentyTwo = TwentyTwo1.replace(";","")
TwentyFour = TwentyFour1.replace(";","")
print("Last Update : "+"On "+Date+", 22Kt Gold is Rs."+TwentyTwo+" and 24Kt Gold is Rs."+TwentyFour+".") #print Date, 22 and 24Kt prices 




