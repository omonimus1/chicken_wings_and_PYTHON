"""
Author: Davide POllicino 
Date: 11/05/2020
Summary: Print content of a file if it exists and then write random text provideed by the user
"""
def print_file_content(filename):
    # r+ allows us to both read and write in the file
    try:
        with open(filename, 'r') as f:
            file_content = f.read()
            # Check if the file is empty
            if file_content == '':
                print('The file is empty')
            else:
                print(file_content) 
    except:
        print('Error while opening the file')


def write_inside_the_file(text_to_add, filename):
    # a : append at the end of the file 
    try:
        with open(filename, 'a') as f:
            f.write(text_to_add)
    except:
        print('Error while adding new data in the file')

if '__name__' == '__main__':
    print_file_content('example.txt')
    write_inside_the_file('extra text inside the file', 'example.txt')
    print_file_content('example.txt')