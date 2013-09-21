#!/bin/env/python
from vars import *
from datetime import datetime
import copy

#Converts an integer
#to its english
#representation
def toString(number):
    if (number == 0):
        return 'zero'
    if (number == 1):
        return 'one'
    if (number == 2):
        return 'two'
    if (number == 3):
        return 'three'
    if (number == 4):
        return 'four'
    if (number == 5):
        return 'five'
    if (number == 6):
        return 'six'
    if (number == 7):
        return 'seven'
    if (number == 8):
        return 'eight'
    if (number == 9):
        return 'nine'

# returns the number given
# in the form of a list
# from numbers
def getNum(number):
    intervalOffset = 3
    numOffset = (number % 10) * 3
    return numbers[numOffset:numOffset+intervalOffset]

# calls getNum
# returns number list
# from vars.numbers
def getNumList(time):
    numbas = {
        'zero':getNum(0),
        'one':getNum(1),
        'two':getNum(2),
        'three':getNum(3),
        'four':getNum(4),
        'five':getNum(5),
        'six':getNum(6),
        'seven':getNum(7),
        'eight':getNum(8),
        'nine':getNum(9)
    }
    return numbas[toString(time)]

# gets current time
# and returns list of ints
# in clock-face order
def getTime():
    time = datetime.now().time().strftime('%I:%M')
    timeList = []
    timeList.append(int(str(time)[0:1]))
    timeList.append(int(str(time)[1:2]))
    timeList.append(int(str(time)[3:4]))
    timeList.append(int(str(time)[4:5]))
    return timeList

# drawsTime lol
def drawTime():
    timeList = getTime()
    numList = []
    for x in range(5):
        print '\n'
    for x in timeList:
        numList.append(getNumList(x))
    print '\n'.join(clock[0:3])
    print str(clock[3]).replace('##',str(numList[-1][0]))
    print str(clock[4]).replace('###',str(numList[-1][1]))
    print str(clock[5]).replace('##',str(numList[-2][0]),1).replace('##',str(numList[-1][2]))
    print str(clock[6]).replace('###',str(numList[-2][1]))
    print str(clock[7]).replace('##',str(numList[-3][0]),1).replace('##',str(numList[-2][2]))
    print str(clock[8]).replace('###',str(numList[-3][1]))
    print str(clock[9]).replace('##',str(numList[-4][0]),1).replace('##',str(numList[-3][2]))
    print str(clock[10]).replace('###',str(numList[-4][1]))
    print str(clock[11]).replace('##',str(numList[-4][2]))
    print str(clock[12])

if __name__ == '__main__':
    drawTime()
