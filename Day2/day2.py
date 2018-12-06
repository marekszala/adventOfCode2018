from utils import InputFileReader
import sys
import os
sys.path.append("C:\\code\\maszala\\adventcode2018\\utils")

inputFileName1 = os.path.join(os.path.dirname(__file__), 'input1.txt')


def getCharacterHistogram(word):
    countDict = {}
    for char in word:
        if char not in countDict:
            countDict[char] = 1
        else:
            countDict[char] += 1

    return countDict


def containsExactlyLetters(count, characterHistogram):
    for value in characterHistogram.values():
        if value == count:
            return True

    return False


def isSimilar(word1, word2, allowedDifference):
    difference = 0
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            difference += 1

        if difference > allowedDifference:
            return False

    return True


def getCommonCharacters(word1, word2):
    result = ""

    for i in range(0, len(word1)):
        if word1[i] == word2[i]:
            result = result + word1[i]

    return result


def problem2(inputData):
    for i in range(0, len(inputData)):
        for j in range(i + 1, len(inputData)):
            if isSimilar(inputData[i], inputData[j], 1):
                return getCommonCharacters(inputData[i], inputData[j])

    raise "Did not find any matching entries"


def problem1(inputData):
    count2 = 0
    count3 = 0
    for word in inputData:
        histogram = getCharacterHistogram(word)
        if containsExactlyLetters(2, histogram):
            count2 += 1
        if containsExactlyLetters(3, histogram):
            count3 += 1

    return count2*count3


if __name__ == '__main__':
    fileReader = InputFileReader()

    problem1Result = problem1(fileReader.readContent(inputFileName1))

    problem2Result = problem2(fileReader.readContent(inputFileName1))

    print (problem1Result)

    print (problem2Result)
