#!/usr/bin/python3
from os import mkdir
from os.path import isdir
from shutil import rmtree
import random as rd
from solution import vowels_in_string

TEST_COUNT = 50
TEST_PATH = 'tests'
ANSWER_PATH = 'tests'
SAMPLES_PATH = 'tests'

SAMPLES = ['Буря мглою небо кроет...',
           'My heart`s in the Highlands, My heart is not here.']
STRINGS = [
    'WHEN you are old and gray and full of sleep And nodding by the fire, take down this book, And slowly read, and dream of the soft look Your eyes had once, and of their shadows deep;',
    'Of great limbs gone to chaos, A great face turned to night Why bend above a shapeless shroud Seeking in such archaic cloud Sight of strong lords and light?',
    'If you can keep your head when all about you Are losing theirs and blaming it on you; If you can trust yourself when all men doubt you, But make allowance for their doubting too: If you can wait and...',
    'Inscribed to a dear Child: in memory of golden summer hours and whispers of a summer sea.',
    'Love is like the wild rose-briar, Friendship like the holly-tree -- The holly is dark when the rose-briar blooms But which will bloom most contantly?',
    'Серые глаза — рассвет, Пароходная сирена, Дождь, разлука, серый след За винтом бегущей пены. Чёрные глаза — жара, В море сонных звёзд скольженье, И у борта до утра Поцелуев...',
    'Однажды, в студёную зимнюю пору Я из лесу вышел; был сильный мороз. Гляжу, поднимается медленно в гору Лошадка, везущая хворосту воз.',
    'На самом деле мне нравилась только ты, мой идеал и моё мерило. Во всех моих женщинах были твои черты, и это с ними меня мирило.',
    'Когда в объятия мои Твой стройный стан я заключаю, И речи нежные любви Тебе с восторгом расточаю...',
    'Мне нравится, что Вы больны не мной, Мне нравится, что я больна не Вами, Что никогда тяжёлый шар земной Не уплывёт под нашими ногами.',
    'Пой же, пой. На проклятой гитаре Пальцы пляшут твои в полукруг. Захлебнуться бы в этом угаре, Мой последний, единственный друг.',
    '— Снова дралась во дворе?.. — Aга! Мама, но я не плакала!.. Вырасту — выучусь на моряка. Я уже в ванне плавала!',
    'Послушайте! Ведь, если звёзды зажигают — значит — это кому-нибудь нужно? Значит — кто-то хочет, чтобы они были?',
    'A', 'Ы', 'PS', 'В'
]


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

        with open(test_file_name, 'w', encoding='utf8', newline="\n") as test_stream:
            data = f'line = "{sample}"\n' \
                   f'print("".join(vowels_in_string(line)))'
            print(data, file=test_stream)

        with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
            print(''.join(make_output_data(sample)), sep='\n', file=answer_stream)

        print(f'Sample {index + 1} [OK]')


def make_test(test_number):
    test_file_name = f'./{TEST_PATH}/{test_number + 1:02}'
    answer_file_name = f'./{ANSWER_PATH}/{test_number + 1:02}.a'

    input_data = make_input_data()
    output_data = make_output_data(input_data)

    with open(test_file_name, 'w', encoding='utf8', newline="\n") as test_stream:
        data = f'line = "{input_data}"\n' \
               f'print("".join(vowels_in_string(line)))'
        print(data, file=test_stream)

    with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
        print(''.join(output_data), sep='\n', file=answer_stream)

    print(f'Test {test_number + 1} [OK]')


def make_input_data():
    data = rd.choice(STRINGS)
    return data


def make_output_data(input_data):
    return vowels_in_string(input_data)


if __name__ == '__main__':
    main()
