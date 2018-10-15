import os, sys
import ipaddress
import subprocess

onlineMakinalar = []
offlineMakinalar = []
addr = ''


#Adresi Al
def getAddres():
  print("Ana host adresini - host numarasını koymadan girin")
  global addr
  addr = input("Ağınız > ")

#İp adresini kontrol et
def ipDogrula(i):
  v = i + '.1'
  ipaddress.ip_address(v) #adresi dogrula

#Sweep işlemini başlat
def pingSweep(network):
  for i in range(1, 255):
    result = str.join('.', (addr, str(i)))
    durumKontrol(result)

#Makinaları tara
def durumKontrol(a):
  print("kontorl ediliyor: %s" % a)
  if os.system("ping %s -n 1 -w 10" % a) == 0:
    onlineMakinalar.append(a)
  else:
    offlineMakinalar.append(a)

#Sonucu yazdır
def sonuc():
  print("\nhost Ayakta")
  print("*" * 20)
  for i in onlineMakinalar:
    print(i)

  print("\nHost kapalı")
  print("*" * 20)
  for i in offlineMakinalar:
    print(i)

def main():
  getAddres()
  ipDogrula(addr)
  pingSweep(addr)
  sonuc()


if __name__ == '__main__':

    main()