#######################
from time import sleep
#######################
#######################
def menu():
    while(True):
        choice=input("Menu:\n1.Search URL\n2.Add URL + IP Address\n3.Delete URL\n4.Update IP of specific URL\n5.Print All URL IP\n")
        if(choice=="1"):
            search()
            #find
        elif (choice=="2"):
            add_url()
            #add_URL
        elif (choice=="3"):
            delete()
            #del_URL
        elif (choice=="4"):
            update1()
            #change
        elif (choice=="5"):
            printer()
            #print_ALL
        else:
            print("Enter 1-5 ONLY Please!")
            continue
        if (input("Do you want to Quit?\n yes/no\n")=="yes"):
            break
    sleep(1)
    print("Thanks and good bye!")

#1
def search():
    url1=input("Enter URL Please:\n")
    if (url1 in dict):
        print("This url exists!")
    else:
        print("This url isn't exists!")
#2
def add_url():
    print("Add an address!")
    sleep(1)
    dict.update({input("Add new URL:\n"): input("Add new IP Address:\n")})
    print("Checking the option...")
    sleep(2)
    print("Insert added successfully!")
    print("Printing the dict!")
    sleep(1)
    print(dict)
#3
def delete():
    del_url=input("Enter the URL you want to delete:\n")
    dict.pop(del_url)
    print(dict)
#4
def update1():
    update_ip=input("Enter You New IP Address:\n")
    sleep(1)
    update_url=input("Enter You New URl:\n")
    print(dict)
#5
def printer():
    print("Scans the information...\n")
    print("Please wait 3 seconds!")
    sleep(3)
    print(dict)
#dict#
dict={}
for i in range(6):
    print("Welcome!")
    dict.update({input("Add URL:\n"): input("Add IP Address:\n")})
    print(dict)

menu()
