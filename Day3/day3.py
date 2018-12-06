import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\utils'))

from utils import InputFileReader

inputFileName1 = os.path.join(os.path.dirname(__file__), 'input1.txt')
inputFileName2 = os.path.join(os.path.dirname(__file__), 'input1.txt')


def readClaim(claimRow):
    empty, id, leftIndent, topIndent, sizeX, sizeY = re.split('[#@,:x]', claimRow)

    return [id, int(leftIndent), int(topIndent), int(sizeX), int(sizeY)]

def selectSquareForClaim(fabric, claim):
    id, leftIndent, topIndent, sizeX, sizeY = claim

    for x in range (leftIndent, leftIndent + sizeX):
        for y in range (topIndent, topIndent + sizeY):
            fabric[y][x]+=1

def getOverlappingPixelsCount(fabric):
    result = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if fabric[x][y] > 1:
                result += 1

    return result

def getClaims(claimRows):
    claims=[]
    for claimRow in claimRows:
        claims.append(readClaim((claimRow)))

    return claims

def getEmptyFabric(x, y):
    return [[0 for i in xrange(x)] for i in xrange(y)]

def applyClaims(fabric, claims):
    for claim in claims:
        selectSquareForClaim(fabric, claim)


def problem1(claimRows):
    claims = getClaims(claimRows)
    fabric = getEmptyFabric(1000, 1000)
    applyClaims(fabric, claims)

    return getOverlappingPixelsCount(fabric)

def isOverlapped(fabric, claim):
    id, leftIndent, topIndent, sizeX, sizeY = claim

    for x in range (leftIndent, leftIndent + sizeX):
        for y in range (topIndent, topIndent + sizeY):
            if fabric[y][x] != 1:
                return True

    return False

def problem2(claimRows):
    claims = getClaims(claimRows)
    fabric = getEmptyFabric(1000, 1000)
    applyClaims(fabric, claims)

    for claim in claims:
        if not isOverlapped(fabric, claim):
            return claim[0]

    raise "Did not find any solution"


if __name__ == '__main__':
    fileReader = InputFileReader()

    problem1Result = problem1(fileReader.readContent(inputFileName1))

    problem2Result = problem2(fileReader.readContent(inputFileName2))

    print ("Result1: ", problem1Result)

    print (problem2Result)
