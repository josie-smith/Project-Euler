import sys
sys.setrecursionlimit(1500)

def daysInMonth(month,year) :
    month = month%12
    if month in [1,3,5,7,8,10,0] :
        return 31
    elif month in [4,6,9,11] :
        return 30
    elif year%4 == 0 :
        if year%100 == 0 :
            if year%400 == 0 :
                return 29
            else: return 28
        else: return 29
    else: return 28

def firstOfMonth(month,year) :
    month = month%12
    if year == 1900 and month == 1 :
        return 1
    elif month == 1 :
        return (daysInMonth(month-1,year-1)%7 + firstOfMonth(month-1,year-1))%7
    else :
        return (daysInMonth(month-1,year)%7 + firstOfMonth(month-1,year))%7

def countFirstSundays() :
    count = 0
    for year in range(1901, 2001) :
        for month in range(12) :
            if firstOfMonth(month,year) == 0 :
                count+=1
    return count


print(countFirstSundays())
