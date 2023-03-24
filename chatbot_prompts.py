## This folder contains all functions of sentences and expressions that Albert (our chatbot) will say during his conversation with the user.


from utils import doubleSpace, printNumberedList
from csv_to_list import propertiesArr


def firstGreeting():
    print('Hi there! This program helps you choose your future dog.')


def interjection():
    print('Sounds good!')


def listOfProperties():
    print('These are the properties that you can choose from:')
    doubleSpace()
    printNumberedList(propertiesArr)


def whichProperty():
    print('Which of these dog properties matters the most to you? Please type a single integer.')


def whichAttributes(property):
    print(f'Sounds good! So in the {property} category, which of these attributes may your dog possess? Please type a single integer.')


def country():
    print(f'{interjection} Which country should your future dog be from? Please type the integers of the countries you like separated by commas.')


def recommendations():
    print(f'Here are the breeds that meet your condition:')


def next():
    print('Let us move to the next property now. Which of these other dog properties matters most to you?')


def congratulations():
    print('Congratulations! We have reached a conclusion about which dog you should have. The perfect breed(s) of dog for you are:')


def closingAsterisks():
    print('***')