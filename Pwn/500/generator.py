#!/usr/bin/python
from os import popen
from os import mkdir
from sys import argv
from random import random as rand
N = int(argv[1])

for t in range(N):
	sec=""
	L = 32
	for i in range(L):
		sec += chr(ord('a')+int(rand()*26))
	sec = popen("echo -n %s | md5sum"%sec).read().split(' ')[0]
	rep = "cat pwn500.c | sed 's/1337/%d/'"%(6000+t)
	source= popen(rep).read()
	
	mkdir('team%d'%t)
	f = file('team%d/pwn500.c'%t, 'w+')
	f.write(source)
	f = file('team%d/flag'%t, 'w+')
	f.write(sec)
	
	popen("echo 'INSERT INTO `flags` (`teamID`, `taskID`, `flag`) VALUES (%d, 20, '\"'\"%s\"'\"');\' >> pwn500.sql"%((t+1), sec))
