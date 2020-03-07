#!/usr/bin/python3

from os import mkdir
from os.path import isdir
from shutil import rmtree
import random as rd
from string import ascii_letters, digits
from solution import search_fruit

TEST_COUNT = 50
TEST_PATH = 'tests'
ANSWER_PATH = 'tests'
SAMPLES_PATH = 'tests'

SAMPLES = [
    'Дуриан',
    'Личи'
]

SHOPS = {
    "Шестёрочка": {
        "Консервы": [
            "Ананасы кусочками",
            "Ананасы колечками"
        ],
        "Сухофрукты": [
            "Тропические ананасы",
            "Дуриан вяленый"
        ],
        "Фрукты": [
            "Бананы",
            "Манго"
        ]
    },
    "Микси": {
        "Овощи-фрукты": [
            "Яблоки",
            "Груши",
            "Личи"
        ]
    }
}
MOLLS = ['Вега', 'Альдебаран', 'Альтаир', 'Верёвка', 'Светофор', 'Всё', 'Облако',
         'Еда', 'Руккола']

DEPARTMENTS = ['Фруктики', 'Здоровое питание', 'Консервы', 'Соки и фрукты', 'Фрукты-Овощи',
               'Сухофрукты', 'Бакалея', 'Для здоровья', 'Фитнес-еда']

GOODS = ['Яблоки сушеные', 'Груши конференс', 'Яблоки Гала', 'Киви', 'Папайя',
         'Бананы', 'Айва', 'Хурма', 'Инжир вяленый', 'Айва японская', 'Виноград сушеный',
         'Гранатовый сок', "Яблоки", "Груши", "Личи", "Ананасы кусочками",
         "Ананасы колечками", "Тропические ананасы", "Дуриан вяленый"]

FRUITS = ['Яблоки', 'Груши', 'Киви', 'Папайя',
          'Бананы', 'Айва', 'Хурма', 'Инжир', 'Виноград сушеный',
          'Гранат', "Личи", "Ананасы", "Дуриан", 'Манго', 'Клубника']


def main():
    if isdir(TEST_PATH):
        rmtree(TEST_PATH)
    mkdir(TEST_PATH)
    if ANSWER_PATH != TEST_PATH:
        if isdir(ANSWER_PATH):
            rmtree(ANSWER_PATH)
        mkdir(ANSWER_PATH)
    if SAMPLES_PATH != TEST_PATH:
        if isdir(SAMPLES_PATH):
            rmtree(SAMPLES_PATH)
        mkdir(SAMPLES_PATH)
    make_samples()
    for test_number in range(TEST_COUNT):
        make_test(test_number)


def make_samples():
    for index, sample in enumerate(SAMPLES):
        test_file_name = f'./{SAMPLES_PATH}/sample{index + 1:02}'
        answer_file_name = f'./{ANSWER_PATH}/sample{index + 1:02}.a'

        with open(test_file_name, 'w', encoding='utf8') as test_stream:
            line = f'shops = {SHOPS}\n' \
                   f'fruit = "{sample}"\n' \
                   f'print(*search_fruit(shops, fruit))'
            print(line, file=test_stream)

        with open(answer_file_name, 'w', encoding='utf8') as answer_stream:
            print('\n'.join([' '.join(map(str, x)) for x in search_fruit(SHOPS, sample)]), sep='\n', file=answer_stream)

        print(f'Sample {index + 1} [OK]')


def make_test(test_number):
    test_file_name = f'./{TEST_PATH}/{test_number + 1:02}'
    answer_file_name = f'./{ANSWER_PATH}/{test_number + 1:02}.a'

    input_data = make_input_data()
    output_data = make_output_data(input_data[0], input_data[1])

    with open(test_file_name, 'w', encoding='utf8') as test_stream:
        print(input_data[-1], file=test_stream)

    with open(answer_file_name, 'w', encoding='utf8') as answer_stream:
        print('\n'.join([' '.join(map(str, x)) for x in output_data]), file=answer_stream)

    print(f'Test {test_number + 1} [OK]')


def make_input_data():
    shops = {rd.choice(MOLLS): {rd.choice(DEPARTMENTS): [rd.choice(GOODS)
                                                         for k in range(rd.randrange(3, 7))]
                                for j in range(rd.randrange(2, 5))}
             for i in range(rd.randrange(1, 5))}

    fruit = rd.choice(FRUITS)
    input_data = f'shops = {shops}\n' \
                 f'fruit = "{fruit}"\n' \
                 f'print(*search_fruit(shops, fruit))'
    return shops, fruit, input_data


def make_output_data(first, second):
    return search_fruit(first, second)


if __name__ == '__main__':
    main()
