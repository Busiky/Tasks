#!/usr/bin/python3

from os import mkdir
from os.path import isdir
from shutil import rmtree
import random as rd
from string import ascii_letters, digits
from solution import decimal_translator_2

TEST_COUNT = 50
TEST_PATH = 'tests'
ANSWER_PATH = 'tests'
SAMPLES_PATH = 'tests'

SAMPLES = [
    '1Z 36',
    '1A0 9'
]
abc = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


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
            print(f'print(decimal_translator_2("{sample.split()[0]}", {int(sample.split()[1])}))', file=test_stream)

        with open(answer_file_name, 'w', encoding='utf8') as answer_stream:
            print(make_output_data(sample), sep='\n', file=answer_stream)

        print(f'Sample {index + 1} [OK]')


def make_test(test_number):
    test_file_name = f'./{TEST_PATH}/{test_number + 1:02}'
    answer_file_name = f'./{ANSWER_PATH}/{test_number + 1:02}.a'

    input_data = make_input_data()
    output_data = make_output_data(input_data)

    with open(test_file_name, 'w', encoding='utf8') as test_stream:
        print(f'print(decimal_translator_2("{input_data.split()[0]}", {int(input_data.split()[1])}))', file=test_stream)

    with open(answer_file_name, 'w', encoding='utf8') as answer_stream:
        print(output_data, sep='\n', file=answer_stream)

    print(f'Test {test_number + 1} [OK]')


def make_input_data():
    base = rd.randint(2, 36)
    delta = rd.choice(abc)
    choises = list(abc[:base]) + [delta]
    number = ''.join([rd.choice(choises) for _ in range(rd.randint(1, 30))])
    return f'{number} {str(base)}'


def make_output_data(input_data):
    number, base = input_data.split()
    return decimal_translator_2(number, int(base))


if __name__ == '__main__':
    main()
