#!/usr/bin/python3
import time, os, subprocess

# files setup
text = ""
os.chdir("flag_scripts")
p = subprocess.Popen("ls", stdout=subprocess.PIPE)
for each in p.stdout.read():
	text += chr(each)

flag_list = text.split("\n")
del flag_list[-1]

# menu
while True:
	inp = input("enter country name: ")

	if inp == "exit".lower():
		exit()

	elif inp + ".py" in flag_list:
		print("found file " + inp + "\n")
		os.system("./" + inp + ".py")		
	else:
		print("Error: file not found")
		print("currently available files are:")
		for x in range(1, len(flag_list)): print(flag_list[x])

pass