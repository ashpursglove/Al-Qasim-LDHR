import time
from datetime import datetime, timedelta
import csv
from time import gmtime, strftime
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_from = "rsfsmtp@gmail.com" # use the RSFSMTP email here
pswd = "RSF2020!"



subject = "TEST Critical Error at Al-Qasim Site TEST"






def email_error(email, err_msg):
    
    
    
    body = "This message was auto generated (by Ash's awesome code!!), Please don't reply to this.\n\n\nThere has been an unexpected error on site. Please contact on site personnel to try a manual restart immediately\n\n\n Error is: "+err_msg +"\n\n\n\nAll code written by Ashley Purslgove\nCopyright 'Red Sea Farms' 2020"

    
    
    email_to = email

        



# formatting and sending email
    
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
#     filename= cur_filename +'.csv'
# 
#     attachment=open(filename,'rb')
#     
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload((attachment).read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', "attachment; filename= "+filename)
# 
#     msg.attach(part)


    text = msg.as_string()


    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_from, pswd)
    
    server.sendmail(email_from ,email_to, text)
    server.quit()

    print ("email sent to %s" %(email))
        
