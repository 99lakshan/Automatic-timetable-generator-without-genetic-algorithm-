import pandas as pd


def capacity(sub_code):
    cap = pd.read_csv("Data/2nd_Sem_Course_codes.csv")
    filtered_cap = cap.loc[cap['Course_Code'] == sub_code]
    value = filtered_cap.iloc[0]['capacity']
    # print(value)

    return value


def block(sub_code):
    blocktype = pd.read_csv("Data/2nd_Sem_Course_codes.csv")
    filtered_blocktype = blocktype.loc[blocktype['Course_Code'] == sub_code]
    value1 = filtered_blocktype.iloc[0]['block_type']
    # print(value1)

    return value1


#print(capacity('GTEC1123'))