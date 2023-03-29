## This folder loads the dataset (csv file), converts it into a list and saves it to a variable {data}
import csv


## fileName should be assigned to the csv file that contains the raw data that will assist our chatbot in making a recommendation
fileName = '../dog_breeds.csv'


## Transform the csv file into a list. Create another list {propertiesArr} with the elements of the header column of {fileName}.
file = open(fileName, "r")
data = list(csv.DictReader(file, delimiter=","))
propertiesArr = list(data[0].keys())
file.close()


## Create a variable {mainColumn} from the list of elements in the header of {fileName}. {mainColumn} should be the header element that we will be recommending: 'Breed' in this case (Column A of the csv).
mainColumn = propertiesArr[0]


## Remove {mainColumn} from the list of properties that the user will input.
propertiesArr.remove(mainColumn)