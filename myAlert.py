# AUTHOR : NIROSHIMAN BALASUBRAMANIAM
# DECRIP : Function to send the related news or stock alert via email
#          Documentation at https://newsapi.org/docs/endpoints/everything
# BRANCH : 02

import smtplib

def send_email():

    # creating an object from SMTP class, connect to the email provider
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # tls secures our connection to the email server, encrypts it
        connection.login(user=login_details["my_email"], password=login_details["email_password"])
        connection.sendmail(from_addr=login_details["my_email"], # sender's email
                            to_addrs=login_details["my_email"], # receiver's email
                            msg="Subject:Hello\n\nThis is the body"
                            )
        # connection.close() - no need to use this when using with, will close automatically
