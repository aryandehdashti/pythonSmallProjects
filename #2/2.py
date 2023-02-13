from random import randint
from datetime import date,timedelta


def generateDates(k):
    return [date(1, 1, 1) + timedelta(randint(0,364)) for i in range(k)]

def matchSameDate(dates):
    datesSet = set(dates)
    return len(datesSet) < len(dates)

def main():
    k = int(input('How many people? '))
    matchedCount = 0
    for i in range(100000):
        if matchSameDate(generateDates(k)):
            matchedCount += 1
        if i % 10000 == 0:
            print('{} simulations run ...'.format(i))
    print('{}%'.format(matchedCount/1000))


main()