from time import sleep
import os

def menu():
    while (True):
        choice = input(
            "\n----------\nMenu: \n----------\n1.Vailable places at the hotel\n2.Date search\n3.Order a room\n4.Cancel reservation\n5.Search for an order and print the order invitation\n6.Rooms info \n--------------------\nEnter your choice: ")
        if (choice == "1"):
            Available()
        elif (choice == "2"):
            search_hotel()
        elif (choice == "3"):
            invitation_hotel()
        elif (choice == "4"):
            cancel_reserv()
        elif (choice == "5"):
            search_invitation()
        elif (choice == "6"):
            about_room()
        else:
            print("-----------\nEnter 1-5 ONLY Please!\n-----------")
            continue
        if (input("Do you want to Quit?\n \t yes/no\n") == "yes"):
            break
    sleep(1)
    print("Thanks and good bye!!!")

# ------------------------------ BUTTON NUMBER 1
def Available():
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
    print("--------------------------\nRooms available this week in Herdos:\n--------------------------")
    sleep(1)
    file = open(filename, "r+")
    print(file.read())
    print("----------------------")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
    file = open(filename, "r+")
    print(file.read())
    print("----------------------")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
    file = open(filename, "r+")
    print(file.read())
    print("----------------------")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
    file = open(filename, "r+")
    print(file.read())
    print("----------------------")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
    file = open(filename, "r+")
    print(file.read())
    sleep(3)
    print("\n")
    print("--------------------------\nRooms available this week in Setia:\n--------------------------")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
    file = open(filename, "r+")
    print(file.read())
    print("----------------------")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
    file = open(filename, "r+")
    print(file.read())
    print("----------------------")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
    file = open(filename, "r+")
    print(file.read())
    print("----------------------")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
    file = open(filename, "r+")
    print(file.read())
    print("----------------------")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
    file = open(filename, "r+")
    print(file.read())

    print("--------------------------\nWe'll move you to MENU in 5 seconds!\n--------------------------")
    sleep(5)

    return menu()
# ------------------------------ BUTTON NUMBER 2
def search_hotel():
    data = input("Enter day in week you want?\n")
    if data == ("sunday"):
        herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
        file = open(herods, "r")
        print("-----------\nHerods Hotel\n-----------")
        print(file.readlines()[0])
        setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
        file = open(setia, "r")
        print(("-----------\nSetia Hotel\n-----------"))
        print(file.readlines()[0])
    elif data == ("monday"):
        herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
        file = open(herods, "r")
        print("-----------\nHerods Hotel\n-----------")
        print(file.readlines()[0])
        setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
        file = open(setia, "r")
        print("-----------\nSetia Hotel\n-----------")
        print(file.readlines()[0])
    elif data == ("tuesday"):
        herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
        file = open(herods, "r")
        print("-----------\nHerods Hotel\n-----------")
        print(file.readlines()[0])
        setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
        file = open(setia, "r")
        print("-----------\nSetia Hotel\n-----------")
        print(file.readlines()[0])
    elif data == ("wednesday"):
        herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
        file = open(herods, "r")
        print("-----------\nHerods Hotel\n-----------")
        print(file.readlines()[0])
        setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
        file = open(setia, "r")
        print("-----------\nSetia Hotel\n-----------")
        print(file.readlines()[0])
    elif data == ("thursday"):
        herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
        file = open(herods, "r")
        print("-----------\nHerods Hotel\n-----------")
        print(file.readlines()[0])
        setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
        file = open(setia, "r")
        print("-----------\nSetia Hotel\n-----------")
        print(file.readline()[0])

    else:
        print("-----------\nEnter week days ONLY Please!\n-----------")


