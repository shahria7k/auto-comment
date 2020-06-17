import pyautogui
import time


comments = ["hi"," Logigtech is awesomome"," checking my python comment bot"," Pyhton is  awesome"," I am a messy proggramer", "i am just checking my python skill",]

time.sleep(10)
for i in range(1000):
    pyautogui.typewrite(comments[i%6])
    pyautogui.typewrite("\n")
    time.sleep(0.5)
    #this is a comment
