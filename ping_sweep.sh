#!/bin/bash

echo "ENTER the Subnet:"
read Subnet

if [ "$Subnet" == "" ]
then
	echo "ENTER the Subnet:"
	echo "Syntax Example = ./pingsweep,sh < 10.1.161"
else

for IP in $(seq 1 254); do

	ping -c 1 $Subnet.$IP | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
