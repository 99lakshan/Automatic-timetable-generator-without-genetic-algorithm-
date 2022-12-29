import numpy as np
import pandas as pd
from GetPriority import *

input1 = pd.read_csv("Data/sam.csv")
# print(input1)

lec_detail = pd.read_csv("Data/instructors1.csv")
# print(lec_detail)

room_detail = pd.read_csv("Data/room_table.csv")
# print(room_detail)

##################

data2 = []
d = {}
for x in range(0, (len(lec_detail))):
    d.update({lec_detail['lecturer_code'][x]: lec_detail['prio_level'][x]})

for i in range(0, (len(input1))):
    data = input1['lecturer_code'][i]
    # print(data)
    if data in d:
        data2.append(d[data])

# print(data2)
data_new = input1.copy()
data_new['prio_level'] = data2

print(data_new)

print(number(2 , data_new))
# cols = ['subject_code','lecturer_code','day','session_no','white_board','projector','computers']


