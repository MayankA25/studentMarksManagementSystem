import pyttsx3
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def enterData():
    
        e_roll_list = []
        e_stufile = open("stufile.txt", 'a')
        e_rollfile_r = open("rollnum.txt", "r")
        e_rollfile_w = open("rollnum.txt", "a")
        e_marksfile_r = open("marks.txt", "r")
        e_marksfile_w = open("marks.txt", "a")
        e_namefile_w = open("names.txt", "a")

        # e_repeated_roll_w = open("repeated_roll.txt", "a")

        e_marks_list = e_marksfile_r.readlines()
        while True:
            
            e_roll_list.extend(e_rollfile_r.readlines())
            
            # print(e_roll_list)
            try:
                e_rollnum = int(input("Enter a new Roll No.: ")) 
            except Exception as e:
                print("Error! Enter numbers")
                break

            if f"{e_rollnum}\n" not in e_roll_list:
                try:
                    e_name = input("Enter name: ")
                except Exception as e:
                    print("Error! Enter letters!")
                    break
        
        
                try:
                    e_marks = int(input("Enter marks: "))
                except Exception as e:
                    print("Error! Enter numbers!")
                    break
                e_stufile.write(f"RollNo.: {e_rollnum}          Name: {e_name}          Marks: {e_marks}\n")
                e_rollfile_w.write(f"{e_rollnum}\n")
                e_marksfile_w.write(f"{e_marks}\n")
                e_namefile_w.write(f"{e_name}\n")

                # if f"{e_marks}\n" in e_marks_list:
                #     e_repeated_roll_w.write(f"{e_rollnum}\n")
            else:
                print(f"Roll number {e_rollnum} is already present! Please Enter a new one!")
                newRecord()
                break

            e_stufile.close()
            e_rollfile_r.close()
            e_rollfile_w.close()
            e_marksfile_r.close()
            e_marksfile_w.close()
            e_namefile_w.close()

            # e_repeated_roll_w.close()

            e_ask = input("Do you want to enter more records? (y/n): ")
            if e_ask.lower() == "y":
                enterData()

            else:
                choice()
                exit()
        
        


# open("rollnum.txt", "w")
# open("stufile.txt", "w")
def newRecord():
        n_roll_list = []
        n_stufile = open("stufile.txt", "a")
        n_rollfile_r = open("rollnum.txt", "r")
        n_rollfile_w = open("rollnum.txt", "a")
        n_marksfile_r = open("marks.txt", "r")
        n_marksfile_w = open("marks.txt", "a")
        n_namefile_w = open("names.txt", "a")
        # n_repeated_roll_w = open("repeated_roll.txt", "a")

        n_marks_list = n_marksfile_r.readlines()
        while True:
            n_roll_list.extend(n_rollfile_r.readlines())
            
            try:
                n_rollnum = int(input("Enter a new Roll No.: "))
            except Exception as e:
                print("Error! Enter numbers")
                break
            if f"{n_rollnum}\n" not in n_roll_list:
                try:
                    n_name = input("Enter name: ")
                except Exception as e:
                    print("Error! Enter Letters!")
                    break

                try:
                    n_marks = int(input("Enter Marks: "))
                except Exception as e:
                    print("Error! Enter numbers!")
                    break
                n_stufile.write(f"RollNo.: {n_rollnum}          Name: {n_name}          Marks: {n_marks}\n")
                n_rollfile_w.write(f"{n_rollnum}\n")
                n_marksfile_w.write(f"{n_marks}\n")
                n_namefile_w.write(f"{n_name}\n")

                # if f"{n_marks}\n" in n_marks_list:
                #     n_repeated_roll_w.write(f"{n_rollnum}\n")


            else:
                print(f"Roll number {n_rollnum} is already present! Please enter a new one.")
                enterData()
                break
            n_stufile.close()
            n_rollfile_r.close()
            n_rollfile_w.close()
            n_marksfile_r.close()
            n_marksfile_w.close()
            n_namefile_w.close()

            # n_repeated_roll_w.close()

            n_ask = input("Do you want to enter more records? (y/n): ")
            if n_ask.lower() == "y":
                newRecord()
            else:
                choice()
                exit()
        
                
        
