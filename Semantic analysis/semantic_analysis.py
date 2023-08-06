from bs4 import BeautifulSoup
import re
from contextlib2 import suppress

with open('izumlenie.man.contexts.txt', 'r', encoding='windows-1251') as file:
    raw_data = file.read()
data = BeautifulSoup(raw_data).find_all('se')

action = int(input('Выберите нужное действие: поиск по лемме - 1, поиск по тегу - 2, поиск по лемме и тегу - 3, поиск по комбинации тегов - 4\n'))

def action1(lemma):
    contexts = []
    frequency = 0
    file = open(f'lemma.txt', 'w', encoding='windows-1251')
    file.write(f'Искомая лемма - {lemma}\n\n')
    for sent in data:
        for word in sent('w'):
            if word.ana['lex'] == lemma:
                frequency += 1
                sentence = ' '.join([w.text for w in sent])
                sentence = re.sub(" +", " ", sentence)
                contexts.append(sentence)
    counter = 1
    for context in contexts:
        file.write(f'Контекст №{counter}: {context}\n')
        counter += 1
    file.write(f'\nКоличество найденных лемм: {frequency}\n')
    file.close()

def action2(tag):
    frequency = 0
    counter = 1
    file = open(f'tag.txt', 'w', encoding='windows-1251')
    for sent in data:
        for word in sent('w'):
            with suppress(KeyError):
                if tag in str(word.ana['sem']).strip().split():
                    frequency += 1
                    file.write(f'Предложение №{counter}: тег {tag}, лемма {word.text}\n')
        counter += 1
    file.write(f'\nКоличество найденных тегов: {frequency}\n')

def action3(lemma, tag):
    frequency = 0
    counter = 1
    file = open(f'lemma&tag.txt', 'w', encoding='windows-1251')
    for sent in data:
        for word in sent('w'):
            with suppress(KeyError):
                if (word.ana['lex'] == lemma) and (tag in str(word.ana['sem']).strip().split()):
                    frequency += 1
                    file.write(f'Предложение №{counter}: лемма "{lemma}" с тегом {tag}\n')
        counter += 1
    file.write(f'\nКоличество найденных лемм по тегу: {frequency}\n')

def action4(tag1, tag2, tag3):
    frequency = 0
    counter = 1
    file = open(f'lemma&tags.txt', 'w', encoding='windows-1251')
    for sent in data:
        for word in sent('w'):
            with suppress(KeyError):
                if tag1 and tag2 and tag3 in str(word.ana['sem']).strip().split():  
                    frequency += 1
                    lemma = word.ana['lex']
                    file.write(f'Предложение №{counter}: лемма "{lemma}" с тегами {tag1}, {tag2} и {tag3}\n')
        counter += 1
    file.write(f'\nКоличество найденных лемм по тегам: {frequency}\n')


if action == 1:
    lemma = input('Введите лемму: ')
    action1(lemma)

if action == 2:
    tag = input('Введите тег: ')
    action2(tag)

if action == 3:
    lemma = input('Введите лемму: ')
    tag = input('Введите тег: ')
    action3(lemma, tag)

if action == 4:
    tag1 = input('Введите тег №1: ')
    tag2 = input('Введите тег №2: ')
    tag3 = input('Введите тег №3: ')
    action4(tag1, tag2, tag3)
