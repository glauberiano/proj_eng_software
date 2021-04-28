import smtplib, ssl

import codecs
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(name, emails, htmlp):
    #htmlp = "content_0002.html"
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "email.marketing.grupo2@gmail.com"
    password = "grupodois"
    receiver_email = emails

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Preparados para a aventura, Capitão?"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    
    # Create the body of the message (a plain-text and an HTML version).
    text = "Se falhar, este e-mail será enviado."
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)
    
    # lendo arquivo HTML como texto
    f=codecs.open(htmlp, 'r')
    soup = BeautifulSoup(f.read(), 'html.parser').prettify()
    html = soup.replace("VARIABLE_NAME", name)
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    
    # Try to log in to server and send email
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 