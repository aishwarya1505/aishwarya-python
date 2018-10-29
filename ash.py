import smtplib
import getpass
myemail=input("your email id:")
password=getpass.getpass()
recemail=input("reciver's email id:")
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(myemail,password)
message= "hi how are you"
s.sendmail(mymail,recemail,message)
s.quit()

output-------------------------------------
your email id:aaishwarya598@gmail.com
Password: 
reciver's email id:aaishwarya598@gmail.com
