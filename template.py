from utils import InputFileReader
import sys
import os

sys.path.append("C:\\code\\maszala\\adventcode2018\\utils")

inputFileName1 = os.path.join(os.path.dirname(__file__), 'input1.txt')
inputFileName2 = os.path.join(os.path.dirname(__file__), 'input2.txt')


def problem1(inputData):
    return 0


def problem2(inputData):
    return 0


if __name__ == '__main__':
    fileReader = InputFileReader()

    problem1Result = problem1(fileReader.readContent(inputFileName1))

    problem2Result = problem2(fileReader.readContent(inputFileName2))

    print (problem1Result)

    print (problem2Result)
