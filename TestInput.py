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

#print(data2)
data_new = input2.copy()
data_new['prio_level'] = data2

print(data_new)

#dn thiyenne methana idan hadagena yana eka
#anthimata ekama dawase ekama welawe than dekaka lectures dekk thiyenna ba. eka check wenna one aniwaryen. eka blnna puluwn subject code ekaka palaweni string 4ren. EX- GTEC1, ETMP3,ETIA3
#MO_M3 ekk danawa pya3 session ekakata. ehema ekk dammoth M0_M1 ekai MO_M2 ekai dekama damma wage wena widiyat hadanna wenwa




#for j in range(0,len(lec_detail)):
#    for k in range (1,36):
#        out = (Get(k , data_new))
#        print(out[0][j])