import requests

from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")

url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e9a01bba99d347d394ebcedec53eecf6"
a = requests.get(url)
b = a.json()
data = (b['articles'])
def newsapp(n):
    v = 1

    if n ==1 :
        for i in data:
            title  = i['title']
            content = i['content']

            print(f"today no {v} headline is {title} and {content}")
            v+=1
    elif n==2:
        v = 1
        for i in data:
            title = i['title']
            content = i['content']

            print(f"today no {v} headline is {title} and {content}")
            speak.Speak(f"today no {v} headline is {title} and {content}")
            v+=1
    else:
        print("please enter valid input ")

n = int(input("enter 1 for only read the news \n "
           "enter 2 for read and listen news :   ".upper()))
newsapp(n)





