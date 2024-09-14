import random
import smtplib
import threading
from contextlib import contextmanager

from logs.logs import log_decorator
from utils.common import get_email


@contextmanager
def smtp_connection():
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_sender, smtp_password)
    yield server
    server.quit()


def verify_code_menu(email):
    if not verify_code(email):
        choice = input("""
        1. Send code again
        2. Change email

        Choice an option:  
        """)

        if choice == "1":
            verify_code_menu(email)
        if choice == "2":
            email = get_email()
            verify_code_menu(email)


def verify_code(email):
    code = random.randint(10000, 99999)
    send_code(email, code)
    code_2 = int(input("Enter code from email:  "))
    if code == code_2:
        return True
    return False


@log_decorator
def send_code(email, code):
    subject = "Verify The Code:"
    t = threading.Thread(target=send_mail, args=(email, subject, code))
    t.start()
    print(f"Email is sent to user")


def send_mail(to_user, subject, message):
    email_content = f"Subject: {subject}\n\n{message}"
    try:
        with smtp_connection() as server:
            server.sendmail(smtp_sender, to_user, email_content)
    except smtplib.SMTPException as e:
        print(f"Failed to send email to {to_user}: {e}")



smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_sender = 'rano.baxromovna@gmail.com'
smtp_password = 'iwnd wsls azqg bphk'
