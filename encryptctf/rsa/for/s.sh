#!/bin/bash

dtrx -n -f  flag
ls | grep -v "flag" | grep -v "$" |  grep -v "s.sh" | while read line;
do 
	mv $line $line
	dtrx -n -f $line

done
