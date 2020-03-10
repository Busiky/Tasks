#!/usr/bin/python3
import string
from os import mkdir
from os.path import isdir
from shutil import rmtree
import random as rd
from solution import *

TEST_COUNT = 50
TEST_PATH = 'tests'
ANSWER_PATH = 'tests'
SAMPLES_PATH = 'tests'

SAMPLES = ['02C22418243C183E6424182400', '014224180800']
SEQUENCE = '0123456789abcdef'

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
            line = f"print('\\n'.join(''.join(map(str, item)) for item in from_bit_to_pic('{sample}')))"
            print(line, file=test_stream)

        with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
            print('\n'.join(''.join(map(str, item)) for item in make_output_data(sample)), sep='\n', file=answer_stream)

        print(f'Sample {index + 1} [OK]')


def make_test(test_number):
    test_file_name = f'./{TEST_PATH}/{test_number + 1:02}'
    answer_file_name = f'./{ANSWER_PATH}/{test_number + 1:02}.a'

    input_data = make_input_data()
    output_data = make_output_data(input_data)

    with open(test_file_name, 'w', encoding='utf8', newline="\n") as test_stream:
        line = f"print('\\n'.join(''.join(map(str, item)) for item in from_bit_to_pic('{input_data}')))"
        print(line, file=test_stream)

    with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
        print('\n'.join(''.join(map(str, item)) for item in output_data), sep='\n', file=answer_stream)

    print(f'Test {test_number + 1} [OK]')


def make_input_data():
    m = rd.randrange(4, 1000, 2)
    number = ''.join([rd.choice(SEQUENCE) for _ in range(m)])
    return number


def make_output_data(input_data):
    return from_bit_to_pic(input_data)


if __name__ == '__main__':
    main()
