# 1. search for IP address from a list
# 2. add IP address to a list
# 3. Delete IP address to a list
# 4. Print all the IPs to the screen.
#Start:

from time import sleep

def IP_LIST():
    list_ip=[]
    for i in range(6):
        list_ip.append(input("Enter a IP: "))
    return list_ip



def menu():
    while(True):
        choice=input("Menu:\n1.Find IP from the list\n2.Add Ip Address to the list\n3.Delete Ip from the list\n4.Print all IP!\n")
        if(choice=="1"):
            a = input("Enter the ip you want to find:")
            search(a)
        elif(choice=="2"):
            b = input("Enter the ip you want to add:")
            c=search(b)
            if(c=="yes"):
                print("This IP isn't available")
            else:
                append(b)
        elif(choice=="3"):
            delete()

        elif(choice=="4"):
            printer()
        else:
            print("Enter 1-4 only!!!\n")
            continue
        if(input("\nDo you want to quit? y/n\n")=="y"):
            break
    print("\nThanks and bye bye...")



def search(a):
    sleep(1)
    if a in my_list:
        print("It is here!!")
        return "yes"
    else:
        print("It's not here!")
        return "no"


def append(a):
    my_list.append(a)
    sleep(1)
    print("Your IP address has been added to the list!")

def delete():
    del_ip=input("Delete ip Address:")
    my_list.remove(del_ip)
    print(my_list)
def printer():
    print("Printing all IP.....")
    print(my_list)



my_list=IP_LIST()
print("My new list is: " + str(my_list))
menu()
