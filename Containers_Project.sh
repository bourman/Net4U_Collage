#!/bin/bash
#Project_containers
EXIT="no"
while [ $EXIT == "no" ]
do
	echo -e "\n----------\nMenu:\n----------\n1)Install Docker system\n2)Create new Container\n3)Download/Update/Delete images\n4)Check with curl\n--------------------\nEnter your chocie: "
	read choice
	if [ $choice == "1" ]
	then
		echo "Install docker system"
		sudo apt install curl
		crul https://get.docker.com
		docker version
		echo "Done"
	elif [ $choice == "2" ]
	then
		echo -e  "How many containers create: "
		read i
		for i in {1..$i}
		do
			echo -e "Which type of container do you want: "
			read machine
			if [ $machine == "dockerui" ]
			then
				sudo docker pull abhlav/dockerui:latest
				sudo docker run -d -p $root:9000 -v /var/run/docker.sock:/docker.soch --name dockerui abh1nav/dockerui:latest -e="/docker.sock"
				echo "Done"
			else
				sudo docker run -d -p $root:8080 $machine
				echo "Done"
			fi
		done
		sudo docker ps
	elif [ $choice == "3" ]
	then
        echo -e "Do you want to download/update/delete?\n"
        read A
        if [ $A == "download" ]
        then
            echo -e "Which kind of image do you want to download? (dockerui/jenkins/centos/nginx)\n"
            read image
            echo "This is the available images:"
            sudo docker search $image
            echo -e "which image's id do you want to download?\n"
            read download
            sudo docker pull $download
            echo "Done!\n"
        elif [ $A == "update" ]
        then
            echo -e "There are the downloaded images:\n"
            sudo docker images
            echo -e "Which images id do you want to update?\n"
            read update
            sudo docker rmi $update
            sudo docker pull $update
            echo "Done!"
        elif [ $A == "delete" ]
        then
            echo -e "There are the downloaded images:\n"
            sudo docker images
            echo -e "Which image's id do you want to delete?\n"
            read delete
			sudo docker rmi $delete
			echo "Done"
		fi
	elif [ $choice == "4" ]
	then
		echo -e "Enter the Ip Address of the conatiner you want to check:"
		read ip_add
		curl -v telnet://$ip_add
	else
		echo "Enter 1-4 please !!"
		continue
	fi
	echo -e "Do you want to quit?  yes/no"
	read EXIT
echo "Good bye...!"
done
