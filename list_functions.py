## This folder creates functions to process the user inputs and return a chatbot recommendation on which dog breeds match the user requirements.


from csv_to_list import data, mainColumn, propertiesArr
from utils import doubleSpace, printNumberedList


## Function takes in a property (eg: 'Country of Origin') and an attribute (eg: 'Germany') and returns an array of dog breeds that have that attribute in that property [eg: 'German Shepherd', 'Rottweiler'].
def breedsThatMeetConditions (property, attribute):
    breedsArr = []

    for i in range (0, len(data)):
        if data[i][property] == attribute:
            breedsArr.append(data[i][mainColumn])
    
    return(breedsArr)


## Function takes a list of breeds (eg: ['German Shepherd', 'Pomeranian']) and a property (eg: 'Country of Origin') and returns a list of the attributes of the breeds contained in the list of breeds (eg: ['Germany', 'Argentina'])
def breedsAttributes (breedsArr, property):
    allBreeds = []
    for i in range (0, len(data)):
        allBreeds.append(data[i][mainColumn])
    attributesArr = []
    for i in range (0, len(breedsArr)):
        breedIndex = allBreeds.index(breedsArr[i])
        attributesArr.append(data[breedIndex][property])
    return(attributesArr)


## Function takes a property (eg: 'Country of Origin') and returns a list of all attributes that a dog breed may have in that property (eg: ['Germany', 'Argentina'...])
def listOfAttributes (property):
    attributesArr = []
    for i in range (0, len(data)):
        if not attributesArr.__contains__(data[i][property]):
                attributesArr.append(data[i][property])
    return(attributesArr)