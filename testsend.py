import smtplib, ssl

def send_email(message_to_send):
    try:
        host = 'smtp.gmail.com'
        port = 465

        username = "ongkitwei@gmail.com"
        password = ""

        receiver = "ongkw2003@yahoo.com.sg"
        context = ssl.create_default_context()

        message = message_to_send

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
            print("email sent")

    except Exception as e:
        print("An error occurred:", str(e))

