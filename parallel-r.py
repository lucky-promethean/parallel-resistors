#! /usr/bin/python
def para(r1, r2):
        return(r1*r2/r1+r2)

print("enter parallel resistances")
r1=float(input("r1: "))
r2=float(input("r2: "))
print ("Req= ",r1*r2/(r1+r2))
