###Solution to problem 58 from ben stephenson's "the python workbook".

print("Enter date (YYYY-MM-DD):")

this_year,this_month,this_day = input().split('-')
this_year = int(this_year)
this_month = int(this_month.lstrip('0'))
this_day = int(this_day.lstrip('0'))

next_year = 0
next_month = 0
next_day = 0

def is_leap_year(year):
  result = False
  if (not year % 400) or ((not year % 4) and (year % 100)):
    result = True
  return(result)

monthdays = { 'january': 31,
              'february': 28,
              'march': 31,
              'april': 30,
              'may': 31,
              'june': 30,
              'july': 31,
              'august': 31,
              'september': 30,
              'october': 31,
              'november': 30,
              'december': 31 }

months = [i for i in monthdays.keys()]

if is_leap_year(this_year):
  monthdays['february'] = 29

if this_month == 12 and this_day == monthdays.get(months[11]):
  next_year = this_year + 1
  next_month = 1
  next_day = 1
elif this_day == monthdays.get(months[this_month - 1]):
  next_year = this_year
  next_month = this_month + 1
  next_day = 1
else:
  next_year = this_year
  next_month = this_month
  next_day = this_day + 1

if next_month < 10:
  next_month = str('0') + str(next_month)
if next_day < 10:
  next_day = str('0') + str(next_day)

print(f'{next_year}-{next_month}-{next_day}.')
