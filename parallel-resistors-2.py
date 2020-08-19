#! /usr/bin/python
def para(r1, r2):
        return(r1*r2/r1+r2)

print("enter parallel resistances")
r1=float(input("r1: "))
r2=float(input("r2: "))
print ("Req= ",r1*r2/(r1+r2))
req=float(r1*r2/(r1+r2))
print ("req= ", req)
inp=int(input("press 1 for another comparison, req taken as r1 or 0 for a clear...  \n"))
print(" ")
if (inp == 1):
        r1 = req
        print ("r1=previous req= ",r1)
        r2=float(input("r2: "))
        req=float(r1*r2/(r1+r2))
        print ("req= ", req)
if (inp == 0):
        print("to clear exit")
