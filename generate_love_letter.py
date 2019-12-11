import inflect
import random
import datetime
import pandas as pd

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

p = inflect.engine()

# get some nouns and adjectives
adj1 = get_pos_adj()
adj2 = get_pos_adj()
noun1 = get_random_noun()
noun2 = get_random_noun()
noun3 = get_random_noun()

def generate_love_letter(to_who,from_who):
    introductions = ['Dear {}'.format(to_who), 'My dear {} partner.'.format(adj1),
                     'To the most {} partner in my life.'.format(adj1)]
    superlative = ['very, extremely', 'most', 'quite']
    middle = 'I just want to let you know that you are {} {}.'.format(random.choice(superlative), adj2)
    n1 = p.a(get_random_noun())
    n2 = p.plural(noun3)
    ending = 'You are more important to me than {}, and even some {}.'.format(n1, n2)
    signature = 'Sincerely, {}'.format(from_who)

    letter = '{}\n {}\n {}\n {}'.format(random.choice(introductions), middle, ending, signature)
    return letter