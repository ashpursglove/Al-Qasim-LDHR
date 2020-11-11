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

email_to = "ashley.pursglove@redseafarms.com" # Email that message will be to be sent to
#email_to = "alba.luna@redseafarms.com" # Email that message will be to be sent to
#email_to = "catherine.decastro@kaust.edu.sa" # Email that message will be to be sent to


subject = "Data from RSF Pi Al Qasim Site"
body = "This message was auto generated (by Ash's awesome code!!), Please don't reply to this.\n\n\n\n\n\nAll code written by Ashley Purslgove\nCopyright 'Red Sea Farms' 2020"




  

def autolog(data_is_logging,ndl, cur_filename, dli, data_arr, no_tank_changes, cooling):
    
    
    if datetime.now() >= ndl: #chesks time now against when next data log time is
        
        ashs_file = open(cur_filename+'.csv','+a',  newline='')
        
        with ashs_file as csvfile:            
            ashs_writer = csv.writer(csvfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            
            
            if data_is_logging == False:
                
                ashs_writer.writerow(['Time'] + ['Inside Temperature']+ ['Inside Humidity']+['Outside Temperature']+ ['Outside Humidity']+
                                     ['Other Temperature']+ ['Other Humidity']+ ['No of Tank Switchs']+ ['Cooling On/Off'])
                
                data_is_logging = True
                
                
                
            if data_is_logging == True:
              
                
                ashs_writer.writerow([str(datetime.now()),"%.1f" %(data_arr[0]),"%.1f" %(data_arr[1]),"%.1f" %(data_arr[2]),"%.1f" %(data_arr[3]),"%.1f" %(data_arr[4]),"%.1f" %(data_arr[5]),no_tank_changes, cooling])
                
                ndl = datetime.now()+ timedelta(minutes = dli) #sets time limit until next data log
                
        ashs_file.close()
        
        
        

    return ndl, data_is_logging
       
       
       
       
       
       
       
       
       
       
       
    
def autosend(session_length, session_start, following_session, data_is_logging,cur_filename):
    
    if datetime.now() >= following_session:
        
    
        ''' formatting and sending email'''
        
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        filename= cur_filename +'.csv'

        attachment=open(filename,'rb')
        
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= "+filename)

        msg.attach(part)


        text = msg.as_string()


        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_from, pswd)
        
        server.sendmail(email_from ,email_to, text)
        server.quit()

        print ("email sent")
        





        ''' Final house keeping'''
        data_is_logging = False
        session_start = datetime.now()
        following_session = session_start + timedelta(minutes = session_length)
        
    
    
    return data_is_logging, session_start, following_session
        





