import sys, os

sys.path.append("C:\\code\\maszala\\adventcode2018\\utils")

from utils import InputFileReader
inputFileName1 = os.path.join(os.path.dirname(__file__), 'input.txt')
inputFileName2 = os.path.join(os.path.dirname(__file__), 'input2.txt')

def problem1(inputData):
    sum = 0

    while len(inputData) > 0:
        value = int(inputData.pop(0))
        sum += value

    return sum

def problem2(inputData):
    freq = 0
    knownFreq = {0}

    while(True):
        for change in inputData:
            factor = int(change)
            freq += factor

            if freq in knownFreq:
                return freq

            knownFreq.add(freq)

    return 0  


if __name__ == '__main__':
    fileReader = InputFileReader()

    problem1Result = problem1(fileReader.readContent(inputFileName1))

    problem2Result = problem2(fileReader.readContent(inputFileName2))

    print (problem1Result)

    print (problem2Result)


