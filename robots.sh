#!/bin/bash

cd /home/student/Desktop/scripts

echo "enter a domain"
read domain

wget -0 $domain\ robots.txt $domain/robots.txt

cat | robots.txt | grep 'Disallow' | cut -d ' ' -f2 > $domain\ robocut.txt

firefox 6
sleep 5

for i in $(cat $domain\ robocut.txt); do
	firefox -new-tab https://www.$domain$i &
	sleep 2
done
