#!/bin/bash

echo -e "Menu:\n1.pull image\n2.run X ubuntu\n3.remove image\n4.Run web app specific port\n5.docker ui\n"
read choice
if [ $choice == "1" ]
then
	echo -e "Choose image to install: php/ubuntu/centos\n"
	read OS
	while true
	do
	if [ $OS == "centeos" ] ||[ $OS == "php" ]|| [ $OS == "ubuntu" ]
	then
		sudo docker pull $OS
		break
	else
		echo -e "Enter good OS\n"
	fi
	done
elif [ $choice == "2" ]
then
	echo -e "Enter how many ubuntu's containers you want?"
	read num
	for i in {1..$num}
	do
		sudo docker run -d ubuntu /bin/bash -c 'while true ; do echo net4u ; sleep 1 ; done' 2>/dev/null
	done

	sudo docker ps


elif [ $choice == "3" ]
then
	echo -e "Choose image to delete php/ubuntu\n"
	read OS
	while true
	do
	if [ $OS == "centos" ] || [ $OS == "ubuntu" ] || [ $OS == "php"]
	then
		su docker rmi $OS
		break
	else
		echo -e "Enter good OS\n"
	fi
	done



elif [ $choice == "4" ] 
then
	echo -e "Enter a port: \n"
	read port
	sudo docker run -d -p  $port:8080 adejonge/helloworld
	sudo docker ps | awk 'NR==1'
fi

elif [ $choice == "5" ]
then
	
