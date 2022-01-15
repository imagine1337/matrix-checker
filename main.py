import requests
from colorama import Fore, init #optional, just cool to see the colors, lol
init(autoreset=True)

wordlist='' #set as name of the file with words

words=open(wordlist,'r').readlines()
hits=open('hits.txt','w+')

for name in words:
    req=requests.get(f'http://matrix-client.matrix.org/_matrix/client/r0/register/available?username={name[:-1]}').status_code
    if req==200:
        print(Fore.GREEN + f'[{name[:-1]}] AVAILABLE')
        hits.write(name)
    else:
        print(Fore.RED+f'[{name[:-1]}] STATUS CODE {req}')
