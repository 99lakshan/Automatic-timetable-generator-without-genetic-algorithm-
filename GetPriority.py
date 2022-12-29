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
                                 [i], ['subject_code', 'lecturer_code', 'day', 'session_no', 'white_board', 'projector',
                                       'computers', 'capacity']])
            # prio_list.append(a)
            count = count + 1

    print("count is : ", count)

    arr = np.array(prio_list).reshape(count, 8)

    return (arr)