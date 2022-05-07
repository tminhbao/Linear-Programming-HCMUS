from operator import mod
from statistics import mode
from pulp import *

model = LpProblem("Crazy diet", LpMinimize)

x1 = LpProblem("x1",0)
x2 = LpProblem("x2",0)

m = input("Nhap so rang buoc: ")
c1 = input("Nhap c1: ")
c2 = input("Nhap c2: ")

model += c1*x1 + c2*x2, "Total cost"
model += 400*b + 200*i + 150*s + 500*c <= 500, "Calories"
model += 3*b + 2*i >= 6, "Chocolate"
model += 2*b + 2*i + 4*s + 4*c >= 10, "Sugar"
model += 2*b + 4*i + s + 5*c >= 8, "Fat"

# model.solve()
# model.objective
# value(model.objective)
# from fractions import Fraction
# for v in model.variables():
#   print(f"{v.name}={str(Fraction(v.varValue).limit_denominator())}")
