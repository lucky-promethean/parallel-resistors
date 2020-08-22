#! /usr/bin/python
def para(r1, r2):
        return(r1*r2/r1+r2)

print("enter parallel resistances")
r1=float(input("R1: "))
r2=float(input("R2: "))
print ("Req= ",r1*r2/(r1+r2))
req=float(r1*r2/(r1+r2))
print ("Req= ", req)
print(" ")
inp=1
while (inp == 1):
        r1 = req
        print ("R1=previous Req= ",r1)
        r2=float(input("R2: "))
        req=float(r1*r2/(r1+r2))
        print ("Req= ", req)
        inp=int(input("press 1 for another comparison, Req taken as R1 or 0 for a clear...  \n"))
if (inp == 0):
        quit()
