import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

FROM = os.getenv('FROM')
TO = os.getenv('TO')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


friend_name = 'Артур'
my_name = 'Игорь'
website = 'https://dvmn.org/profession-ref-program/lanin.igor/Mepje/'
sender = FROM
receiver = TO
subject = 'Приглашение!'
content_type = 'text/plain; charset="UTF-8";'


letter = """\
From: {sender}
To: {receiver}
Subject: {subject}
Content-Type: {content_type}

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""" .format(
	friend_name=friend_name, my_name=my_name, website=website, sender=sender, receiver=receiver, subject=subject, content_type=content_type)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(LOGIN, PASSWORD)
server.sendmail(FROM, TO, letter)
server.quit()