import groceryList
import smtplib

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