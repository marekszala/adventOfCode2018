import sys
import os
import string 

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\utils'))

from utils import InputFileReader

inputFileName1 = os.path.join(os.path.dirname(__file__), 'input1.txt')
test = os.path.join(os.path.dirname(__file__), 'test.txt')

def calculatePolymer(fabric):
    result = []
    lastIndex = -1

    for i in range(0, len(fabric)):
        toCheck = fabric[i]
        if lastIndex < 0:
            result.append(toCheck)
            lastIndex += 1
        elif toCheck != result[lastIndex] and toCheck.lower() == result[lastIndex].lower():
            result.pop(lastIndex);
            lastIndex-= 1
        else:
            result.append(toCheck)
            lastIndex += 1
        
    return  len(result)


def problem1(inputData):
    return calculatePolymer(list(inputData[0]))


def problem2(inputData):
    lowest = -1
    alphabet = string.ascii_uppercase
    values = str(inputData[0])

    for letter in alphabet:
        updatedVersionOfPolymer = values.replace(letter, "")
        updatedVersionOfPolymer = updatedVersionOfPolymer.replace(letter.lower(), "")

        calculated = calculatePolymer(list(updatedVersionOfPolymer))
        if lowest < 0 or calculated < lowest:
            lowest = calculated

    return lowest

if __name__ == '__main__':
    fileReader = InputFileReader()

    problem1Result = problem1(fileReader.readContent(inputFileName1))
    print (problem1Result)

    problem2Result = problem2(fileReader.readContent(inputFileName1))
    print (problem2Result)
