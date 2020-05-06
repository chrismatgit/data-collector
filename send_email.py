from email.mime.text import MIMEText
import smtplib


def send_email(email, height):
    ''' Send email function with 2 @param (email, height)'''
    # make sure you the 'Allow less secure apps' in your gmail account
    from_email = "youremail@gmail.com"  # put your correct email address here
    from_password = "yourpassword"  # put your correct password
    to_email = email  # get the mail from  the input form

    # Message to be displayed
    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>." % height

    # setting up the header of the email
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    # login into your account
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
