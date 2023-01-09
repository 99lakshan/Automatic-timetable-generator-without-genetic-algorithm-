# this file is not nessosery bcz if we type our input data in csv file there is no need to use this.

import pandas as pd

CC_list = ['CC_CODE']
LC_list = ['LEC_CODE']
TS1_list = ['TIME_SLOT1']
TS2_list = ['TIME_SLOT2']
TS3_list = ['TIME_SLOT3']
TS4_list = ['TIME_SLOT4']
def inputs(Answer):


    day = pd.read_csv("Data/Day_arrangement.csv")
    print("This is the time slot table that you have to type below in exact same arrangement as in the table\n",day)

    print("\ntype 0 in Course code if you finish the process\n")

    for i in range(0,100):
        CC = str(input("Enter your Course Code : "))
        if (CC=="0"):
            break
        CC_list.append(CC)

        LC = str(input("Enter your Lecturer Code : "))
        LC_list.append(LC)

        TS1 = str(input("Enter your Preffered 1st time slot : "))
        TS1_list.append(TS1)
        TS2 = str(input("Enter your Preffered 2nd time slot : "))
        TS2_list.append(TS2)
        TS3 = str(input("Enter your Preffered 3rd time slot : "))
        TS3_list.append(TS3)
#        TS4 = str(input("Enter your Preffered 4th time slot : "))
#        TS4_list.append(TS4)

    Input_table = [CC_list,LC_list,TS1_list,TS2_list,TS3_list]
    #print(Input_table)

    DF = pd.DataFrame(Input_table)
    new_DF = DF.T
    #print(new_DF)

    headers = new_DF.iloc[0]
    new_DF = pd.DataFrame(new_DF.values[1:],columns=headers)

    new_DF.to_csv("input2.csv",index=False)
    return(new_DF)