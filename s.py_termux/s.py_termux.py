__Author__="Kaio Fábio Prates"
import os
import time
#colors
neg = '\033[1m';cl= '\033[0;0m';red= '\033[31m';green = '\033[32m'
blue = '\033[34m';cian = '\033[36m';mag = '\033[35m'
#take a picture
def photo(x,c):
    hor = time.strftime('%H:%M:%S')
    hor = hor.replace(":","")
    hor = hor+".jpg"
    time.sleep(x)
    os.system("termux-camera-photo -c 0 "+hor)
    if (c == 'y' or c == "Y"):
        os.system("termux-vibrate -d 300 -f")
    print(neg+"SUCESS"+cl)
#number of photos
def tempo(y,x,c):
    for i in range(y):
        photo(x,c)
tela = " ____                              \n/\\  _`\\                            \n\\ \\,\\L\\_\\       _____    __  __    \n \\/_\\__ \\      /\\ '__`\\ /\\ \\/\\ \\   \n   /\\ \\L\\ \\  __\\ \\ \\L\\ \\\\ \\ \\_\\ \\  \n   \\ `\\____\\/\\_\\\\ \\ ,__/ \\/`____ \\ \n    \\/_____/\\/_/ \\ \\ \\/   `/___/> \\\n                  \\ \\_\\      /\\___/\n                   \\/_/      \\/__/ \n"
print(cian+neg+tela+cl)
print(mag+'{:_^45}'.format('dev_kailp*may18'))
f = int(input(blue+"\nNúmero de fotos: "+cl))
t = int(input(blue+"\nIntervalo de tempo, em segundos: "+cl))
c = input(blue+"\nVibrar [y/n]: "+cl)
print(green+"TEMPO TOTAL: "+cian+"{} segundos".format(f*t))
tempo(f,t,c)
