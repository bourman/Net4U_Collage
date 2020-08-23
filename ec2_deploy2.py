#!/bin/python3
###############

def deploy_instances():
    import boto3
    ec2 = boto3.resource('ec2')

# create a new EC2 instance
    instances = ec2.create_instances(
        ImageId=input("Enter ami ID:\n"),
        MinCount=1,
        MaxCount=int(input("How many instances?\n")),
        InstanceType=input("Which type of instance?\n"),
        KeyName=input("Which keypair?\n")
 )

def describe_instance():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            print("ID: "+ i['Instances'] + "\nIP Address:" + i['PublicIpAddress'] + "\n------------------\n") 
def destory_instance():
    instances = input("Enter the ids of the instances that you want to STOP: ")
    ids = [instances]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(Instancelds = ids).terminate() 

def stop_instance():
    instances = input("Enter the ids of the instances that you want to stop:")
    ids = [instances]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(Instancelds = ids).stop()


def start_instance():
    instances = input("Enter the ids of the instances you want  to stop:")
    ids = [instances]
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(Instancelds = ids).start()
def menu():
    while(True):
        choice=input("Menu:\n1.Describe EC2 \n2.Deploy Instances\n4.Stop Instance \n5.Start Instance \n")
        if(choice=="1"):
            describe_instance()
        elif(choice=="2"):
            deploy_instances()
        elif(choice=="3"):
            destroy_instance()
        elif(choice=="4"):
            stop_instance()
        elif(choice=="5"):
            start_instance()
        else:
            print("Enter 1-5 ONLY!!! \n")
            continue

	exit=input("Do you want to exit?!    yes\no\n")
        if(exit=="yes"):
            print("Good BYE...\n")
            break
#finish!

menu()
