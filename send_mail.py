# from smtplib import SMTP
import smtplib
from email import message
from settings import mail_address, app_password as mail_password, to_address


def send_mail(title='test mail title(default)', description='test'):
    smtp_host = 'smtp.gmail.com'  # メールサーバ
    smtp_port = 587  # メールサーバのポート
    from_email = mail_address
    to_email = to_address
    username = from_email
    password = mail_password

    # 送信メールの作成
    msg = message.EmailMessage()
    msg.set_content(description)
    msg['Subject'] = title
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP(smtp_host, smtp_port) as smtpobj:
        smtpobj.starttls()
        smtpobj.login(username, password)
        smtpobj.send_message(msg)


if __name__ == '__main__':
    # send_mail()
    pass
