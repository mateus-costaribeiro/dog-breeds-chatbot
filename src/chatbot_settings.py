## This folder configures how the chatbot will interact with the user.


## Imports
from list_functions import listOfAttributes, breedsThatMeetConditions, breedsAttributes
from utils import doubleSpace, printNumberedList, combineLists
from chatbot_prompts import recommendations, firstGreeting, whichProperty, whichAttributes, next, congratulations, closingAsterisks, listOfProperties
from csv_to_list import propertiesArr
import pyinputplus as pyip


def chatBot():
    ## Change to not hardcode number 6
    list = []
    for i in range (0, 5):
        doubleSpace()

        ## If this is the Chatbot's first message, send a greeting message.
        if i == 0:
            firstGreeting()
            doubleSpace()              
                
        ## Ask user which dog property matters the most to them.
        whichProperty()
        doubleSpace()
        
        ## List to user the dog properties they can choose from.
        listOfProperties()
        doubleSpace()
        
        ## User inputs the property they want in their future dog.
        propertyInput = pyip.inputNum(prompt="", greaterThan= 0, lessThan= len(propertiesArr) + 1)
        doubleSpace()

        ## In the property category chosen by the user, ask user which attribute are they looking for in a dog.
        whichAttributes(propertiesArr[int(propertyInput)-1])
        doubleSpace()

        ## Different functions are used to determine which attributes the user can choose from. If this is not the user's first choice, list of options is filtered by their previous chioces.
        if i == 0:
            listOfAttributesObj = listOfAttributes(propertiesArr[int(propertyInput) - 1])            
        
        else:
            listOfAttributesObj = breedsAttributes(list, propertiesArr[int(propertyInput) - 1])                  
        
        ## List to user the dog attributes they can choose from.
        printNumberedList(listOfAttributesObj)
        doubleSpace()

        ## User inputs the attribute they want in their future dog.
        attributeInput = pyip.inputNum(prompt="", greaterThan= 0, lessThan=int(len(listOfAttributesObj) + 1))
        doubleSpace()        
        
        ## Different functions are used to determine which breeds will be recommended to the user. If this is not the user's first choice, list of breeds is filtered by their previous chioces. 
        recommendations()
        doubleSpace()
        if i == 0:
            breedsList = breedsThatMeetConditions(propertiesArr[int(propertyInput) - 1], listOfAttributesObj[int(attributeInput) - 1])

        else:
            breedsList = combineLists(list, breedsThatMeetConditions(propertiesArr[int(propertyInput) - 1], listOfAttributesObj[int(attributeInput) - 1]))
        
        ## If user has already listed all attributes, congratulate them and finalize the Chatbot.
        if i == 4:
            congratulations()
            doubleSpace()
            printNumberedList(breedsList)
            closingAsterisks()
            doubleSpace()
        
        ## List to user the dog breeds that are recommended to them and ask for additional input.
        else:
            printNumberedList(breedsList)
            doubleSpace()
            next()            

        ## Setup for next loop
        propertiesArr.remove(propertiesArr[int(propertyInput) - 1])
        list = breedsList