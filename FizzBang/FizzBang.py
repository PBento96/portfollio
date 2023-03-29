# coding: utf-8

import os
from distutils.util import strtobool

def FizzBang():
    while True:
        try:
            option = strtobool(input("\nHello! Would you like to play FizzBang? (y/n) "))
        except ValueError:
            print("\nSorry, I didn't understand!\nYou should reply with yes or no!\n")
            os.system("pause")
            os.system('cls')
        else:
            if option == 1:
                os.system('cls')
                print("\nGreat! I love this game!\n")
                get_values()
            elif option == 0:
                os.system('cls')
                print("\nThat's too bad, let's play another time then!\nGoodbye!\n")
                os.system("pause")
                quit()          

def get_values():
    while True:
        print("\nTo start, we will need to set the range!\n\nRemember both the begining and the end should be Integers,")
        print("and the end should be higher than the begining!\n")
        os.system("pause")
        os.system('cls')
        print("What is the begining?")
        min = get_int()
        print("Great! We will start at ", min," then!\n")
        print("What is the end?")
        max = get_int()
        print("Great! We will end with ", max,", excellent choice!\n")
        os.system("pause")
        break

def get_int():
    while True:
        try:
            num = int(input())
            return num
        except ValueError:
            print("\nSorry, I didn't understand!\nYou should reply with an Integer (whole number)!\n")
            os.system("pause")
            os.system('cls')

FizzBang()