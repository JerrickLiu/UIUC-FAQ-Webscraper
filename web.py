from bs4 import BeautifulSoup
import requests
import os
import smtplib
from email.mime.text import MIMEText

url = "https://covid19.illinois.edu/frequently-asked-questions/"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='post-23')

questions = results.find_all('summary', class_="ab-accordion-title")

num_questions = len(questions)

save_path = '/Users/SirJerrick/Desktop/webscraper/scraping_data/'


file = open(save_path + "number_of_questions.txt", 'r')

if num_questions > int(file.read()):

    new_file = open(save_path + "number_of_questions.txt", "w")

    new_file.write(str(num_questions))

    new_file.close()

    new_question = questions[-1].text

    sender = 'jerrick.y.liu@gmail.com'

    receiver = 'jerrick.y.liu@gmail.com'

    body_of_email = new_question

    msg = MIMEText(body_of_email + " Go to https://covid19.illinois.edu/frequently-asked-questions/ to view the answer!")
    msg['Subject'] = "New question in UIUC FAQ!"
    msg['From'] = sender
    msg['To'] = receiver

    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port = 465)
    s.login(user='jerrick.y.liu@gmail.com', password ='Jerrick100')
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

