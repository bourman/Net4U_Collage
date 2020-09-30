#!/bin/python3
##############
from time import sleep
import os

def menu():
	while(True):
		choice = input("--------------------\nMenu:\n1.Change enp0s8\n2.Add a route (Permanent)\n3.Change hostname\n4.Change etc/hosts\n5.Change root password\n6.Enable ssh to root\n--------------------\nEnter your Choice: ")
		if (choice == "1"):
			emp_add()
		elif (choice == "2"):
			add_route()
		elif (choice == "3"):
			hostim_add()
		elif (choice == "4"):
			etc_change()
		elif (choice == "5"):
			pass_root()
		elif (choice == "6"):
			ssh_to_root()
		else:
			print("\nEnter only 1-6!!!!!\n")
			continue
		if (input("Do you want to quit? \t yes/no\n") == "yes"):
			break
	print("Thanks, good bye!")

###### 1
def emp_add():
	os.system('sudo ifconfig eth0 down')
	ip_set = input("Enter you new Ip address to enp0s8: ")
	sleep(1)
	print("Address picked up on system!\n")
	os.system('sudo ifconfig eth0 + ip_set')
	os.system('sudo ifconfig eth0 up')
###### 2
def add_route():
	ip_route = input("Enter your Ip Route: ")
	mask = input("Enter your Mask: ")
	gateway = input("Enter your Gateway: ")
	os.system('route ADD + ip route + MASK + mask + gateway ')
###### 3
def hostim_add():
	os.system('apt-get install systemd')
	host_new = input("Enter your new Hostname: ")
	os.system('sudo hostnamectl set-hostname + host_new')
	os.system('hostnamectl')
	print("Your new Hostname is :\n")
	os.system('hostname')
###### 4
def etc_change():
	host = input("Enter new host: ")
	sleep(1)
	re_ip = input("Enter new Ip address: ")
	print("Done!\n")
	SetHostAT(re_ip)
###### 5
def pass_root():
	while(True):
		pass_r = input("Are you sure you want to Change Root Password?\nYes/no\nEnter you choice:")
		if (pass_r == "yes"):
			os.system('sudo passwd root')
		elif (pass_r == "no"):
			print("Ok, you transferred to Menu...")
			sleep(2)
			return menu()
		else:
			sleep(1)
			print("Enter Only Yes/No thanks...!")
			continue
		if (input("Do you want back to menu?  Yes/No\n") == "yes"):
			break
	print("Ok, you transferred to Menu...")
	sleep(1)
###### 6
def ssh_to_root():
	while(True):
		ssh_r = input("Do you sure you want to enable SSH to Root?")
		if (ssh_r == "yes"):
			os.system('sudo sed -i "s/#PermitRootLogin prohibit-password/PermitRootLogin yes/" /etc/ssh/sshd_config')
			print("Successful!")
		elif (ssh_r == "no"):
			print("Ok, you transferred to Menu...")
			sleep(2)
			return menu()
		else:
			sleep(1)
			print("Enter only Yes/No thanks...!")
			continue
		if (input("Do you want back to menu?  Yes/No\n") == "yes"):
			break
	print("Ok, you transferred to Menu...")




menu()
#Victor Bourman
