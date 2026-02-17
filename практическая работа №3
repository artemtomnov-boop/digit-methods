from math import *
def f(x):
    answer = x + sin(x) - 0.2*x
    return answer
x_n1 = 0
x_n2 = 2.6
count = 1
epselant = 10**(-3)
print(f'0 --- {x_n2}')
while abs(x_n2 - x_n1) > epselant:
    x_n1 = x_n2
    x_n2 = round(f(x_n1), 3)
    print(f'{count} --- {x_n2}')
    count += 1
print(f'ANSWER {x_n2}')
