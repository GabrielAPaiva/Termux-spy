import requests
import re, os , time
import subprocess as sp

neg = '\033[1m';cl= '\033[0;0m';red= '\033[31m';green = '\033[32m'
blue = '\033[34m';cian = '\033[36m';mag = '\033[35m'

global bus,url,link

print(cian+' _______                                 \n(_______)                      _         \n _  _  _  _____   ____  ___  _| |_  ___  \n| ||_|| |(____ | / ___)/ _ \\(_   _)/ _ \\ \n| |   | |/ ___ || |   | |_| | | |_| |_| |\n|_|   |_|\\_____||_|    \\___/   \\__)\\___/ \n                                         \n'+cl)
print(neg+"*Copie o link da página com as respostas no site Dontpad e clique enter,\nnão é necessário colar.\nO formato das respostas deverá seguir o modelo:\n\t[respostas a b c d e ]\n"+cl)
print(mag+'{:_^45}'.format('dev_kailp*may18'))
status, link = sp.getstatusoutput("termux-clipboard-get")
w = input("Tecle Enter")
url = requests.get(link)
def vibrate(x):
    for i in range(x):
        os.system("termux-vibrate -d 100 -f")

def pes(x):
    bus = re.findall(r'id="text">respostas(.*)</textarea>\n\t\t</div>\n\t\t\n\t\t<input',x)
    return bus
def chec(x):
    while not x:
        url = requests.get(link)
        print(red+"Escutando..."+cl)
        os.system("clear")
        x = re.findall(r'id="text">respostas(.*)</textarea>\n\t\t</div>\n\t\t\n\t\t<input',url.text)
    else:
        print(green+"Lendo"+cl)
        time.sleep(2)
        os.system("termux-vibrate -d 300 -f")
        time.sleep(2)
        x = str(x[0])
        x = x.split()
        for i in x[:]:
            time.sleep(2)
            if i == 'a':
                vibrate(1)
            if i == 'b':
                vibrate(2)
            if i == 'c':
                vibrate(3)
            if i == 'd':
                vibrate(4)
            if i == 'e':
                vibrate(5)

for i in range(3):
    chec(pes(url.text))
