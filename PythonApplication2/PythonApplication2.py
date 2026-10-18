from math import *

def funct(x):
    if -9 <= x <= -6:
        y = -sqrt(9-(x+6)**2)
    elif -6 < x < -3:
        y = x+3
    elif -3 <= x <= 0:
        y = sqrt(9-x**2)
    elif 0 < x <= 3:
        y = 3 - x
    else: 
        y = (x-3)/2
    print("x={0:.3f}  y={0:.3f}".format(x, y))

def main():
    x = float(input("Введите x в промежутке от -9 до +9: "))
    if -9 <= x <= 9:
       funct(x) 
    else:
        print("x не находится в промежутке от -9 до +9")

if __name__ == "__main__":
    main()