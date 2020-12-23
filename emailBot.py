import groceryList
import smtplib

#s = smtplib.SMTP('smtp.gmail.com', 587)
#s.starttls()
#s.ehlo()
#s.login('fsjhkfiovh@gmail.com', 'roottootandyoot773') #fill in later
#text = """Test test TEST

#-hayley
#"""
#msg = email.message.EmailMessage()
#msg['from'] = 'fsjhkfiovh@gmail.com'
#msg["to"] = 'haleydaisyhill@gmail.com'
#msg["Subject"] = "Re: TEST!!! "
#msg.set_content(text)
#res = s.send_message(msg)

gl = groceryList.GroceryList()
sender = "fsjhkfiovh@gmail.com"
receiver = ["haleydaisyhill@gmail.com"]
password = "roottootandyoot773"
message = str(gl.showList())

session = smtplib.SMTP('smtp.gmail.com',587)
session.ehlo()
session.starttls()
session.ehlo()
session.login(sender,password)
session.sendmail(sender,receiver,message)
session.quit()