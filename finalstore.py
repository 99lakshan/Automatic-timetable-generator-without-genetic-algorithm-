first_year = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
second_year = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
third_year = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

PR001 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PR002 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PR003 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PR004 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PR005 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PR006 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PR007 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PR008 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PR009 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
CL001 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
CL002 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
CL003 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
CL004 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
CL005 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
CH001 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
CH002 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PH001 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PH002 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
PH003 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def store(book_room_L1, book_room_L2, detail_raw):
    num = 1
    h = ' / '
    day = ['MO', 'TU', 'WE', 'TH', 'FR']
    slot = ['M1', 'M2', 'A1', 'A2']
    year = ['first_year', 'second_year', 'third_year']

    for i in range(0, 1):  # looping the raw of input details
        print(detail_raw)

        credit = int(detail_raw[i][8])
        yr_no = int(detail_raw[i][4])
        print(yr_no)
        if credit > 3:
            credit = 3

        for j in range(0, len(book_room_L2)):  # loop the book_room_L2
            print(book_room_L1[j])

            for k in range(2, 5):
                dy = detail_raw[k][:2]
                sl = detail_raw[k][3:]

                print("dy : ", dy)
                print("sl : ", sl)

                z = str(book_room_L1[j])
                # print(type(z))

                p = day.index(dy)
                q = slot.index(sl)

                if yr_no == 1:
                    y = year[0]

                elif yr_no == 2:
                    y = year[1]

                elif yr_no == 3:
                    y = year[2]

                val = globals()[z][p][q]
                yr = globals()[y][p][q]
                print("*****************", yr)

                for l in range(0, credit - 1):
                    if yr != 0:
                        continue

                    elif yr == 0:
                        if val == 0:


                            if num > credit:
                                print("enne na bokka")
                                continue
                            else:
                                globals()[y][p][q] = detail_raw[i] + h + z
                                globals()[z][p][q] = detail_raw[i] + h + z
                                num = num + 1

                    print("my_list :", globals()[z])

                print(l)

                print("lec_hall :", z, "/ day no. :", p, "/ session no :", q, "/ credit :", credit)

            print("------------------")

    return first_year, second_year, third_year  # continue from there

# methanin ehat krna ona dewal

#  - credit ganat lecture kiyk watenna oned kiyl check krnna one eka dala thiyenne  e unat wada na
#  - e slot eka wen wela thiyanawanm e wenuwat that ekk assign krnna one.
################################################################################# 3rd yr ekedi hall eka mulin check krl ita passe yra list eka check krnna
