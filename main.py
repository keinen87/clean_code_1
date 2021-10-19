# from pathlib import Path
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.mime.text import MIMEText
# from email.utils import COMMASPACE, formatdate
# from email import encoders


# def send_mail(send_from, send_to, subject, message, files=[],
#               server="localhost", port=587, username='', password='',
#               use_tls=True):
#     """Compose and send email with provided info and attachments.

#     Args:
#         send_from (str): from name
#         send_to (list[str]): to name(s)
#         subject (str): message title
#         message (str): message body
#         files (list[str]): list of file paths to be attached to email
#         server (str): mail server host name
#         port (int): port number
#         username (str): server auth username
#         password (str): server auth password
#         use_tls (bool): use TLS mode
#     """
#     msg = MIMEMultipart()
#     msg['From'] = send_from
#     msg['To'] = COMMASPACE.join(send_to)
#     msg['Date'] = formatdate(localtime=True)
#     msg['Subject'] = subject

#     msg.attach(MIMEText(message))

#     for path in files:
#         part = MIMEBase('application', "octet-stream")
#         with open(path, 'rb') as file:
#             part.set_payload(file.read())
#         encoders.encode_base64(part)
#         part.add_header('Content-Disposition',
#                         'attachment; filename={}'.format(Path(path).name))
#         msg.attach(part)

#     smtp = smtplib.SMTP(server, port)
#     if use_tls:
#         smtp.starttls()
#     smtp.login(username, password)
#     smtp.sendmail(send_from, send_to, msg.as_string())
#     smtp.quit()







import os # импортируем библиотеку os
import smtplib # импортируем библиотеку smtplib для отправки письма
SMTPSERVER = smtplib.SMTP_SSL ('smtp.mail.ru:465') # объявление глобальной константы SMTPSERVER

print ('''
Привет! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.

'''.replace ('%my_name%','Илья').replace ('%website%','dvmn.org'))
#def READFILE():
def READFILE (filename): #объявляем функцию для чтения текста из файла!
    # f = open ('text.txt', 'r')
    with open (filename,'r') as FILE: # открываем файл на чтение
        # text=read ()
        text = FILE.read () # читаем файл


    return text # возвращаем текст из файла
#str1 = str1.replace('%website%', website)
#str1 = str1.replace('%friend_name%', name)
#str1 = str1.replace('%my_name%', my_name)

MYLOGin    = os.environ ['login'] # достаём логин
#MYLOG='example@yandex.ru'
MYPASsword = os.environ ['password'] # достаём пароль

#READFILE()
READFILE ('text.txt')

#From:+\
#To:+\
#Subject:Важно!+\
#Content-Type: text/plain; charset="UTF-8";
LETter=''
# LETter='Работает?'
LETter='\n'+'From: '+ MYLOGin
print ('\n\n\n')
print (LETter)
LETter=LETter+'\n'+'To: '+MYLOGin
print ('\n\n\n')
print (LETter)
# LETter=LETter + LETter + MYLOGin
# LETter=LETter+'\n'+'Subject: '+'Invite'
LETter=LETter+'\n'+'Subject: '+'Invite'
print ('\n\n\n')
print (LETter)
#LETter =LETter+'\nContent-Type: '+'text/plain; charset="UTF-8";'
LETter=LETter+'\nContent-Type: '+'text/plain; charset="UTF-8";'+'\n\n'
print ('\n\n\n')
print (LETter)
LETter1=READFILE ('text.txt') # читаем из файла и кладём в переменную
#READFILE('test_file.txt')
READFILE ('to_replace.txt')
MyName,Website=READFILE ('to_replace.txt').split ('\n') # читаем из файла и распаковываем в переменные
# '\n'.replace ('%my_name%',i).replace ('%website%',j)
LETter1=LETter1.replace ('%my_name%',MyName).replace ('%website%',Website)
print ('\n\n\n')
print (LETter)
LETter=LETter.strip () + '''\
"Привет! %my_name% приглашает тебя на сайт %website%! \n\n%website% — это новая версия онлайн-курса по программированию.  \nИзучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. \n\nКак будет проходить ваше обучение на %website%? \n\n→ Попрактикуешься на реальных кейсах. \nЗадачи от тимлидов со стажем от 10 лет в программировании.\n→ Будешь учиться без стресса и бессонных ночей. \nЗадачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь. \n→ Подготовишь крепкое резюме. \nВсе проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. \n\nРегистрируйся → %website%  \nНа модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.

'''.replace('%my_name%','Илья').replace('%website%','dvmn.org')
print ('\n\n\n')
print (LETter)
LETter=LETter.encode ('utf-8') # кодируем письмо в utf-8
print ('\n\n\n')
print (LETter)



from email.mime.application import MIMEApplication
#from email.mime.application import MIMEApplication as Ma
from email.mime.multipart import MIMEMultipart
#from email.mime.multipart import MIMEMultipart as Mm
from email.mime.text import MIMEText
#from email.mime.text import MIMEText as Mt

# def send_mail(send_from, send_to, subject, text, files=None,
#               server="127.0.0.1"):
#     assert isinstance(send_to, list)

#     msg = MIMEMultipart()
#     msg['From'] = send_from
#     msg['To'] = COMMASPACE.join(send_to)
#     msg['Date'] = formatdate(localtime=True)
#     msg['Subject'] = subject

#     msg.attach(MIMEText(text))

#     for f in files or []:
#         with open(f, "rb") as fil:
#             part = MIMEApplication(
#                 fil.read(),
#                 Name=basename(f)
#             )
#         # After the file is closed
#         part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
#         msg.attach(part)


#     smtp = smtplib.SMTP(server)
#     smtp.sendmail(send_from, send_to, msg.as_string())
#     smtp.close() 





def sendMail(to, subject, text, files=[]):
    assert type(to)==list
    assert type(files)==list

    msg = MIMEMultipart ()
    msg ['From']    = username
    msg ['To']      = COMMASPACE.join(to)
    msg ['Date']    = formatdate(localtime=True)
    msg ['Subject'] = subject

    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase ('application', "octet-stream")
        part.set_payload ( open(file,"rb").read() )
        Encoders.encode_base64 (part)
        part.add_header ('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach (part)

#smtplib.SMTP_SSL ('smtp.yandex.com:465')
SERVER = smtplib.SMTP_SSL ('smtp.yandex.com:465') # инициализируем сервер
# SERVER
SERVER.login (MYLOGin,MYPASsword) # логинимся на сервер
#SERVER.sendmail
SERVER.sendmail (MYLOGin,MYLOGin,LETter) # отправляем письмо
SERVER.quit () # выход
print ('Письмо отправлено!')
