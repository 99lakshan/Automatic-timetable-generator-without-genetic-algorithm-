import pandas as pd

CC_list = ['CC_CODE']
LC_list = ['LEC_CODE']
TS1_list = ['TIME_SLOT1']
TS2_list = ['TIME_SLOT2']
TS3_list = ['TIME_SLOT3']

def inputs(Answer):
    day = pd.read_csv("Data/Day_arrangement.csv")
    print("This is the time slot table that you have to type below in exact same arrangement as in the table\n", day)

    print("\ntype 0 in Course code if you finish the process\n")

    for i in range(0, 1000):
        CC = str(input("Enter your Course Code : "))
        if CC == "0":
            break
        CC_list.append(CC)

        LC = str(input("Enter your Lecturer Code : "))
        LC_list.append(LC)

        TS1 = str(input("Enter your Preferred 1st time slot : "))
        TS1_list.append(TS1)
        TS2 = str(input("Enter your Preferred 2nd time slot : "))
        TS2_list.append(TS2)
        TS3 = str(input("Enter your Preferred 3rd time slot : "))
        TS3_list.append(TS3)

    Input_table = [CC_list, LC_list, TS1_list, TS2_list, TS3_list]

    DF = pd.DataFrame(Input_table)
    new_DF = DF.T
    print(new_DF)

    headers = new_DF.iloc[0]
    new_DF = pd.DataFrame(new_DF.values[1:], columns=headers)

    try:
        existing_df = pd.read_csv("input2.csv")
        combined_df = pd.concat([existing_df, new_DF], ignore_index=True)
        combined_df.to_csv("input2.csv", index=False)
    except FileNotFoundError:
        new_DF.to_csv("input2.csv", index=False)

    return new_DF