def displayData():
    d_stufile = open("stufile.txt", "r")
    d_rollfile = open("rollnum.txt", "r")
    d_stu_list = d_stufile.readlines()
    d_roll_list = d_rollfile.readlines()
    d_avail_roll = []
    for d_i in d_roll_list:
        d_avail_roll.append(int(d_i.rstrip("\n")))
    while True:
        print(d_avail_roll)
        d_rollnum = int(input("Enter the roll number to display the record: "))
        if f"{d_rollnum}\n" in d_roll_list:
            d_index = d_roll_list.index(f"{d_rollnum}\n")
            print("\n")
            print(d_stu_list[d_index])
            d_ask = input("Do you want to see more records? (y/n): ")
            if d_ask.lower() == "y":
                continue
            else:
                choice()
                break

        else:
            print(f"Roll number {d_rollnum} is not present. Please check if the roll number is correct or not")
            exit()

    d_stufile.close()
    d_rollfile.close()

def modifyData():
    m_stufile_r = open("stufile.txt", "r")
    m_rollfile = open("rollnum.txt", "r")
    m_namesfile_r = open("names.txt", "r")
    m_marksfile_r = open("marks.txt", "r")
    m_stu_list = m_stufile_r.readlines()
    m_roll_list = m_rollfile.readlines()
    m_names_list = m_namesfile_r.readlines()
    m_marks_list = m_marksfile_r.readlines()
    print(m_marks_list)
    print(m_names_list)
    m_avail_roll = []
    for m_i in m_roll_list:
        m_avail_roll.append(int(m_i.rstrip("\n")))
    while True:
        print(m_avail_roll)
        m_rollnum = int(input("Enter the roll number to modify: "))
        if f"{m_rollnum}\n" in m_roll_list:
            m_index = m_roll_list.index(f"{m_rollnum}\n")
            try:
                m_name = input("Enter new name: ") 
            except Exception as e:
                print("Some Error Occurred!")
                break

            try:
                m_marks = int(input("Enter new marks: "))

            except Exception as e:
                print("Some Error Occurred!")
                break
            m_details = f"Roll No.: {m_rollnum}         Name: {m_name}          Marks: {m_marks}\n"
            m_stu_list.pop(m_index)
            m_stu_list.insert(m_index, m_details)

            m_names_list.pop(m_index)
            m_names_list.insert(m_index, f"{m_name}\n")

            m_marks_list.pop(m_index)
            m_marks_list.insert(m_index, f"{m_marks}\n")


            m_stufile_w = open("stufile.txt", "w")
            for m_j in m_stu_list:
                m_stufile_w.write(m_j)

            m_stufile_w.close()

            m_namesfile_w = open("names.txt", "w")
            for m_k in m_names_list:
                m_namesfile_w.write(f"{m_k}")
            m_namesfile_w.close()

            m_marksfile_w = open("marks.txt", "w")
            for m_l in m_marks_list:
                m_marksfile_w.write(f"{m_l}")
            m_marksfile_w.close()           

            m_ask = input("Do you want to modify more records? (y/n): ")
            if m_ask.lower() == "y":
                continue
            else:
                m_stufile_r.close()
                m_rollfile.close()
                choice()
                break

        else:
            print(f"Roll number {m_rollnum} is not present!")
            m_stufile_r.close()
            m_rollfile.close()
            break

    


def deleteData():
    de_stufile_r = open("stufile.txt", "r")
    de_rollfile_r  = open("rollnum.txt", "r")
    de_namesfile_r = open("names.txt", "r")
    de_marksfile_r = open("marks.txt", "r")
    de_roll_list = de_rollfile_r.readlines()
    de_stu_list = de_stufile_r.readlines()
    de_names_list = de_namesfile_r.readlines()
    de_marks_list = de_marksfile_r.readlines()
    de_avail_roll = []
    for de_i in de_roll_list:
        de_avail_roll.append(int(de_i.rstrip("\n")))
    while True:
        print(de_avail_roll)
        de_rollnum = int(input("Enter the roll number to delete the record: "))
        if f"{de_rollnum}\n" in de_roll_list:
            de_index = de_roll_list.index(f"{de_rollnum}\n")
            de_stu_list.pop(de_index)
            de_roll_list.pop(de_index)
            de_avail_roll.pop(de_index)
            de_names_list.pop(de_index)
            de_marks_list.pop(de_index)
            de_stufile_w = open("stufile.txt", "w")
            for de_i in de_stu_list:
                de_stufile_w.write(de_i)

            de_stufile_w.close()

            de_roll_file_w = open("rollnum.txt", "w")
            for de_j in de_roll_list:
                de_roll_file_w.write(de_j)

            de_roll_file_w.close()

            de_names_file_w = open("names.txt", "w")
            for de_l in de_names_list:
                de_names_file_w.write(de_l)
            de_names_file_w.close()

            de_marks_file_w = open("marks.txt", "w")
            for de_k in de_marks_list:
                de_marks_file_w.write(de_k)
            de_marks_file_w.close()
            print("Record deleted!")
            de_ask = input("Do you want to delete more records? (y/n): ")
            if de_ask.lower() == "y":
                continue
            else:
                de_stufile_r.close()
                de_rollfile_r.close()
                de_namesfile_r.close()
                de_marksfile_r.close()
                choice()
                break

        else:
            print(f"Roll number {de_rollnum} not found!")
            de_stufile_r.close()
            de_rollfile_r.close()
            break

