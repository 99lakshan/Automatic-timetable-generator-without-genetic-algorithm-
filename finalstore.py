first_year_CT = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
first_year_ET = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
first_year_CS = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
first_year_GT = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

second_year_CT = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
second_year_ET = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
second_year_CS = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
second_year_GT = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

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
    global year_name
    num = 1
    h = ' / '
    day = ['MO', 'TU', 'WE', 'TH', 'FR']
    slot = ['M1', 'M2', 'A1', 'A2']
    year = ['first_year', 'second_year', 'third_year']

    yr_no = int(detail_raw[0][4])

    degree_programme = str(detail_raw[0][0:2])

    credit = int(detail_raw[0][8])

    if credit > 3:
        credit = 3

    if credit == 3:
        i = 2
    if credit > 3:
        i = 2
    if credit < 3:
        i = 1

    for j in range(0,
                   len(book_room_L1)):  # hall number eka gnne meken ekin eka  # onna list eken eka hall no ekk gaththa
        #print(book_room_L2)
        hall_id = str(book_room_L1[j])

        for k in range(2, 5):

            if yr_no == 1:
                year_name = year[0]

            elif yr_no == 2:
                year_name = year[1]

            elif yr_no == 3:
                year_name = year[2]
                continue  # temperary adding delete later

            dy = detail_raw[k][:2]  # meken piliwelat time slot 3na ekin eka gnnawa #dn eka time slot ekk gaththa
            sl = detail_raw[k][3:]  # e time slot eken day ekai slot ekai extract kr gaththa

            day_position = day.index(dy)
            slot_position = slot.index(sl)

            halls_list_value = globals()[hall_id][day_position][slot_position]
            g = str(year_name + '_' + degree_programme)
            #print(g)
            years_list_value = globals()[g][day_position][slot_position]

            if year_name != 'third_year':

                if degree_programme == 'ET':
                    if num == 3:
                        continue
                    if credit < 3:
                        if num == 2:
                            continue

                    if halls_list_value == 0:
                        if years_list_value == 0:
                            globals()[hall_id][day_position][slot_position] = detail_raw[0] + h + hall_id
                            d = str(year_name + '_' + degree_programme)
                            #print(d)
                            globals()[d][day_position][slot_position] = detail_raw[0] + h + hall_id
                            num = num + 1

                if degree_programme == 'CT':
                    if num == 3:
                        continue
                    if credit < 3:
                        if num == 2:
                            continue

                    if halls_list_value == 0:
                        if years_list_value == 0:
                            globals()[hall_id][day_position][slot_position] = detail_raw[0] + h + hall_id
                            d = str(year_name + '_' + degree_programme)
                            globals()[d][day_position][slot_position] = detail_raw[0] + h + hall_id
                            num = num + 1

                if degree_programme == 'CS':
                    if num == 3:
                        continue
                    if credit < 3:
                        if num == 2:
                            continue

                    if halls_list_value == 0:
                        if years_list_value == 0:
                            globals()[hall_id][day_position][slot_position] = detail_raw[0] + h + hall_id
                            d = str(year_name + '_' + degree_programme)
                            globals()[d][day_position][slot_position] = detail_raw[0] + h + hall_id
                            num = num + 1

                if degree_programme == 'GT':
                    if num == 3:
                        continue
                    if credit < 3:
                        if num == 2:
                            continue

                    if halls_list_value == 0:
                        if years_list_value == 0:
                            globals()[hall_id][day_position][slot_position] = detail_raw[0] + h + hall_id
                            e = str(year_name + '_' + 'ET')
                            c = str(year_name + '_' + 'CT')
                            d = str(year_name + '_' + degree_programme)
                            globals()[e][day_position][slot_position] = detail_raw[0] + h + hall_id
                            globals()[c][day_position][slot_position] = detail_raw[0] + h + hall_id
                            globals()[d][day_position][slot_position] = detail_raw[0] + h + hall_id

                            num = num + 1

            else:
                continue
            # if credit<3:
            #    for count in range(0,1):

    return first_year_CT, first_year_ET, first_year_CS, first_year_GT, second_year_CT, second_year_ET, second_year_CS, second_year_GT  # continue from there

# methanin ehat krna ona dewal

#  - credit ganat lecture kiyk watenna oned kiyl check krnna one eka dala thiyenne  e unat wada na
#  - e slot eka wen wela thiyanawanm e wenuwat that ekk assign krnna one.
################################################################################# 3rd yr ekedi hall eka mulin check krl ita passe yra list eka check krnna
