#!/usr/bin/python3
import hashlib

def sha256(inp):
	return hashlib.sha256(inp.encode('utf-8')).hexdigest()

doc = open("pass.txt", "r")
hashes = doc.read().split("\n")
del hashes[-1]
print(hashes)

for x in range(1,3):
	inp = input("enter password: ")

	if inp == "new password":
		doc = open("pass.txt", "a")
		doc.write(sha256(input("enter new password: ")) + "\n")
		exit()

	elif sha256(inp) in hashes:
		print("authenticated")
		exit()

	else:
		print("incorrect password\nattempt {} of 3\n".format(x))
print("out of attempts")