def arrangeDataAccRoll():
    ar_stufile_r = open("stufile.txt", "r")
    a_rollffile_r = open("rollnum.txt", "r")
    

    a_namesfile_r = open("names.txt", "r")
    a_marksfile_r = open("marks.txt", "r")
    
    a_stu_list = ar_stufile_r.readlines()
    a_roll_list = a_rollffile_r.readlines()


    a_names_list = a_namesfile_r.readlines()
    a_marks_list = a_marksfile_r.readlines()
    
    
    a_sorted_stu_list = []


    a_sorted_names_list = []
    a_sorted_marks_list = []
    
    
    a_avail_roll = []


    # a_avail_names = []
    # a_avail_marks = []
    
    
    a_roll_index_before = []
    a_roll_index_after = []
    for a_i in a_roll_list:
        a_avail_roll.append(int(a_i.rstrip("\n")))


    # for a_i_2 in a_marks_list:
    #     a_avail_names.append(int(a_i_2.rstrip("\n")))
    # for a_i_3 in a_names_list:
    #     a_avail_marks.append(a_i_3)
    
    
    # print(a_avail_roll)
    # print(a_roll_list)
    for a_j in a_avail_roll:
        a_roll_index_before.append(a_roll_list.index(f"{a_j}\n"))
    
    # print(a_roll_index_before)


    a_avail_roll.sort()
    # print(a_avail_roll)
    for a_k in a_avail_roll:
        a_roll_index_after.append(a_roll_list.index(f"{a_k}\n"))

    # print(a_roll_index_after)
    for a_l in a_roll_index_after:
        # print(a_stu_list[a_l])
        a_sorted_stu_list.append(a_stu_list[a_l])
        a_sorted_names_list.append(a_names_list[a_l])
        a_sorted_marks_list.append(a_marks_list[a_l])

    # print(a_sorted_stu_list)

    a_sorted_rollfile = open("rollnum.txt", "w")
    for a_m in a_avail_roll:
        a_sorted_rollfile.write(f"{a_m}\n")

    a_sorted_rollfile.close()
    a_sorted_stufile = open("stufile.txt", "w")
    for a_n in a_sorted_stu_list:
        a_sorted_stufile.write(a_n)
    a_sorted_stufile.close()  

    a_sorted_namesfile = open("names.txt", "w")
    for a_o in a_sorted_names_list:
        a_sorted_namesfile.write(a_o)
    a_sorted_namesfile.close()


    a_sorted_marksfile = open("marks.txt", "w")
    for a_p in a_sorted_marks_list:
        a_sorted_marksfile.write(a_p)
    a_sorted_marksfile.close()
    
    ar_stufile_r.close()
    a_rollffile_r.close()

def arrangeDataAccMarks():
    am_rollfile_r = open("rollnum.txt", "r")
    am_stufile_r = open("stufile.txt", "r")
    am_namesfile_r = open("names.txt", "r")
    am_marksfile_r = open("marks.txt", "r")

    am_roll_list = am_rollfile_r.readlines()
    am_stu_list = am_stufile_r.readlines()
    am_names_list = am_namesfile_r.readlines()
    am_marks_list = am_marksfile_r.readlines()

    am_stu_dict = {

    }
    am_names_dict = {

    }
    am_marks_dict = {

    }

    for am_i in range(len(am_roll_list)):
        am_stu_dict.update({int(am_roll_list[am_i].rstrip("\n")):am_stu_list[am_i]})
        am_names_dict.update({int(am_roll_list[am_i].rstrip("\n")):am_names_list[am_i]})
        am_marks_dict.update({int(am_roll_list[am_i].rstrip("\n")):int(am_marks_list[am_i].rstrip("\n"))})


    am_marks_dict_keys = list(am_marks_dict.keys())
    am_marks_dict_values_1 = list(am_marks_dict.values())

    am_marks_dict_values_1.sort()
    am_marks_dict_values = am_marks_dict_values_1[::-1]
    am_marks_indexes = []
    for am_j in am_marks_dict_values:
        am_marks_index = am_marks_list.index(f"{am_j}\n")
        am_marks_indexes.append(am_marks_index)
        am_marks_list.pop(am_marks_index)
        am_marks_list.insert(am_marks_index, " ")

    print(am_marks_indexes)
    am_sorted_roll = []

    for am_k in am_marks_indexes:
        am_roll = int(am_roll_list[am_k].rstrip("\n"))
        am_sorted_roll.append(am_roll)
    am_rollfile_w = open("rollnum.txt", "w")
    am_stufile_w = open("stufile.txt", "w")
    am_namesfile_w = open("names.txt","w")
    am_marksfile_w = open("marks.txt", "w")

    for am_l in am_sorted_roll:
        am_rollfile_w.write(f"{am_l}\n")
        am_stufile_w.write(am_stu_dict[am_l])
        am_namesfile_w.write(am_names_dict[am_l])
        am_marksfile_w.write(f"{am_marks_dict[am_l]}\n")


    
    am_rollfile_w.close()
    am_stufile_w.close()
    am_namesfile_w.close()
    am_marksfile_w.close()



    am_rollfile_r.close()
    am_stufile_r.close()
    am_namesfile_r.close()
    am_marksfile_r.close()
    

