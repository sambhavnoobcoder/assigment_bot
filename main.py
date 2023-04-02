import pyautogui, sys
# import urllib.request
import time
import requests
import pandas as pd
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         # print("here")
#         # print(int(x) " , " int(y))
#         print(positionStr)
#         print('\b' * len(positionStr), end='')
# except KeyboardInterrupt:
#     print('\n')
#     print("no here")
#
#

    #x: 601 y : 521


# urllib.request.urlopen("https://www.google.co.in/?client=safari&channel=mac_bm")
# import urllib.request

# url = "https://www.google.com/"
# response = urllib.request.urlopen(url)
#
# print(response.read())

# time.sleep(10)
# pyautogui.click(x=601 ,y=521)


# import urllib.request
# # Using urlopen() function with url in it
# webUrl = urllib.request.urlopen('https://www.javatpoint.com/python-tutorial')

import webbrowser as wb

time.sleep(2)
wb.open('https://chat.openai.com')
time.sleep(17)
pyautogui.click(x=601,y=521)
time.sleep(26)
pyautogui.click(x=805,y=823)
pyautogui.hotkey('command','a')
pyautogui.press('backspace')
pyautogui.write("formula for angular momentum. start the answer with here's the answer",)
pyautogui.press('enter')
time.sleep(60)
pyautogui.moveTo(x=477 ,y=230)
from pynput.mouse import Button,Controller
mouse = Controller()
mouse.click(Button.left, 2)
time.sleep(27)
# start_time = time.time() # record the start time
# end_time = start_time + 15 # set the end time for 15 seconds later
#
# while time.time() < end_time: # keep looping until end time is reached
#     pyautogui.hotkey('shift','down')

import keyboard

start_time = time.time() # record the start time
end_time = start_time + 15 # set the end time for 15 seconds later

while time.time() < end_time: # keep looping until end time is reached
    keyboard.press_and_release('shift+down')


time.sleep(7)
pyautogui.hotkey('command','c')

pyautogui.hotkey('command','n')
print('command n executed')
time.sleep(7)
pyautogui.hotkey('command','v')
print('command v executed')
time.sleep(7)
pyautogui.hotkey('command','a')
print('command a executed')
time.sleep(7)
pyautogui.hotkey('command','c')
print('command c executed ')
time.sleep(7)
pyautogui.hotkey('command','space')
print('command space executed')
time.sleep(7)
pyautogui.hotkey('command','a')
print('command a executed ')
time.sleep(7)
pyautogui.press('backspace')
print('backspace executed')
time.sleep(7)
pyautogui.write("TextEdit")
pyautogui.press('enter')
pyautogui.hotkey('command','v')
pyautogui.hotkey('command','a')
pyautogui.hotkey('command','c')
pyautogui.hotkey('command','space',interval=0.5)
pyautogui.hotkey('command','a')
pyautogui.press('backspace')
pyautogui.write("microsoft word")
pyautogui.press('enter')
pyautogui.hotkey('command','v')
pyautogui.press('enter')



wb.open('https://www.google.com/imghp?hl=EN')

time.sleep(5)
pyautogui.moveTo(x=689,y=445)
pyautogui.click()
time.sleep(5)
pyautogui.write("luigi")
pyautogui.press('enter')
time.sleep(5)
pyautogui.moveTo(x=106,y=411)
pyautogui.rightClick()
pyautogui.moveTo(x=160,y=595)
pyautogui.click()
pyautogui.hotkey('command','space',interval=0.5)
pyautogui.hotkey('command','a')
pyautogui.press('backspace')
pyautogui.write("microsoft word")
pyautogui.press('enter')
pyautogui.hotkey('command','v')






# pyautogui.hotkey('command','space',interval=0.25)








# print("hlw")
# time.sleep(5)
# pyautogui.hotkey('command','space',interval=0.25)
# print('this line was executed ')
# pyautogui.press('backspace ')
# pyautogui.write('microsoft word')
# pyautogui.press('enter')
# time.sleep(5)
# #pyautogui.hotkey('fn','command','right')        #this line is unreliable, sometimes it works sometimes it doesnt , so i ma diabling it , instead for now believing that the user will position the cursor at the end always .
# pyautogui.hotkey('command','v')




# color =(255, 150, 50)
# s= pyautogui.screenshot()
# text_area = pyautogui.locateOnScreen('s.png')
# background_color = pyautogui.pixel(text_area.left, text_area.top)
# for character in text_area:
#     if pyautogui.pixelMatchesColor(character.left, character.top, background_color):
#         pyautogui.moveTo(text_area.left,text_area.top)


#477 230

# import requests
# from bs4 import BeautifulSoup

# Define the URL of the website
# url = "https://chat.openai.com/chat/09cb7d3a-7b15-4e34-a719-4319eda34989"

# Send a GET request to the URL
# response = requests.get(url)
# hml=response.content
# print(hml)

# Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify)
# print(soup.title)
# # Find the first div element with the class name "parent"
# paras=soup.find_all('p')
# print(paras)
# print(soup.find_all('p'))
# # div1 = soup.find('div',{'id': '__next'})
# #
# # div2=div1.find('div',{'class':'overflow-hidden w-full h-full relative'})
# #
# # div3 = div2.find('div',{'class': 'flex h-full flex-1 flex-col md:pl-[260px]'})
# #
# # div4 = div3.find('main',{'class': 'relative h-full w-full transition width flex flex-col overflow-hidden items-stretch flex-1'})
# #
# # div5=div4.find('div',{'class':'flex-1 overflow-hidden'})
# #
# # div6=div5.find('div',{'class ': 'react-scroll-to-bottom--css-xefgf-1n7m0yu'})
# #
# # div7=div6.find('div',{'class:flex flex-col items-center text-sm dark:bg-gray-800'})
# #
# # div8=div7.find('div',{'class':'group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]'})
# #
# # div9= div8.find('div',{'class':'text-base gap-4 md:gap-6 md:max-w-2xl lg:max-w-2xl xl:max-w-3xl p-4 md:py-6 flex lg:px-0 m-auto'})
# #
# # div10=div9.find('div',{'class':'relative flex w-[calc(1oo%-50px)] flex-col gap-1 md:gap-3 lg:w-[calc(100%-115px)]'})
# #
# # div11=div10.find('div',{'class':'flex flex-grow flex-control gap-3'})
# #
# # div12=div11.find('div',{'class:min-h-[20px] flex flex-control items-start gap-4 white space-pre-wrap'})
#
# div13=soup.find('div',{'class':'markdown'})
# # parent_div = soup.find('div', {'class': 'parent'})
#
# # Find the first div element with the class name "child"
# # child_div = parent_div.find('div', {'class': 'child'})
#
# # Find the div element with the class name "aeo"
# # aeo_div = child_div.find('div', {'class': 'aeo'})
#
# # Find all <p> tags inside the aeo_div
# p_tags = div13.find_all('p')
#
# # Concatenate the text content of all <p> tags
# aeo_text = '\n'.join([p.text.strip() for p in p_tags])
#
# # Print the text content of the div element
# print(aeo_text)


