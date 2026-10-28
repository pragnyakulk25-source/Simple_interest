
import sys

def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

if len(sys.argv) == 4:
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])
else:
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time in years: "))

si = simple_interest(p, r, t)

print("Simple Interest =", si)
