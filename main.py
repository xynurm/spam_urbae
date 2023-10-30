import pyautogui, time, random

time.sleep(6)
f=open("wordlist.txt",'r')

for word in f:
    time.sleep(2)
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(5)