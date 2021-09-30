from typing import Text
import pafy #library yt
from termcolor import colored,cprint #library color
#print_green = lambda x: cprint(x,'green')
#print_green(" Tools ZaydanM")

from pyfiglet import Figlet #library font
# f = Figlet(font = 'banner3-D')
# print(f.renderText('Tools ZaydanM'))

f= Figlet(font='banner3-D')
print(colored(f.renderText('Tools ZaydanM'),('green')))

print(" [1] Download Video YT")
print(" [2] Encrypt (coming soon)")
print(" [3] Decrypt (coming soon)")
pilih = input(" Pilih : ")

if (pilih == "1"):
    f= Figlet(font='banner3')
    print(colored(f.renderText('Selamat Datang'),('red')))
    link = input(" Masukkan Link : ")
    url = pafy.new(link)
    print(url.title)
    hasil = url.getbest()
    hasil.download()
elif (pilih == "2"):
    print("Maaf, fitur akan segera datang")
elif (pilih == "3"):
    print("Maaf, fitur akan segera datang")
else:
    print(" Maaf")


