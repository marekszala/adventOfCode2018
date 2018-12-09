import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\utils'))

from utils import InputFileReader

inputFileName1 = os.path.join(os.path.dirname(__file__), 'input1.txt')
inputFileName2 = os.path.join(os.path.dirname(__file__), 'input2.txt')


def problem1(inputData):
    return 0


def problem2(inputData):
    return 0

if __name__ == '__main__':
    fileReader = InputFileReader()

    problem1Result = problem1(fileReader.readContent(inputFileName1))
    print ("solution1", problem1Result)

    problem2Result = problem2(fileReader.readContent(inputFileName2))
    print ("solution2", problem2Result)
