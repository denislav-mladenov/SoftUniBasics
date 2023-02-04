import math

figura = input()
area = 0
pi = 3.141592653589793

if figura == 'square':
    a = float(input())
    area = a * a
elif figura == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif figura == 'circle':
    r = float(input())
    area = pi * (r ** 2)
elif figura == 'triangle':
    a = float(input())
    b = float(input())
    area = 1 / 2 * a * b
print(f'{area:3f}')