import sys, os

sys.path.append("C:\\code\\maszala\\adventcode2018\\utils")
from utils import InputFileReader

inputFileName1 = os.path.join(os.path.dirname(__file__), 'input1.txt')

def getCharacterHistogram(word):
    countDict = {}
    for char in word:
        if char not in countDict:
            countDict[char] = 1
        else:
            countDict[char] +=1

    return countDict

def containsExactlyLetters(count, characterHistogram):
    
    for value in characterHistogram.values():
        if value == count:
            return True

    return False

def problem1(inputData):
    count2 = 0
    count3 = 0
    for word in inputData:
        histogram = getCharacterHistogram(word)
        if containsExactlyLetters(2, histogram):
            count2 +=1
        if containsExactlyLetters(3, histogram):
            count3+=1

    return count2*count3

def problem2(inputData):
    return 0


if __name__ == '__main__':
    fileReader = InputFileReader()

    problem1Result = problem1(fileReader.readContent(inputFileName1))

    problem2Result = problem2(fileReader.readContent(inputFileName1))

    print (problem1Result)

    print (problem2Result)


