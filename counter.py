import time
import re

time_today = time.localtime()
print(time_today)

time_want = time.localtime()
print(time_want.tm_mon)
print(time_want.tm_mday)
print(time_want.tm_hour)
print(time_want.tm_min)

_result = input("want month, date, hour, min?" + "\n")
print(_result)

result = str(_result)
print(result)

'''
parsing code

"mon date hour min"

"mon day hour"


https://stackoverflow.com/questions/17325232/parsing-user-input-in-python

import re
s1 = '1321 .. 123123'
s2 = '-21323 , 1312321'
s3 = '- 12312.. - 9'

[int(x) for x in re.findall(r'[^,.]+', ''.join(s1.split()))]
=> [1321, 123123]

[int(x) for x in re.findall(r'[^,.]+', ''.join(s2.split()))]
=> [-21323, 1312321]

[int(x) for x in re.findall(r'[^,.]+', ''.join(s3.split()))]
=> [-12312, -9]

result = "6 9 14"
## data = [int(x) for x in re.findall(r'\d+', result)]
=> [6, 9, 14]
'''

_data = [int(x) for x in re.findall(r'\d+', result)]
print(str(_data)+"  "+str(len(_data)))


if len(_data) == 3:
    _data.append(0)
    print("this is list"+str(_data))

data = {
    "month": _data[0],
    "date": _data[1],
    "hour": _data[2],
    "minute": _data[3],
}

if data["month"] > 12:
 data["month"] = data["month"] - 12

if data["month"] < 1:
 data["month"] = data["month"] + 1

result_month = data["month"] - time_today.tm_mon
result_date = data["date"] - time_today.tm_mday
result_hour = data["hour"] - time_today.tm_hour
result_min = data["minute"] - time_today.tm_min

dDay = [result_month, result_date, result_hour, result_min]
print(dDay)
print(str(result_month * 30 + result_date)+" Date lefts.")