# arrangeDataAccMarks()


# arrangeDataAccMarks()




def choice():
    
    while True:
        choice_str = input("What do you want to do? Enter 1{Enter new data} 2{Add more records} 3{display records} 4{modify records} 5{delete records} 6{display all records} 7{clear file} exit{to exit program} 8{to arrange data roll number wise} 9{to arrange data marks wise}: ")
        if choice_str == '1':
            c_stufile_1 = open("stufile.txt", "r")
            if c_stufile_1.read() == "":
                c_stufile = open("stufile.txt", "w")
                c_rollfile = open("rollnum.txt", "w")
                c_marksfile = open("marks.txt", "w")
                c_namesfile = open("names.txt", "w")
                c_repeated_rollfile = open("repeated_roll.txt", "w")

                c_marksfile.close()
                c_stufile.close()
                c_rollfile.close()
                c_namesfile.close()
                c_repeated_rollfile.close()
                enterData()
                print("Records entered successfully")
                speak("Records entered successfully")

            else:
                c_ask_1 = input("The file contains data, by proceeding it will clear the file and takes new data. Do you want to continue? (y/n): ")
                if c_ask_1.lower() == "y":
                    c_stufile = open("stufile.txt", "w")
                    c_rollfile = open("rollnum.txt", "w")
                    c_marksfile = open("marks.txt", "w")
                    c_namesfile = open("names.txt", "w")
                    c_repeated_rollfile = open("repeated_roll.txt", "w")
                    c_stufile.close()
                    c_rollfile.close()
                    c_marksfile.close()
                    c_namesfile.close()
                    c_repeated_rollfile.close()
                    enterData()
                    print("Records entered successfully")
                    speak("Records entered successfully")

                else:
                    choice()

            c_stufile_1.close()
            choice()

        elif choice_str == "2":
            newRecord()
            print("Records entered successfully")
            speak("Records entered successfully")

        elif choice_str == "3":
            speak("Displaying Data")
            time.sleep(1)
            displayData()


        elif choice_str == "4":
            modifyData()
            speak("Data modified!")

        elif choice_str == "5":
            deleteData()
            speak("Data deleted!")

        elif choice_str == "6":
            speak("Displaying all data")
            c_stufile_r = open("stufile.txt", "r")
            print(f"Present records are:\n{c_stufile_r.read()}")
            c_stufile_r.close()
            choice()
            break

        elif choice_str == "7":
            c_stufile_7 = open("stufile.txt", "w")
            c_rollfile_7 = open("rollnum.txt", "w")
            c_stufile_7.close()
            c_rollfile_7.close()
            print("File cleared")
            speak("File cleared")

        elif choice_str == "8":
            arrangeDataAccRoll()
            print("Data arranged according to roll numbers!")
            speak("Data arranged according to roll numbers!")

        elif choice_str == "9":
            arrangeDataAccMarks()
            print("Data arranged according to marks!")
            speak("Data arranged according to marks!")

        elif choice_str.lower() == "exit":
            print("Program exited successfully!")
            speak("Program exited successfully!")
            exit()
        
        

        
        # c_ask = input("Do you want to do more operations? (y/n): ")
        # if c_ask.lower() == "y":
        #     continue
        # else:
        #     print("Program exited!")
        #     exit()

# print(repeated_roll)
# speak("Enter 1 for entering new records, 2 for adding more to existing records, 3 to display records, 4 to modify records, 5 to delete records, 6 to display all the records, 7 to clear the file, 8 to arrange records roll number wise and 9 to arrange records marks wise hisghest to lowest")
choice()