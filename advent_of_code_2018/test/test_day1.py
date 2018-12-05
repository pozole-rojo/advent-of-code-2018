from advent_of_code_2018.day_1.day1 import add_frequencies
from advent_of_code_2018.day_1.inputs.input_1 import get_input_1


def test_add_only_one_number():
    frequencies = ['+1']
    assert add_frequencies(frequencies) == 1


def test_add_two_positive_numbers():
    frequencies = ['+1', '+1']
    assert add_frequencies(frequencies) == 2


def test_add_two_negative_numbers():
    frequencies = ['-1', '-1']
    assert add_frequencies(frequencies) == -2


def test_add_3_numbers():
    frequencies = ['+1', '+1', '+1']
    assert add_frequencies(frequencies) == 3

    frequencies = ['+1', '+1', '-2']
    assert add_frequencies(frequencies) == 0

    frequencies = ['-1', '-2', '-3']
    assert add_frequencies(frequencies) == -6


def test_add_input_1():
    assert add_frequencies(get_input_1()) == 556
