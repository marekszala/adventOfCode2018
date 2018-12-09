import sys
import os
import re
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\utils'))

from utils import InputFileReader

inputFileName1 = os.path.join(os.path.dirname(__file__), 'input1.txt')
test = os.path.join(os.path.dirname(__file__), 'test.txt')
inputFileName2 = os.path.join(os.path.dirname(__file__), 'input1.txt')

def parseInputRow(inputRow):
    empty, date, actionName = re.split('[\[\]]', inputRow)
    actionName = actionName.strip()

    log = { 'date': datetime.strptime(date, '%Y-%m-%d %H:%M')}

    if actionName == 'falls asleep':
        log['action'] = 'sleep'
    if actionName == 'wakes up':
        log['action'] = 'awaken'
    if actionName.startswith('Guard'):
        log['action'] = 'shiftStarts'
        log['guard'] = actionName.replace('Guard #', '').replace(' begins shift', '')
    
    return log

def getLogEntries(inputData):
    logEntries = []
    for inputRow in inputData:
        logEntries.append(parseInputRow(inputRow))
    return logEntries

def updateSleepLog(dayLog, startMinute, endMinute):
    for i in range(startMinute, endMinute):
        dayLog[i] += 1

def processGuardLog(logEntries):
    guardInfo = {}
    dayLog = []

    for i in range(0, len(logEntries)-1):
        log = logEntries[i]
        nextLog = logEntries[i+1]
        date = log['date']
        nextDate = nextLog['date']

        if (i!= 0 and nextLog['action'] == 'shiftStarts' and nextLog['action'] == 'sleep'):
            updateSleepLog(dayLog, date.minute, 59)
        
        elif log['action'] == 'shiftStarts':
            currentGuard = log['guard']
            if not guardInfo.has_key(currentGuard):
                dayLog = [0 for i in xrange(59)]
                guardInfo[currentGuard] = dayLog
            else:
                dayLog = guardInfo[currentGuard] 

        elif log['action'] == 'sleep':
            updateSleepLog(dayLog, date.minute, nextDate.minute)          
        elif i == len(logEntries) - 1 and nextLog['action'] == 'sleep':
            updateSleepLog(dayLog, nextDate.minute, 59)

    return guardInfo
    
def getTheMostSleepyGuard(quardLog):
    theBiggestSleeper = ''
    theBiggestSleeperSleepMinutes = 0
    
    for guard in quardLog.keys():
        guardSleepMinutes = sum(quardLog[guard])

        if guardSleepMinutes > theBiggestSleeperSleepMinutes:
            theBiggestSleeper = guard
            theBiggestSleeperSleepMinutes = guardSleepMinutes

    theMinute = quardLog[theBiggestSleeper].index(max(quardLog[theBiggestSleeper]))

    return int(theBiggestSleeper) * theMinute

def getTheMostSleepyMinute(quardLog):
    theGuard = ''
    theMostSleepyMinute = 0
    theMostSleepyMinuteValue = 0
    
    for guard in quardLog.keys():
        # count sleep hours
        guardTheMostSleepyMinuteValue = max(quardLog[guard])
        guardTheMostSleepyMinute = quardLog[guard].index(guardTheMostSleepyMinuteValue)

        if guardTheMostSleepyMinuteValue > theMostSleepyMinuteValue:
            theGuard = guard
            theMostSleepyMinute = guardTheMostSleepyMinute
            theMostSleepyMinuteValue = guardTheMostSleepyMinuteValue

    return int(theGuard) * theMostSleepyMinute

def problem1(inputData):
    logEntries = getLogEntries(inputData)
    logEntries = sorted(logEntries, key= lambda log: log['date'])

    quardLogs = processGuardLog(logEntries)
    
    return getTheMostSleepyGuard(quardLogs)

def problem2(inputData):
    logEntries = getLogEntries(inputData)
    logEntries = sorted(logEntries, key= lambda log: log['date'])

    quardLogs = processGuardLog(logEntries)
    
    return getTheMostSleepyMinute(quardLogs)

if __name__ == '__main__':
    fileReader = InputFileReader()

   # problem1Result = problem1(fileReader.readContent(inputFileName1))
   # print (problem1Result)

    problem2Result = problem2(fileReader.readContent(inputFileName1))
    print (problem2Result)
