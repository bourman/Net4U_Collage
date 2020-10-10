#!/bin/bash
#test
echo -e "how many Containers create:"
read con
for con in con:
do
	echo -e "which root you want:"
	read rootz
	echo -e "Which type you want:"
	read machine
	if [ $machine == "dockerui" ]
	then
		sudo docker pull abh1nav/dockerui:lastest
		sudo docker run -d -p $root:9000 -v /var/run/docker.sock:/docker.sock --name dockerui abh1nav/dockerui:latest -e="/docker.sh"
		echo "done!"
	else
		sudo docker run -d -p $root:8080 $machine
		echo "Done"
	fi
done
sudo docker ps
