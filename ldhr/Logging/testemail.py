import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_from = "rsfsmtp@gmail.com" # use the RSFSMTP email here
email_to = "rsfsmtp@gmail.com" # Email that message will be to be sent to


subject = "message from RSF Pi"

msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = subject


body = "main body of text I assume"


msg.attach(MIMEText(body, 'plain'))



filename='info.csv'
attachment=open(filename,'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= "+filename)

msg.attach(part)


text = msg.as_string()


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_from,'RSF2020!')

#message = "beijinhos fofa2"

server.sendmail(email_from ,email_to, text)
server.quit()

print ("email sent")
