import random
import smtplib
import threading
import os
from contextlib import contextmanager
from dotenv import load_dotenv

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
    while True:
        if verify_code(email):
            print("Verification successful!")
            break  # Exit the loop on success
        choice = input("""  
        1. Send code again  
        2. Change email  

        Choose an option (1 or 2):  
        """)
        if choice == "1":
            continue  # Retry verification
        elif choice == "2":
            email = get_email()
            continue
        else:
            print("Invalid choice. Please select 1 or 2.")


def verify_code(email):
    code = random.randint(10000, 99999)
    send_code(email, code)

    while True:
        try:
            code_2 = int(input("Enter the code from the email: "))
            break  # Valid input, exit loop
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return code == code_2


@log_decorator
def send_code(email, code):
    subject = "Open budget"
    message = f"Your verification code is  {code}."
    t = threading.Thread(target=send_mail, args=(email, subject, message))
    t.start()
    print("Email is sent to the user...")


def send_mail(to_user, subject, message):
    email_content = f"Subject: {subject}\n\n{message}"
    try:
        with smtp_connection() as server:
            server.sendmail(smtp_sender, to_user, email_content)
    except smtplib.SMTPException as e:
        print(f"Failed to send email to {to_user}: {e}")


load_dotenv()

smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))
smtp_sender = os.getenv('SMTP_SENDER')
smtp_password = os.getenv('SMTP_PASSWORD')
