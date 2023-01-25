import pandas as pd

from finalstore import *


def capacity(sub_code):  # 1
    cap = pd.read_csv("Data/2nd_Sem_Course_codes.csv")
    filtered_cap = cap.loc[cap['Course_Code'] == sub_code]
    value = filtered_cap.iloc[0]['capacity']
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx  ", value)

    return value


def block(sub_code):  # 2
    blocktype = pd.read_csv("Data/2nd_Sem_Course_codes.csv")
    filtered_blocktype = blocktype.loc[blocktype['Course_Code'] == sub_code]
    value1 = filtered_blocktype.iloc[0]['block_type']
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@", value1)

    return value1


def room(cap, blockType, pp):  # 3
    store = []
    given_room = []
    given_room_cap = []

    suitroom = pd.read_csv("Data/room_table.csv")
    for i in range(0, len(suitroom)):
        A = suitroom['Room_No'][i][:2]
        B = str(A)

        if B == blockType:
            store.append(suitroom['Room_No'][i])

    for j in range(0, len(store)):
        filtered_suitroom = suitroom.loc[suitroom['Room_No'] == store[j]]
        value2 = filtered_suitroom.iloc[0]['capacity']

        x = int(value2)
        y = int(cap)

        if x >= y:
            value3 = store[j]
            print("capacity of selected course : ", y, " capacity of lecture hall : ", x)
            given_room_cap.append(x)
            given_room.append(value3)

    # sorting = sort(book_room_L1, book_room_L2, pp)

    return given_room, given_room_cap


# ----------------------------------------------------------------------------

def sort(book_room_L1, book_room_L2):  # 4
    for i in range(0, len(book_room_L2)):
        for j in range(0, len(book_room_L2)):
            if i == j:
                continue

            if book_room_L2[i] < book_room_L2[j]:
                c = book_room_L2[i]
                d = book_room_L1[i]

                book_room_L2[i] = book_room_L2[j]
                book_room_L1[i] = book_room_L1[j]

                book_room_L2[j] = c
                book_room_L1[j] = d

    print("book room no. : ", book_room_L1)
    print("book room cap : ", book_room_L2, "\n")

    #storing = store(book_room_L1, book_room_L2, detail_row, pp)
    #print(storing)

    return book_room_L1, book_room_L2, #storing

