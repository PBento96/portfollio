# coding: utf-8

import os

def FizzBang():
    while True:
        option = input("Hello! Would you like to play FizzBang? (y/n)")
        if option == "y":
            print("")
        elif option == "n":
            print("")
        else:
            print("Goodbye")
            os.system("pause")
            quit()