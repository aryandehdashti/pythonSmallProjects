import datetime

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

print('Enter the year for the calendar:')
year = int(input('>'))
print('Enter the month for the calendar, 1-12:')
month = int(input('>'))


def createCall(month, year):
    calText = ''
    calText += ' '*34 + '{} {}\n'.format(MONTHS[month-1], year)
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '+\n'
    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    
    while True:
        calText += weekSeparator
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break

    calText += weekSeparator
    return calText

calText = createCall(month, year)
print(calText)
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)
print('Saved to ' + calendarFilename)
