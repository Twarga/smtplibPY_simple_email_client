import smtplib
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587 )
server.starttls()

server.login("youremail@gmail.com", "Yourpassword")

msg = MIMEText("This is the body of the email")
msg['From'] = "youremail@gmail.com"
msg['To'] = "recipent@gmail.com"
msg['Subject'] = "Subject of the email"

server.sendmail("youremail@gmail.com" ,"recipent@gmail.com" , msg.as_string())

server.quit()

