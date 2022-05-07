from operator import mod
from statistics import mode
from pulp import *

model = LpProblem("Crazy diet", LpMinimize)

b = LpVariable('Brownies', lowBound = 0)
i = LpVariable('Ice cream', 0)
s = LpVariable('Soda', 0)
c = LpVariable('Cheesecake', 0)

model += 0.5*b + 0.2*i + 0.3*s + 0.8*c, "Total cost"
model += 400*b + 200*i + 150*s + 500*c >= 500, "Calories"
model += 3*b + 2*i >= 6, "Chocolate"
model += 2*b + 2*i + 4*s + 4*c >= 10, "Sugar"
model += 2*b + 4*i + s + 5*c >= 8, "Fat"

model.solve()
model.objective
value(model.objective)
from fractions import Fraction
for v in model.variables():
  print(f"{v.name}={str(Fraction(v.varValue).limit_denominator())}")