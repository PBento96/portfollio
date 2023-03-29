# coding: utf-8

import os
from distutils.util import strtobool

def FizzBang():
    while True:
        try:
            option = strtobool(input("Hello! Would you like to play FizzBang? (y/n)"))
        except ValueError:
            print("\nSorry, I didn't understand!\nYou should reply with yes or no!\n")
            os.system("pause")
            os.system('cls')
        else:
            if option == 1:
                print("\nGreat! I love this game!\n")
                get_range()
            elif option == 0:
                print("\nThat's too bad, let's play another time then!\n Goodbye!")
                os.system("pause")
                quit()          

def get_range():
    while True:
        print("range")
        break

FizzBang()