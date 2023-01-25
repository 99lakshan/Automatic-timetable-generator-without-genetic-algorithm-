from GetPriority import *
from Enterinputs import *
from GetCapacity import *
from finalstore import *

Answer = str(input("Do you want to enter your data :(y/n) : "))

if Answer == "y":
    x = inputs(Answer)
else:
    pass

input2 = pd.read_csv("Data/input2.csv")
# print(input2)
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

# print(data_new)
# print(len(lec_detail))

# sam_list = []
# sub = []
for j in range(1, (len(lec_detail) + 1)):
    # print(j)
    out = (Get(j, data_new))
    # print(out)
    if len(out) == 0:
        # print("This is empty")
        continue

    pp = out.tolist()                               # pp - input detail table
    print(pp)

    for k in range(0, len(pp)):
        detail_row = pp[k]                          # selected  one raw from the input detail table
        print(detail_row)

        sub_code = pp[k][0]
        # print(sub_code)

        cap = (capacity(sub_code))
        # print(cap)

        blockType = (block(sub_code))
        # print(blockType)

        book_room = (room(cap, blockType, pp))
        print(book_room)
        book_room_L1 = book_room[0]

        book_room_L2 = book_room[1]
        # print(type(book_room_L1))
        # print("book_room_L1 : ", book_room_L1)
        # print("book_room_L2 : ", book_room_L2)
        # print(type(book_room_L2[0]))

        sorting = sort(book_room_L1, book_room_L2)
        print(sorting)

        storing = store(book_room_L1, book_room_L2, detail_row)

        print("book room no. : ", book_room_L1)
        # print("book room cap : ", book_room_L2, "\n")

        print("---------------------------------------------------------------------------")

fy = (storing[0])
sy = (storing[1])
ty = (storing[2])

df_fy = pd.DataFrame(fy)
# df_fy = df_fy.T

df_sy = pd.DataFrame(sy)
# df_sy = df_sy.T

df_ty = pd.DataFrame(ty)
# df_ty = df_ty.T

pd.options.display.max_columns = None
pd.options.display.width = 1000

print("First year\n", df_fy, "\n\n","Second year\n", df_sy, "\n\n", "Third year\n", df_ty)