from math import *
def f(x):
  answer = 2**x - 2*cos(x)
  return answer
epselant = 1
a = 0.5
b = 1
while epselant > 0.001:
  c = (a+b)/2
  if f(a) * f(c) < 0:
    b = c
  else:
    a = c
  epselant = (b - a)/2
globalAnswer = (a + b)/2
print(globalAnswer)