# ------------------------------ BUTTON NUMBER 3
def invitation_hotel():
    User_name = input("Hello, Enter you Full Name Please: ")
    filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
    file4 = open(filename, "a")
    file4.write("Full Name: " + User_name + "\n")
    file4.close()
    take_hotel = input("Hello you have 2 Hotels to choice: \n-----------------------\nHotel Herods! (5 Stars)\n-----------------------\nHotel Setia! (5 Stars)\n-----------------------\nEnter name of Hotel: ")
    if take_hotel == "herods":
        filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
        file5 = open(filename, "a")
        file5.write("Hotel: " + take_hotel + "\n")
        print("Welcome to Hotel Herods!!")
        sleep(1)
        a = input("Enter day you want to take: ")
        b = input("How many adult (1-3): ")
        c = input("How many kids: ")
        room1= ("Cuples room")
        room2=("Cuples+1 kid")
        room3=("Room for 3 adult")
        room4=("Cuples+2 kid")
        if a == "sunday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Sunday \nRoom take : room1" "\nPrice: 200 NIS\n")
                filename2 = "C:/Users/ויקטור/Desktop/Hotel_Project/forbutton4/" + User_name + ".txt"
                f = open(filename2, "a")
                f.write("Sunday : Room1, Room2, Room3, Room4")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")

        elif a == "sunday" and b == "2" and c == "0":
            sleep(1)
            print("The best room for you is Room1")
            answer1 = input("Do you want take room1?")
            if answer1 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Sunday\nRoom take : room1" "\nPrice: 200 NIS\n")
            elif answer1 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "sunday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Sunday\nRoom take : room3""\n Price: 350 NIS\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "sunday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Sunday\nRoom take : room4" "\nPrice: 350 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        #-------------------------------------------------------------
        elif a == "monday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
                file = open(herods, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Monday\nRoom take : room1" "\nPrice: 200 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "monday" and b == "2" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
                file = open(herods, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Monday\nRoom take : room1" "\n Price: 200 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "monday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Monday\nRoom take : room3" " Price: 350 NIS\n\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "monday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Monday\nRoom take : room4" "\n Price: 350 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        #-------------------------------------------------------------
        elif a == "tuesday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
                file = open(herods, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Tuesday\nRoom take : room1" "\nPrice: 200 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "tuesday" and b == "2" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
                file = open(herods, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Tuesday\nRoom take : room1" "\nPrice: 200 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "tuesday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Tuesday\nRoom take : room3" "\nPrice: 350 NIS\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "tuesday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Tuesday\nRoom take : room4" "\nPrice: 350 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        #----------------------------------------------------------------------------
        elif a == "wednesday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
                file = open(herods, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Wednesday\nRoom take : room1" "\n Price: 200 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "wednesday" and b == "2" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
                file = open(herods, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Wednesday\nRoom take : room1" "\n Price: 200 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "wednesday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Wednesday\nRoom take : room3" "\n Price: 350 NIS\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "wednesday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Wednesday\nRoom take : room4" "\n Price: 350 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        #_______________________________________________________________________
        elif a == "thursday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
                file = open(herods, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Thursday\nRoom take : room1" "\n Price: 200 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "thursday" and b == "2" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
                file = open(herods, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Thursday\nRoom take : room1" "\n Price: 200 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "thursday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Thursday\nRoom take : room3" "\nPrice: 350 NIS\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "thursday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                herods = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
                file = open(herods, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Thursday\nRoom take : room4" "\nPrice: 350 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
    elif take_hotel == "setia":
        filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
        file5 = open(filename, "a")
        file5.write("Hotel: " + take_hotel + "\n")
        print("Welcome to Hotel Setia!!")
        sleep(1)
        a = input("Enter day you want to take: ")
        b = input("How many adult: ")
        c = input("How many kids: ")
        room1 = ("Cuples room")
        room2 = ("Cuples+1 kid")
        room3 = ("Room for 3 adult")
        room4 = ("Cuples+2 kid")
        if a == "sunday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Sunday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")

        elif a == "sunday" and b == "2" and c == "0":
            sleep(1)
            print("The best room for you is Room1")
            answer1 = input("Do you want take room1?")
            if answer1 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Sunday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer1 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "sunday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Sunday\nRoom take : room3" "\n Price: 450 NIS\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "sunday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Sunday\nRoom take : room4" "\n Price: 660 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        #-------------------------------------------------------------
        elif a == "monday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
                file = open(setia, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Monday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "monday" and b == "2" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
                file = open(setia, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Monday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "monday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Monday\nRoom take : room3" "\n Price: 550 NIS\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "monday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Monday\nRoom take : room4" "\n Price: 660 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        #-------------------------------------------------------------
        elif a == "tuesday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
                file = open(setia, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Tuesday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "tuesday" and b == "2" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
                file = open(setia, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Tuesday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "tuesday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Tuesday\nRoom take : room3" "\n Price: 550 NIS\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "tuesday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Tuesday\nRoom take : room4" "\n Price: 660 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        #----------------------------------------------------------------------------
        elif a == "wednesday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
                file = open(setia, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Wednesday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "wednesday" and b == "2" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
                file = open(setia, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Wednesday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "wednesday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Wednesday\nRoom take : room3" "\n Price: 550 NIS\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "wednesday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Wednesday\nRoom take : room4" "\n Price: 660 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        #_______________________________________________________________________
        elif a == "thursday" and b == "1" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
                file = open(setia, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Thursday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "thursday" and b == "2" and c == "0":
            sleep(1)
            print("the best room for you is Room1")
            answer = input("Do you want take room1?")
            if answer == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
                file = open(setia, "w")
                file.write("Monday :Room2, Room3, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Thursday\nRoom take : room1" "\n Price: 350 NIS\n")
            elif answer == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "thursday" and b == "3" and c == "0":
            sleep(1)
            print("The best room for you its Room3")
            answer2 = input("Do you want to take Room3?")
            if answer2 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room4")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Thursday\nRoom take : room3" "\n Price: 550 NIS\n")
            elif answer2 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want back to menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a
        elif a == "thursday" and b == "2" and c == "2":
            sleep(1)
            print("The best room for you its Room4")
            answer3 = input("Do you want to take Room4?")
            if answer3 == "yes":
                setia = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
                file = open(setia, "w")
                file.write("Sunday :Room1, Room2, Room3")
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/" + User_name + ".txt"
                file5 = open(filename, "a")
                file5.write("Day take: Thursday\nRoom take : room4" "\n Price: 660 NIS\n")
            elif answer3 == "no":
                return a
            else:
                print("Enter only yes/no")
                z = input("Do you want to back menu?")
                if z == "yes":
                    return menu()
                elif z == "no":
                    return a

def cancel_reserv():
    files = os.listdir('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/')
    user_name = input("Enter your full name: ")
    file_to_search = user_name + ".txt"
    if file_to_search in files:
        print("The order is in the system!")
        A = input("Name of the hotel: ")
        if A == "herdos":
            take_day = input("Enter the day you take: ")
            take_room = input("Enter the room you take: ")
            if take_day == "sunday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "sunday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "sunday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "sunday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/sunday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
                #--------------------------------------------------
            elif take_day == "monday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "monday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "monday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "monday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/monday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
                #-----------------------------------------------------
            elif take_day == "tuesday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "tuesday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "tuesday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "tuesday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/tuesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
                #-------------------------------------------------------
            elif take_day == "wednesday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "wednesday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "wednesday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "wednesday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/wednesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
                #-----------------------------------------------
            elif take_day == "thursday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "thursday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "thursday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "thursday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/herdos/thursday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
        elif A == "setia":
            take_day = input("Enter the day you take: ")
            take_room = input("Enter the room you take: ")
            if take_day == "sunday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "sunday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "sunday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "sunday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/sunday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
                # --------------------------------------------------
            elif take_day == "monday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "monday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "monday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "monday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/monday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
                # -----------------------------------------------------
            elif take_day == "tuesday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "tuesday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "tuesday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "tuesday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/tuesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
                # -------------------------------------------------------
            elif take_day == "wednesday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "wednesday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "wednesday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "wednesday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/wednesday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
                # -----------------------------------------------
            elif take_day == "thursday" and take_room == "room1":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "thursday" and take_room == "room2":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "thursday" and take_room == "room3":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
            elif take_day == "thursday" and take_room == "room4":
                filename = "C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/setia/thursday.txt"
                file = open(filename, "a")
                file.write("Sunday :Room1, Room2, Room3, Room4")
                os.remove('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + '.txt')
                print("Order deleted from system!")
        else:
            print("Enter only (Herods/Setia)")
            return A


def search_invitation():
    files = os.listdir('C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/')
    user_name = input("Enter your full name: ")
    file_to_search = user_name + ".txt"
    if file_to_search in files:
        print("--------------------\nAll about your order:\n--------------------\n")
        filename = 'C:/Users/ויקטור/Desktop/Hotel_Project/Weekdays/rooms/User1/' + user_name + ".txt"
        file5 = open(filename, "r")
        print(file5.read())


def about_room():
    print("Information on all rooms!\n")
    sleep(1)
    dict_se = {"Two adults" : 350, "Two adults+ 1 kid" : 450 , "Three adults" : 550, "Two adults + Two kids" : 660}
    print("Setia Hotel:\nRoom1)Two adults - 350 Nis\nRoom2)Two adults + 1 kid - 450 Nis\nRoom3)Three adults - 550 Nis\nRoom4)Two adults + Two kids - 660 Nis")
    print("-------------------------------")
    print("Herods Hotel:\nRoom1)Two adults - 200 Nis.\nRoom2)Two adults + 1 kid - 250 Nis.\nRoom3)Three adults - 350 Nis.\nRoom4)Two adults + Two kids - 350 Nis.")
    sleep(1)
    print("\n-----------\nTransporting you automatoy to menu.....")
    print("By:Victor Bourman")
    sleep(10)
    return menu()


menu()