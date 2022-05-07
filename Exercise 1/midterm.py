from operator import mod
from statistics import mode
from pulp import *

model = LpProblem("Project", LpMaximize)

x1 = LpVariable('Dac trung 1', lowBound = 0)
x2 = LpVariable('Dac trung 2', 0)
x3 = LpVariable('Dac trung 3', 0)

model += 2*x1 + 2*x2 + 3*x3, "Loi Nhuan"
model += x1 + 2*x2 - x3 <= 14
model += 2*x1 - 2*x2 + 3*x3 <= 16
model += -x1 + 4*x2 + 2*x3 <= 16

model.solve()
model.objective
value(model.objective)

from fractions import Fraction
for v in model.variables():
  print(f"{v.name}={str(Fraction(v.varValue).limit_denominator())}")