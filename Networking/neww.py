from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
#from email.MIMEaudio import MIMEAudio
import smtplib

user="root"
passw="1234"

username=raw_input("Username: ")
password=raw_input("Password: ")

if user==username and passw==password:
        
    msg = MIMEMultipart()
    msg.attach(MIMEText(file("mm.txt").read()))
    msg.attach(MIMEImage(file("new.jpg").read()))
    #msg.attach(MIMEAudio(file("song.mp3").read()))

    # to send
    server = smtplib.SMTP('127.0.0.1', 1025)
    print "ready to send"
    server.set_debuglevel(True) # show communication with the server
    try:
        server.sendmail('author@example.com', ['recipient@example.com'], msg.as_string())
    finally:
        server.quit()

else:
    print "Username and password does not mach!!!"
    
