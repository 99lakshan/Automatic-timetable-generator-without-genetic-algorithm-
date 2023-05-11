import pandas as pd

from GetPriority import *
from Enterinputs import *
from GetCapacity import *
from finalstore import *

Answer = str(input("Do you want to enter your data :(y/n) : "))

if Answer == "y":
    x = inputs(Answer)
else:
    pass

input2 = pd.read_csv("Data\input2.csv")
print(input2)
# print(input2['LEC_CODE'][0])
lec_detail = pd.read_csv("Data/instructors1.csv")
# print(lec_detail)

room_detail = pd.read_csv("Data/room_table.csv")
# print(room_detail)

# day = pd.read_csv("Data/Day_arrangement.csv")
# print(day)

data2 = []
d = {}
for x in range(0, (len(lec_detail))):
    d.update({lec_detail['lecturer_code'][x]: lec_detail['prio_level'][x]})

for i in range(0, (len(input2))):
    data = input2['LEC_CODE'][i]
    # print(data)
    if data in d:
        data2.append(d[data])

# print(data2)
data_new = input2.copy()
data_new['prio_level'] = data2

print(data_new)
# print(len(lec_detail))

# sam_list = []
# sub = []
for j in range(1, (len(lec_detail) + 1)):
    # print(j)
    out = (Get(j, data_new))
    print(out)
    if len(out) == 0:
        # print("This is empty")
        continue

    pp = out.tolist()  # pp - input detail table
    # print(pp)

    for k in range(0, len(pp)):
        detail_row = pp[k]  # selected  one raw from the input detail table
        # print(detail_row)

        sub_code = pp[k][0]
        # print(sub_code)

        cap = (capacity(sub_code))
        # print(cap)

        blockType = (block(sub_code))
        # print(blockType)

        book_room = (room(cap, blockType))
        # print(book_room)
        book_room_L1 = book_room[0]

        book_room_L2 = book_room[1]
        # print(type(book_room_L1))
        # print("book_room_L1 : ", book_room_L1)
        # print("book_room_L2 : ", book_room_L2)
        # print(type(book_room_L2[0]))

        sorting = sort(book_room_L1, book_room_L2)
        # print(sorting)

        storing = store(book_room_L1, detail_row)

        # print("book room no. : ", book_room_L1)
        # print("book room cap : ", book_room_L2, "\n")

        # print("---------------------------------------------------------------------------")

fyctec = (storing[0])
fyetec = (storing[1])
fycs = (storing[2])

syctec = (storing[4])
syetec = (storing[5])
sycs = (storing[6])

ty_ctnt = (storing[8])
ty_gani = (storing[9])
ty_swst = (storing[10])

ty_etmp = (storing[12])
ty_etia = (storing[13])
ty_etst = (storing[14])

ty_csci = (storing[15])
ty_csec = (storing[16])
ty_aint = (storing[17])
ty_dsci = (storing[18])
ty_scom = (storing[19])

# print('  First_year_CT', "\n", fyct, "\n", 'First_year_ET', "\n", fyet, "\n", 'First_year_CS', "\n", fycs, '\n')
# print(syct, "\n", syet, "\n", sycs)

df_fy_ct = pd.DataFrame(fyctec)
df_fy_et = pd.DataFrame(fyetec)
df_fy_cs = pd.DataFrame(fycs)

df_sy_ct = pd.DataFrame(syctec)
df_sy_et = pd.DataFrame(syetec)
df_sy_cs = pd.DataFrame(sycs)

df_ty_ctnt = pd.DataFrame(ty_ctnt)
df_ty_gani = pd.DataFrame(ty_gani)
df_ty_swst = pd.DataFrame(ty_swst)

df_ty_etmp = pd.DataFrame(ty_etmp)
df_ty_etia = pd.DataFrame(ty_etia)
df_ty_etst = pd.DataFrame(ty_etst)

df_ty_csci = pd.DataFrame(ty_csci)
df_ty_csec = pd.DataFrame(ty_csec)
df_ty_aint = pd.DataFrame(ty_aint)
df_ty_dsci = pd.DataFrame(ty_dsci)
df_ty_scom = pd.DataFrame(ty_scom)

with pd.ExcelWriter("TimeTable (First_Year).xlsx") as writer:
    df_fy_ct.to_excel(writer, sheet_name='First_year_CTEC')
    df_fy_et.to_excel(writer, sheet_name="First_year_ETEC")
    df_fy_cs.to_excel(writer, sheet_name='First_year_CSCI')

with pd.ExcelWriter("TimeTable (Second_Year).xlsx") as writer:
    df_sy_ct.to_excel(writer, sheet_name='Second_year_CTEC')
    df_sy_et.to_excel(writer, sheet_name='Second_year_ETEC')
    df_sy_cs.to_excel(writer, sheet_name='Second_year_CSCI')

with pd.ExcelWriter("TimeTable (Third_Year).xlsx") as writer:
    df_ty_ctnt.to_excel(writer, sheet_name='Third_year_CTNT')
    df_ty_gani.to_excel(writer, sheet_name='Third_year_GANI')
    df_ty_swst.to_excel(writer, sheet_name='Third_year_SWST')

    df_ty_etmp.to_excel(writer, sheet_name='Third_year_ETMP')
    df_ty_etia.to_excel(writer, sheet_name='Third_year_ETIA')
    df_ty_etst.to_excel(writer, sheet_name='Third_year_ETST')

    df_ty_csci.to_excel(writer, sheet_name='Third_year_CSCI')
    df_ty_csec.to_excel(writer, sheet_name='Third_year_CSEC')
    df_ty_aint.to_excel(writer, sheet_name='Third_year_AINT')
    df_ty_dsci.to_excel(writer, sheet_name='Third_year_DSCI')
    df_ty_scom.to_excel(writer, sheet_name='Third_year_SCOM')


pd.options.display.max_columns = None
pd.options.display.width = 1000

# print('  First_year_CT', "\n", df_fy_ct, "\n", 'First_year_ET', "\n", df_fy_et, "\n", 'First_year_CS', "\n", df_fy_cs,
#      '\n')

# print("_____________________________________________________________________________________________________________")

# print('Second_year_CT', '\n', df_sy_ct, "\n", 'Second_year_ET', '\n', df_sy_et, "\n", 'Second_year_CS', '\n', df_sy_cs)
# print("_____________________________________________________________________________________________________________")

# print('Third_year_ETMP', "\n",df_ty_etmp )