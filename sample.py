def arrangeDataAccMarks():
    am_marksfile_r = open("marks.txt", "r")
    am_stufile_r = open("stufile.txt", "r")
    am_rollfile_r = open("rollnum.txt", "r")
    am_namesfile_r = open("names.txt", "r")
    am_repeated_rollfile_r = open("repeated_roll.txt", "r")
    am_marks_list = am_marksfile_r.readlines()
    am_stu_list = am_stufile_r.readlines()
    am_roll_list = am_rollfile_r.readlines()
    am_names_list = am_namesfile_r.readlines()
    am_repeated_roll_list = am_repeated_rollfile_r.readlines()
    am_avail_marks = []
    am_avail_roll = []
    am_sorted_stu = []
    am_sorted_roll = []
    am_sorted_names = []
    am_marks_index_before = []
    am_marks_index_after = []
    am_repeated_roll_index_before = []
    am_repeated_roll_index_after = []
    print(am_stu_list)
    print(am_marks_list)
    
    if am_repeated_roll_list != []:
        for am_x in am_repeated_roll_list:
            am_repeated_roll_index_before.append(am_roll_list.index(am_x))

    for am_i in am_marks_list:
        am_avail_marks.append(int(am_i.rstrip("\n")))
    
    for am_o in am_roll_list:
        am_avail_roll.append(int(am_o.rstrip("\n")))


    for am_j in am_avail_marks:
        am_marks_index_before.append(am_marks_list.index(f"{am_j}\n"))


    print(am_marks_index_before)

    am_avail_marks.sort()
    print(am_avail_marks)
    for am_k in am_avail_marks:
        am_marks_index_after.append(am_marks_list.index(f"{am_k}\n"))
    print(am_marks_index_after)

    for am_l in am_marks_index_after:
        print(am_l)
        am_sorted_stu.append(am_stu_list[am_l])

    print(am_sorted_stu)

    for am_p in am_marks_index_after:
        am_sorted_roll.append(am_roll_list[am_p])

    for am_r in am_marks_index_after:
        am_sorted_names.append(am_names_list[am_r])

    print(am_sorted_names)


    if am_repeated_roll_list != []:
        for am_y in am_repeated_roll_list:
            am_repeated_roll_index_after.append(am_sorted_roll.index(int(am_y.rstrip("\n"))))
    print(am_stu_list)
    print(am_repeated_roll_index_before)
    print(am_repeated_roll_index_after)
    if am_repeated_roll_list != []:
        for am_z_1 in am_repeated_roll_index_after:
            am_sorted_stu.pop(am_z_1)
            am_sorted_roll.pop(am_z_1)
            am_sorted_names.pop(am_z_1)

        for am_z_2 in am_repeated_roll_index_before:
            am_sorted_stu.append(am_stu_list[am_z_2])
            am_sorted_roll.append(am_roll_list[am_z_2])
            am_sorted_names.append(am_names_list[am_z_2])




    am_marksfile_w = open("marks.txt", "w")
    for am_m in am_avail_marks:
        am_marksfile_w.write(f"{am_m}\n")
    am_marksfile_w.close()

    am_stufile_w = open("stufile.txt", "w")
    for am_n in am_sorted_stu:
        am_stufile_w.write(f"{am_n}")

    am_stufile_w.close()

    am_rollfile_w = open("rollnum.txt", "w")
    for am_q in am_sorted_roll:
        am_rollfile_w.write(f"{am_q}")
    am_rollfile_w.close()


    am_namesfile_w = open("names.txt", "w")
    for am_s in am_sorted_names:
        am_namesfile_w.write(am_s)

    am_namesfile_w.close()

    am_rollfile_r.close()
    am_marksfile_r.close()
    am_stufile_r.close()
    am_namesfile_r.close()

    am_repeated_rollfile_r.close()