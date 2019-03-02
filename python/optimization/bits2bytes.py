#!/usr/bin/python3
while True:
    try:
        amount = int(input("\nPlease enter the number of bits: "))
        if amount < 1:
            print("error: input is to low\n")
            continue
        else: break
    except:
        print("error: bad input\n")
        continue
names= ["Bits","Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes", "Exabytes","Zettabyte"]
loop = 0
while True:
    if loop == 0:
        remainder = amount % 8
        carryForward = (amount-remainder)/8
    else:
        remainder = amount % 1000
        carryForward = (amount-remainder)/1000
    
    if loop > 8:
        print("error: input is to high\n")
        exit()
    
    if remainder != 0.0: print(names[loop] + ": " + str(round(remainder)))
    loop += 1
    if carryForward > 0: amount = carryForward
    else: break
