import email,smtplib,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "an email with attachment from python"
body = "this is an email with attachment sent from python"

sender_email = "mradusoni@gmail.com"
receiver_email = "shricharankantsoni1999@gmail.com"
password = input("type your password and press enter")

#create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email # recommmended for mass emails

#add body to email
message.attach(MIMEText(body, "plain"))

filenm = "attach.txt" #in same directory as script


 #open PDF file in binary mode
with open(filenm, "rb")as att:
    #add file as application /octet-stream
    #email cleint can usually download this automaticallyas attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(att.read())

#encode file in ASCII characters to sendby email
encoders.encode_base64(part)

#add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment: filename = {filenm}",
    )
#add attachment to message and convert message to string
message.attach(part)

#log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

         
