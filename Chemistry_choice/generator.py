#!/usr/bin/python3

from os import mkdir
from os.path import isdir
from shutil import rmtree
import random as rd
from solution import solve

TEST_COUNT = 50
TEST_PATH = 'tests'
ANSWER_PATH = 'tests'
SAMPLES_PATH = 'tests'

SAMPLES = ['argon helium silicium aurum xenon krypton aluminium oxygenium',
           'neon calcium lithium hydrogenium radon radium hydrargyrum cuprum']
SUBSTANCES = ['nitrogenium', 'actinium', 'aluminium', 'americium', 'argon', 'astatinum', 'barium', 'beryllium',
              'berkelium', 'borum', 'bromum', 'vanadium', 'bismutum', 'hydrogenium', 'wolframium', 'gadolinium',
              'gallium', 'hafnium', 'helium', 'germanium', 'holmium', 'dysprosium', 'europium', 'ferrum', 'aurum',
              'indium', 'jodum', 'iridium', 'ytterbium', 'yttrium', 'cadmium', 'kalium', 'californium', 'calcium',
              'oxygenium', 'cobaltum', 'silicium', 'krypton', 'xenon', 'curium', 'lanthanum', 'lithium', 'lutetium',
              'magnesium', 'manganum', 'cuprum', 'mendelevium', 'molybdanum', 'arsenicum', 'natrium', 'neodymium',
              'neon',
              'neptunium', 'niccolum', 'niobium', 'stannum', 'osmium', 'palladium', 'platinum', 'plutonium', 'polonium',
              'praseodimium', 'promethium', 'protactinium', 'radium', 'radon', 'renium', 'rhodium', 'hydrargyrum',
              'rubidium', 'ruthenium', 'samarium', 'plumbum', 'selenium', 'sulfur', 'argentum', 'scandium', 'strontium',
              'stibium', 'thallium', 'tantalum', 'tellurium', 'terbium', 'technetium', 'titanium', 'thorium', 'thulium',
              'carboneum', 'uranium', 'fermium', 'phosphorus', 'francium', 'fluorum', 'chlorum', 'chromium', 'cesium',
              'cerium', 'zincum', 'zirconium', 'einsteinium', 'erbium']


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
            print(sample, file=test_stream)

        with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
            print(make_output_data(sample), sep='\n', file=answer_stream)

        print(f'Sample {index + 1} [OK]')


def make_test(test_number):
    test_file_name = f'./{TEST_PATH}/{test_number + 1:02}'
    answer_file_name = f'./{ANSWER_PATH}/{test_number + 1:02}.a'

    input_data = make_input_data()
    output_data = make_output_data(input_data)

    with open(test_file_name, 'w', encoding='utf8', newline="\n") as test_stream:
        print(input_data, file=test_stream)

    with open(answer_file_name, 'w', encoding='utf8', newline="\n") as answer_stream:
        print(output_data, sep='\n', file=answer_stream)

    print(f'Test {test_number + 1} [OK]')


def make_input_data():
    data = ' '.join(rd.choice(SUBSTANCES) for _ in range(rd.randint(5, 40)))
    return data


def make_output_data(input_data):
    return solve(input_data)


if __name__ == '__main__':
    main()
