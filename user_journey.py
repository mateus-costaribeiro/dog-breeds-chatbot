## This folder is the chatbot program. Run it to receive recommendations from the chatbot.


## Imports
from list_functions import listOfAttributes, breedsThatMeetConditions, breedsAttributes
from utils import doubleSpace, printNumberedList, combineLists
from chatbot_prompts import recommendations, firstGreeting, whichProperty, whichAttributes, next, congratulations, closingAsterisks, listOfProperties
from csv_to_list import propertiesArr
import pyinputplus as pyip


doubleSpace()
firstGreeting()
doubleSpace()
whichProperty()
doubleSpace()
listOfProperties()
doubleSpace()
property1 = pyip.inputNum(prompt="", greaterThan= 0, lessThan= len(propertiesArr) + 1)
doubleSpace()
whichAttributes(propertiesArr[int(property1)-1])
doubleSpace()


listOfAttributesObj = listOfAttributes(propertiesArr[int(property1) - 1])
printNumberedList(listOfAttributesObj)
doubleSpace()
## Add a lessThan statement
attribute1 = pyip.inputNum(prompt="", greaterThan= 0, lessThan=int(len(listOfAttributesObj) + 1))
chosenAttribute1 = listOfAttributesObj


list1 = breedsThatMeetConditions(propertiesArr[int(property1) - 1], listOfAttributesObj[int(attribute1) - 1])
doubleSpace()
recommendations()
doubleSpace()
printNumberedList(list1)
doubleSpace()
next()
doubleSpace()
propertiesArr.remove(propertiesArr[int(property1) - 1])


listOfProperties()
doubleSpace()
property2 = pyip.inputNum(prompt="", greaterThan= 0, lessThan= len(propertiesArr) + 1)
doubleSpace()
whichAttributes(propertiesArr[int(property2)-1])
doubleSpace()
listOfAttributesObj2 = breedsAttributes(list1, propertiesArr[int(property2) - 1])
printNumberedList(listOfAttributesObj2)
doubleSpace()


attribute2 = pyip.inputNum(prompt="", greaterThan= 0, lessThan=int(len(listOfAttributesObj2) + 1))
doubleSpace()
recommendations()
doubleSpace()
list2 = combineLists(list1, breedsThatMeetConditions(propertiesArr[int(property2) - 1], listOfAttributesObj2[int(attribute2) - 1]))
printNumberedList(list2)
doubleSpace()
next()
doubleSpace()
propertiesArr.remove(propertiesArr[int(property2) - 1])


listOfProperties()
doubleSpace()
property3 = pyip.inputNum(prompt="", greaterThan= 0, lessThan= len(propertiesArr) + 1)
doubleSpace()
whichAttributes(propertiesArr[int(property3)-1])
doubleSpace()
listOfAttributesObj3 = breedsAttributes(list2, propertiesArr[int(property3) - 1])
printNumberedList(listOfAttributesObj3)
doubleSpace()


attribute3 = pyip.inputNum(prompt="", greaterThan= 0, lessThan=int(len(listOfAttributesObj3) + 1))
doubleSpace()
recommendations()
doubleSpace()
list3 = combineLists(list2, breedsThatMeetConditions(propertiesArr[int(property3) - 1], listOfAttributesObj3[int(attribute3) - 1]))
printNumberedList(list3)
doubleSpace()
next()
doubleSpace()
propertiesArr.remove(propertiesArr[int(property3) - 1])


listOfProperties()
doubleSpace()
property4 = pyip.inputNum(prompt="", greaterThan= 0, lessThan= len(propertiesArr) + 1)
doubleSpace()
whichAttributes(propertiesArr[int(property4)-1])
doubleSpace()
listOfAttributesObj4 = breedsAttributes(list3, propertiesArr[int(property4) - 1])
printNumberedList(listOfAttributesObj4)
doubleSpace()


attribute4 = pyip.inputNum(prompt="", greaterThan= 0, lessThan=int(len(listOfAttributesObj4) + 1))
doubleSpace()
recommendations()
doubleSpace()
list4 = combineLists(list3, breedsThatMeetConditions(propertiesArr[int(property4) - 1], listOfAttributesObj4[int(attribute4) - 1]))
printNumberedList(list4)
doubleSpace()
next()
doubleSpace()
propertiesArr.remove(propertiesArr[int(property4) - 1])


listOfProperties()
doubleSpace()
property5 = pyip.inputNum(prompt="", greaterThan= 0, lessThan= len(propertiesArr) + 1)
doubleSpace()
whichAttributes(propertiesArr[int(property5)-1])
doubleSpace()
listOfAttributesObj5 = breedsAttributes(list4, propertiesArr[int(property5) - 1])
printNumberedList(listOfAttributesObj5)
doubleSpace()


attribute5 = pyip.inputNum(prompt="", greaterThan= 0, lessThan=int(len(listOfAttributesObj5) + 1))
doubleSpace()
recommendations()
doubleSpace()
list5 = combineLists(list4, breedsThatMeetConditions(propertiesArr[int(property5) - 1], listOfAttributesObj5[int(attribute5) - 1]))
printNumberedList(list5)
doubleSpace()
next()
doubleSpace()
propertiesArr.remove(propertiesArr[int(property5) - 1])


listOfProperties()
doubleSpace()
property6 = pyip.inputNum(prompt="", greaterThan= 0, lessThan= len(propertiesArr) + 1)
doubleSpace()
whichAttributes(propertiesArr[int(property6)-1])
doubleSpace()
listOfAttributesObj6 = breedsAttributes(list5, propertiesArr[int(property6) - 1])
printNumberedList(listOfAttributesObj6)
doubleSpace()


attribute6 = pyip.inputNum(prompt="", greaterThan= 0, lessThan=int(len(listOfAttributesObj6) + 1))
doubleSpace()
recommendations()
doubleSpace()
list6 = combineLists(list5, breedsThatMeetConditions(propertiesArr[int(property6) - 1], listOfAttributesObj6[int(attribute6) - 1]))
printNumberedList(list6)
doubleSpace()
next()
doubleSpace()
propertiesArr.remove(propertiesArr[int(property6) - 1])


listOfProperties()
doubleSpace()
property7 = pyip.inputNum(prompt="", greaterThan= 0, lessThan= len(propertiesArr) + 1)
doubleSpace()
whichAttributes(propertiesArr[int(property7)-1])
doubleSpace()
listOfAttributesObj7 = breedsAttributes(list6, propertiesArr[int(property7) - 1])
printNumberedList(listOfAttributesObj7)
doubleSpace()


attribute7 = pyip.inputNum(prompt="", greaterThan= 0, lessThan=int(len(listOfAttributesObj7) + 1))
doubleSpace()
list7 = combineLists(list6, breedsThatMeetConditions(propertiesArr[int(property7) - 1], listOfAttributesObj7[int(attribute7) - 1]))
congratulations()
doubleSpace()
printNumberedList(list7)
closingAsterisks()
doubleSpace()