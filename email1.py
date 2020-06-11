import smtplib, ssl

pt = 465  # For SSL or 587 for TLS
sp_ser = "smtp.gmail.com"
smail = "mradusoni@gmail.com"  # Enter your address
remail = "shricharansoni1999@gmail.com"  # Enter receiver address
pwd = input("Type your password and press enter: ")
msg = """\
Subject: Hi
tu bhut bads awala ghadh he
he he he"""

ctxt = ssl.create_default_context()
                         
with smtplib.SMTP_SSL(sp_ser, pt, context=ctxt) as server:
    server.login(smail, pwd)
    server.sendmail(smail, remail, msg)   
