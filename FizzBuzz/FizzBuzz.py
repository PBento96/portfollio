# coding: utf-8

import os
from distutils.util import strtobool

def FizzBang():
    while True:
        try:
            option = strtobool(input("\nHello! Would you like to play FizzBuzz? (y/n) "))
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
        print("\nTo start, we will need to set the range!\n\nRemember both the begining and the end should be Integers,\nand the end should be higher than the start!\n")
        os.system("pause")
        os.system('cls')
        print("What is the start number?")
        min = get_int()
        print("Great! We will start at", min,"then!\n")
        print("What is the end number?")
        max = get_int()
        while max <= min:
            print("That doesn't seem right... the game can't end before it starts!\nMake sure you're writing a number that is larger than", min,"!\n\nLet's try that again! When should the game end? ")
            max = get_int()
        print("Great! We will end with", max,", excellent choice!\n")
        os.system("pause")
        break

def get_int():
    while True:
        try:
            num = int(input())
            print()
            return num
        except ValueError:
            print("\nSorry, I didn't understand!\nYou should reply with an Integer (whole number)!\n")
            os.system("pause")
            os.system('cls')

FizzBang()