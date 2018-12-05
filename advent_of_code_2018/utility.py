def read_lines_from_file(file_reader, path_to_file):
    with file_reader(path_to_file, 'r') as file:
        return file.readlines()
