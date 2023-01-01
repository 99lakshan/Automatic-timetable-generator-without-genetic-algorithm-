import numpy as np
import pandas as pd
from GetPriority import *
from Enterinputs import *

Answer = str(input("Do you want to enter your data :(y/n) : "))

if (Answer=="y"):
    x = inputs(Answer)
else:
    pass

input2 = pd.read_csv("Data/input2.csv")
#print(input2)
#print(input2['LEC_CODE'][0])
lec_detail = pd.read_csv("Data/instructors1.csv")
#print(lec_detail)

room_detail = pd.read_csv("Data/room_table.csv")
#print(room_detail)

#day = pd.read_csv("Data/Day_arrangement.csv")
#print(day)


data2 = []
d = {}
for x in range(0, (len(lec_detail))):
    d.update({lec_detail['lecturer_code'][x]: lec_detail['prio_level'][x]})

for i in range(0, (len(input2))):
    data = input2['LEC_CODE'][i]
    # print(data)
    if data in d:
        data2.append(d[data])

print(data2)
data_new = input2.copy()
data_new['prio_level'] = data2

print(data_new)

#dn thiyenne methana idan hadagena yana eka

out = (Get(2 , data_new))

print(out[0][2])