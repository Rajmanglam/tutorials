# so in this video we will learn about uses of requests module
import requests
r=requests.get('http://ecare.franciscanecare.com/Panel/Inbox')#this will get the code of
#the url
print(r.text)
'''# let's learn about post requests now
# rt=('www.something.com')
# data=[55,6798,'hj']
# r2=requests.post(url=rt,data=data)'''
#let's learn about status code now
print(r.status_code)#this will give us our status code
