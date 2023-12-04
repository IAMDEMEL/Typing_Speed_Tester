from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from _csv import writer
import pandas as pd
import requests
import random
import string


def grab_paragraph_of_the_web(amount_to_grab=3):
    readable_paragraph = ''
    for i in range(amount_to_grab):
        website = 'https://randomword.com/paragraph'
        response = requests.get(website)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraph = soup.find_all(id="random_word_definition")[0]
        readable_paragraph += paragraph.text
        if amount_to_grab > 1 and i < amount_to_grab - 1:
            readable_paragraph += '\n\n'
    return readable_paragraph


class Brain:
    def __init__(self):
        self.countdown = 0
        self.characters_in_word = 0
        self.words_in_sentence = 0
        self.current_sentence = ''
        self.sentences_in_paragraph = 0
        self.paragraphs = None
        self.readable_paragraphs = ''

    def generate_random_paragraph(self):
        self.paragraphs = random.randint(1, 4)

        for paragraph in range(self.paragraphs):
            self.sentences_in_paragraph = random.randint(4, 8)

            for sentence in range(self.sentences_in_paragraph):
                short_sentence_length = 10
                self.words_in_sentence = random.randint(3, 19)
                if self.words_in_sentence >= short_sentence_length:
                    self.countdown = random.randint(3, self.words_in_sentence - 3)

                for word in range(self.words_in_sentence):
                    self.characters_in_word = random.randint(1, 12)

                    if self.words_in_sentence >= short_sentence_length:
                        if self.countdown > 0:
                            self.countdown -= 1
                            if self.countdown == 0:
                                structuring_list = [',', ';']
                                self.current_sentence += random.choice(structuring_list)
                    self.current_sentence += ' '

                    while self.characters_in_word > 1:
                        self.characters_in_word -= 1
                        self.current_sentence += random.choice(string.ascii_lowercase)

                while self.current_sentence[0] == ' ':
                    self.current_sentence = self.current_sentence[1:]

                self.current_sentence += '. '
                self.readable_paragraphs += self.current_sentence.capitalize()
                self.current_sentence = ''

            self.readable_paragraphs += '\n\n'

        return self.readable_paragraphs

    def generate_normal_paragraph(self):
        try:
            file = open("List of paragraphs/Normal Paragraphs.csv", "r")
            file.close()
            try:
                with open("List of paragraphs/Normal Paragraphs.csv", "a") as file:
                    self.paragraphs = [grab_paragraph_of_the_web(random.randint(1, 5))]
                    writer_object = writer(file)
                    writer_object.writerow(self.paragraphs)
                    file.close()
                return self.paragraphs[0]
            except ConnectionError:
                df = pd.read_csv('List of paragraphs/Normal Paragraphs.csv')
                self.paragraphs = df['Paragraph'].to_list()

                if len(self.paragraphs) >= 5:
                    return random.choice(self.paragraphs)
                else:
                    df = pd.read_csv('List of paragraphs/No Internet Paragraphs.csv')
                    self.paragraphs = df['Paragraph'].to_list()
                    return random.choice(self.paragraphs)

        except FileNotFoundError:
            try:
                self.paragraphs = grab_paragraph_of_the_web(random.randint(1, 5))
                df = pd.DataFrame({'Paragraph': [self.paragraphs]}, index=[0])
                df.to_csv('List of paragraphs/Normal Paragraphs.csv', mode='a', index=False)
                return self.paragraphs
            except ConnectionError:
                df = pd.read_csv('List of paragraphs/No Internet Paragraphs.csv')
                self.paragraphs = df['Paragraph'].to_list()
                return random.choice(self.paragraphs)
