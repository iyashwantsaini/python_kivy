import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header=figlet_format('JOKES')
header=colored(header,color='magenta')
print(header)

user_input=input('Enter the topic for the joke : ')
url='https://icanhazdadjoke.com/search'
req=requests.get(
    url,
    headers={'Accept':'application/json'},
    params={'term':user_input}
).json()


num_jokes=req['total_jokes']
results=req['results']

if(num_jokes>1):
    print(choice(results)['joke'])
elif(num_jokes==1):
    print(results[0]['joke'])
else:
    print('joke not found :(')
