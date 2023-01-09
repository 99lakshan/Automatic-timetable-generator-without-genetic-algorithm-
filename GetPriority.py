import numpy as np
import pandas as pd

def Get(x , data_new):
    count = 0
    prio_list = []
    for i in range(0, (len(data_new))):
        data_new['prio_level'][i]
        if (data_new['prio_level'][i] == x):
            # print(data_new[cols].loc[i])

            prio_list.append(data_new.loc[
                                 [i], ['CC_CODE', 'LEC_CODE', 'TIME_SLOT1', 'TIME_SLOT2', 'TIME_SLOT3']])
            # prio_list.append(a)
            count = count + 1

    print("count is : ", count)

    arr = np.array(prio_list).reshape(count,6)

    return (arr)