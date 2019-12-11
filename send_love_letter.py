import datetime
import smtplib

from generate_love_letter import generate_love_letter

def send_love_letter(letter,to_who,from_who):

    d = datetime.datetime.now()

    subject = 'Love letter written {}/{}'.format(d.month,d.day)
    print(subject)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #Next, log in to the server
    # get login details from file

    # put your login in a text file or any more secure vessel
    with open('gmail_login.txt') as file:
        user = file.readline().strip()
        password = file.readline().strip()

    server.login(user,password)


    #Send the mail
    msg = 'Subject:{}\n{}'.format(subject,letter)
    server.sendmail("email@email.com",to_who, msg)
