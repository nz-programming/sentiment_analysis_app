import datetime

today = datetime.date.today()
print(f'today:{today}')

today_year = today.year
today_month = today.month
thismonth_start = datetime.date(today_year, today_month, 1)


if today_month == 1:
    lastmonth_start = datetime.date(today_year-1, 12, 1)
    lastmonth_last = datetime.date(today_year-1, 12, 31)
else:
    lastmonth_start = datetime.date(today_year, today_month-1, 1)
    lastmonth_last = thismonth_start + datetime.timedelta(days=-1)


print(f'today_year:{today_year}')
print(f'today_month:{today_month}')
print(f'thismonth:{thismonth_start}')
print(f'lastmonth_start:{lastmonth_start}')
print(f'lastmonth_last:{lastmonth_last}')