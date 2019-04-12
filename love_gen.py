# load the list of positive adjectives
import pandas as pd
import random
import datetime
import inflect
import smtplib

# load the positive words index
positive = pd.read_csv('positive.csv')
nouns = pd.read_csv('brown_nouns.csv')
adjs = pd.read_csv('brown_adj.csv')
# set index to word
positive.set_index('word',inplace=True)
nouns.set_index('word',inplace=True)
adjs.set_index('word',inplace=True)
thetime = datetime.time()

def get_random_noun():
    """returns a random noun"""
    while True:
        return random.choice(nouns.index)

def get_pos_adj():
    """returns a random positive adjective"""
    while True:
        word = random.choice(adjs.index)
        if word in positive.index:
            if positive.loc[word,'sentiment']=='positive':
                return word

def send_love_letter(to_who,from_who,to_email):
    # load the inflect engine
    p = inflect.engine()

    # get some nouns and adjectives
    adj1 = get_pos_adj()
    adj2 = get_pos_adj()
    noun1 = get_random_noun()
    noun2 = get_random_noun()
    noun3 = get_random_noun()

    introductions = ['Dear {}'.format(to_who),'My dear {} partner.'.format(adj1),'To the most {} partner in my life.'.format(adj1)]
    superlative = ['very, extremely','most','quite']
    middle = 'I just want to let you know that you are {} {}.'.format(random.choice(superlative),adj2)
    n1=p.a(get_random_noun())
    n2=p.plural(noun3)
    ending='You are more important to me than {}, and even some {}.'.format(n1,n2)
    signature = 'Sincerely, {}'.format(from_who)

    letter = '{}\n {}\n {}\n {}'.format(random.choice(introductions),middle,ending,signature)
    print(letter)

    d = datetime.datetime.now()

    subject = 'Love letter written {}/{}'.format(d.month,d.day)
    print(subject)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #Next, log in to the server
    # get login details from file
    with open('gmail_login.txt') as file:
        user = file.readline().strip()
        password = file.readline().strip()

    server.login(user,password)


    #Send the mail
    msg = 'Subject:{}\n{}'.format(subject,letter)
    server.sendmail("emil.shivan@gmail.com",to_email, msg)
