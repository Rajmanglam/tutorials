import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("welcome here comes the news for you")
    url="https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=3451db45e74b4d2c9b3b34cfab3bddfa"
    k=requests.get(url).text
    k_dict=json.loads(k)
    arts=k_dict['articles']
    for articles in arts:
        speak(articles['title'])
        print(articles['title'])
        speak("Moving on to the next news..Listen Carefully")
    speak("thanks for listening")


