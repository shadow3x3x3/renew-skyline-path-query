def read_edges_data(file_path):
    """
    Reading text file by every line
    """
    for line in open(file_path, 'r', encoding='UTF-8'):
        print(line, end='\n')