import smtplib
from email.mime.text import MIMEText

def Pass_Email(Mname,Dict):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login("sun98390123@gmail.com","nlxcotsiwztvmhqu")

    SendString = "산 이름은 " + Mname + "\n"

    for Key, Value in Dict.items():
        if Key == '대중교통':
            '''
            if Value:
                SendString += "대중교통은" + "\n"
                for Key1,Value2 in Value:'''
            pass
        else :
            SendString += Key + "은 " + Value + "\n"


    msg = MIMEText(SendString)
    msg['Subject'] = '제목: 파이썬으로 gmail 보내기'

    smtp.sendmail('sun98390123@gmail.com', 'sun98390123@gmail.com', msg.as_string())

    smtp.quit()


