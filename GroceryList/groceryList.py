# Author: Davide Pollicino
# Date: 08/12/2019

import os


def print_menu():
    print("Type '/' to know how to use this grocery list")
    command = input("Command: ")
    print(command)
    if command == '/':
        print_commands()
    elif command == '/list':
        print_list()
    elif command == '/delete':
        delete_list()
    elif command == '/add':
        add_element()
    elif command == '/stop':
        exit(0)
    else:
        print("Wrong command")


# Print list of commands
def print_commands():
    print('/-> Show the list of commands')
    print('/delete -> Delete the list')
    print('/add -> Add an element in the list')
    print('/list -> Show the list')
    print('/stop')


# Add a new element in the list
def add_element():
    f = open("list.txt", "a+")
    newElement = input("New element of the list: ")
    f.write(newElement)
    f.write('\n')
    f.close()


# Print all the elements off the list
def print_list():
    f = open("list.txt", "r")
    if os.stat("list.txt").st_size == 0:
        print("List already empty")
    else:
        for line in f:
            print(line)
    f.close()


# Delete all the content fo the list
def delete_list():
    if os.stat("list.txt").st_size == 0:
        print("List already empty")
    else:
        f = open("list.txt", "w")
        f.truncate(0)
        print('List removed')
        f.close()


while 1:
    print_menu()
