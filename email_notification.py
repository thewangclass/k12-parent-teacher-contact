import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import time
from dotenv import load_dotenv

load_dotenv()

letter_path = f"messages/first-message-nine-weeks.txt"
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
FROM_EMAIL = os.getenv('FROM_EMAIL')


def get_message(student_data, *letter_choosing_criteria):
    with open(letter_path) as letter_file:
        contents = letter_file.read()
        return format_message(student_data, contents)


def format_message(student_data, message):
    message = message.replace("[STUDENT_NAME]", student_data.student_name.split()[0])
    message = message.replace("[GRADE_AVERAGE]", f"{student_data.grade_average}")
    message = message.replace("[PARENT_NAME]", student_data.guardian_name.split()[0])
    return message


def email_parent(student_data):
    print(f"Send email to {student_data.student_name}'s parent, {student_data.guardian_name}")
    message = get_message(student_data)
    print(message)
    time.sleep(10)
    send_mail(send_from=FROM_EMAIL,
              send_to=[student_data.student_Email, student_data.guardian_email, FROM_EMAIL],
              subject=f'Computer Science: 3rd Nine Weeks {student_data.student_name}',
              message=message,
              )
    print("success!")


def send_mail(send_from, send_to, subject, message, files=[],
              server="smtp.gmail.com", port=587, use_tls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ", ".join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
