from mock import MagicMock
from advent_of_code_2018.utility import read_lines_from_file


def test_read_lines_from_file():
    mock_file_reader = MagicMock()
    read_lines_from_file(mock_file_reader, 'data.txt')
    mock_file_reader.assert_called_once_with('data.txt', 'r')
