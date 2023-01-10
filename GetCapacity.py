import pandas as pd


def capacity(sub_code):
    cap = pd.read_csv("Data/2nd_Sem_Course_codes.csv")
    filtered_cap = cap.loc[cap['Course_Code'] == sub_code]
    value = filtered_cap.iloc[0]['capacity']
    # print(value)

    return value
