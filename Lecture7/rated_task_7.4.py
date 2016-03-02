import datetime


def create_calendar_page(month, year=int(str(datetime.datetime.today())[:4])):

    days_in_month = {1: 31,
                     2: 28,
                     3: 31,
                     4: 30,
                     5: 31,
                     6: 30,
                     7: 31,
                     8: 31,
                     9: 30,
                     10: 31,
                     11: 30,
                     12: 31
                     }
    days = days_in_month[month]
    if month is 2 and year % 4 is 0 and (year % 100 != 0 or year % 400 is 0):
        days += 1
    week_count = [[], [], [], [], [], []]
    week_num = 0
    cur_day = 1
    calendar_string = '\n'
    while cur_day != days+1:
        if not (week_count[week_num]):
            week_count[week_num] = ['  ', '  ', '  ', '  ', '  ', '  ', '  ']
        dt = datetime.datetime(year, month, cur_day)
        week_count[week_num][int(dt.weekday())] = str(cur_day).zfill(2)
        if int(dt.weekday()) == 6:
            week_num += 1
        cur_day += 1
    for item in week_count:
        if not item:
            week_count.remove(item)
    i1 = 0
    while i1 != 7:
        if week_count[len(week_count)-1][i1] == '  ':
            week_count[len(week_count)-1] = week_count[len(week_count)-1][:i1]
            break
        else:
            i1 += 1
    for item in week_count:
        my_string = ''
        for i in item:
            if len(my_string) < 2*len(item)+len(item)-3:
                my_string += i+' '
            else:
                my_string += i
        if len(calendar_string) > 20*(len(week_count)-1):
            calendar_string += my_string
        else:
            calendar_string += my_string+'\n'
    calendar = '-'*20+'\n'+'MO TU WE TH FR SA SU'+'\n'+'-'*20+calendar_string
    return calendar


print create_calendar_page(12, 2019)
print create_calendar_page(1, 2020)
print create_calendar_page(9, 1939)
print create_calendar_page(1, 1988)
print create_calendar_page(01, 1988)




