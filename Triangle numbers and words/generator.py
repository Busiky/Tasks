#!/usr/bin/python3
import string
from os import mkdir
from os.path import isdir
from shutil import rmtree
import random as rd
from solution import triangle

TEST_COUNT = 50
TEST_PATH = 'tests'
ANSWER_PATH = 'tests'
SAMPLES_PATH = 'tests'

SAMPLES = ['Sky', '123']
SEQUENCE = [n * (n + 1) // 2 for n in range(1, 10 ** 3)]


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
            line = f'print(triangle("{sample}"))'
            print(line, file=test_stream)

        with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
            print(make_output_data(sample), sep='\n', file=answer_stream)

        print(f'Sample {index + 1} [OK]')


def make_test(test_number):
    test_file_name = f'./{TEST_PATH}/{test_number + 1:02}'
    answer_file_name = f'./{ANSWER_PATH}/{test_number + 1:02}.a'

    input_data = make_input_data()
    output_data = make_output_data(input_data)

    with open(test_file_name, 'w', encoding='utf8', newline="\n") as test_stream:
        line = f'print(triangle("{input_data}"))'
        print(line, file=test_stream)

    with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
        print(output_data, sep='\n', file=answer_stream)

    print(f'Test {test_number + 1} [OK]')


def make_input_data():
    abc = string.ascii_letters
    word = ''.join(rd.choices(abc, k=rd.randint(1, 10)))
    number = str(rd.choice(SEQUENCE) + rd.choice([-1, 0, 0, 0, 0, 1]))
    return rd.choice([word, number, number, number])


def make_output_data(input_data):
    return triangle(input_data)


if __name__ == '__main__':
    main()
