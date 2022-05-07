from operator import mod
from statistics import mode
from pulp import *

# model = LpProblem("Project", LpMinimize)

# x = LpVariable('Dac trung 1', upBound = 0)
# y = LpVariable('Dac trung 2')
# z = LpVariable('Dac trung 3', 0)


# model += 2*x - y + 4*z, "Loi Nhuan"
# model += x - y + 2*z == 5
# model += 2*x - y + z >=3

model = LpProblem('ABC',LpMaximize)

x1 = LpVariable('Dac Trung 1',0)
x2 = LpVariable('Dac Trung 2',0)

model += 29*x1 + 4*x2
model += 9*x1 - 4*x2 <= 23
model += 5*x1 - 7*x2 >= -22
model += x1 + x2 >= 5

model.solve()
model.objective
value(model.objective)

from fractions import Fraction
for v in model.variables():
  print(f"{v.name}={str(Fraction(v.varValue).limit_denominator())}")