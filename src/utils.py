## This folder creates utility functions to manage and clean data sets.


from csv_to_list import data, mainColumn


## Function to insert a line break.
def doubleSpace():
    print('\n')


## Function takes two lists as parameters and returns a new list with the items that exist in both lists. The new list does not have duplicates.
def combineLists(list1, list2):
    newList = []
    for i in range (0, len(list1)):
        for j in range (0, len(list2)):
            if list1[i] == list2[j]:
                newList.append(list1[i])
    return(newList)


## Function takes a list as parameter and prints all elements from that list in numbered fashion.
def printNumberedList (arr):
    for i in range (0, len(arr)):
        print(f'{int(i) + 1}. {arr[i]}')


## Function takes a string of a dog breed as parameter (eg: 'Golder Retriever') and returns that breed's index in <data>.
def findBreedIndex(breed):
    allBreedsArr = []
    for i in range(0, len(data)):
        allBreedsArr.append(data[i][mainColumn])
    return(allBreedsArr.index(breed))

## Function that takes a string of attributes (eg: ['Loyal, friendly, intelligent']) and returns a list of them (eg: ['Loyal', 'Friendly', 'Intelligent'])
def split(commaSeparatedString):
    formatStr = str(commaSeparatedString)
    commaSeparatedList = formatStr.split(', ')
    
    splitList = []
    for i in range (0, len(commaSeparatedList)):
        capitalizedElement = str(commaSeparatedList[i]).capitalize()
        splitList.append(capitalizedElement)

    return(splitList)

## Function takes a list of attributes (eg: ['Loyal, friendly, intelligent', 'Gentle, brave, friendly']) and returns a list without duplicates of all individual attributes in the original list (eg: ['Loyal', 'Friendly', 'Intelligent', 'Brave'...])
def parseListWithCommaSeparatedElements (attributesList):
    cleanAttributesList = []
    for i in range (0, len(attributesList)):
        listOfSubattributes = split(attributesList[i])
        
        for j in range (0, len(listOfSubattributes)):
            subattribute = listOfSubattributes[j]

            if not cleanAttributesList.__contains__(subattribute):
                cleanAttributesList.append(subattribute)
    
    return(cleanAttributesList)