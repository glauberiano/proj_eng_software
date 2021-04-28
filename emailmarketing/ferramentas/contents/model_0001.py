import smtplib

def send_email(subject, email_body):
    sender_email = "email.marketing.grupo2@gmail.com"
    password = "grupodois"
    receiver_email = ["lucas.mazim9@gmail.com","fabiiegawa@hotmail.com","leonardolcruz08@gmail.com"]
    message = 'Subject: {}\n\n{}'.format(subject, email_body)


    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls() 
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        # print('Successfully sent!')
    except Exception as exc:
        print(exc)
    return