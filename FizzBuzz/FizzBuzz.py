# coding: utf-8

import os
from distutils.util import strtobool

def FizzBuzz():
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
                min, max = get_range()
                print("\nAwsome! Now that we have our start and end we need our fizz and our buzz!\n")
                fizz, buzz = get_fizzbuzz()
                for i in range(min, max+1):
                    if i % fizz == 0 and i % buzz == 0:
                        print("FizzBuzz")
                    elif i % fizz == 0:
                        print("Fizz")
                    elif i % buzz == 0:
                        print("Buzz")
                    else:
                        print(i)
                try:
                    option = strtobool(input("\nWould you like to play again? (y/n) "))
                except ValueError:
                    print("\nSorry, I didn't understand!\nYou should reply with yes or no!\n")
                    os.system("pause")
                    os.system('cls')
            elif option == 0:
                os.system('cls')
                print("\nThat's too bad, let's play another time then!\nGoodbye!\n")
                os.system("pause")
                quit()          

def get_range():
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
        os.system('cls')
        return min, max

def get_fizzbuzz():
    while True:
        print("What should fizz be?")
        fizz = get_int()
        while fizz == 0:
            os.system('cls')
            print("Well, the only multiple of 0 is 0 so thats no fun... Can you pick a diferent number?\n")
            print("What should fizz be?")
            fizz = get_int()
        print("Awsome! We're gonna replace multiples of",fizz,"with the word Fizz!\n")
        os.system("pause")
        os.system('cls')
        print("And what should buzz be?")
        buzz = get_int()
        while buzz == 0 or buzz == fizz:
            os.system('cls')
            if buzz == 0:
                print("Well, the only multiple of 0 is 0 so thats no fun... Can you pick a diferent number?\n")
            if buzz == fizz:
                print("For the most fun buzz and fizz should be different numbers! Can you pick a diferent number?\n")
            print("What should buzz be?")
            buzz = get_int()
        print("Awsome! We're gonna replace multiples of",buzz,"with the word Buzz!\n")
        print("Multiples of both",fizz,"and",buzz,"will be replaced with FizzBuzz!\n")
        os.system("pause")
        os.system('cls')
        return fizz, buzz

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

os.system('cls')
FizzBuzz()