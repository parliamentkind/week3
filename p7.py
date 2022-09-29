#1
"""
1. Write a program to calculate the area of various geometric shapes.
2. Given 3 different arrays of integers (the size of each does not exceed 15). In each
array, find the sum of the elements and the arithmetic mean.
"""
#1
"""
import math

a = str(input("Enter the shape you want to calc. A of: "))
if a == "circle":
    r = int(input("enter the value of radius: "))
    area = 2*math.pi*r
elif a == "square":
    s = int(input("enter the value of side: "))
    area = s*s
elif a == "triangle":
        b = int(input("enter the value of base: "))
        h = int(input("enter the value of height: "))
        area = (1/2) * b * h
else:
    print ("Enter the valid shape")
print ("A of shape: " + str(area))

#2
import math
def mean(array):
    mean = 0
    sum = 0
    for i in range(len(array)):
        mean += (array[i] / len(array))
        sum += array[i]
    print(sum, ' , ', round(mean, 3))

a = [11,13,15,16,12,17,18]
b = [0,5,66,76,13,25]
c = [53,34,45,56,67,78,89,90]
mean(a)
mean(b)
mean(c)
"""
#2
"""
1. Calculate the area of a regular hexagon with side a using the triangle area
subroutine.
2. The user enters two sides of three rectangles. Bring out their area.
"""
#1
"""
import math

n = int(input("Enter the side: "))
atri = (math.sqrt(3) / 4) * math.pow(5, 2)
ahex = 6 * atri
print(ahex)

#2
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
area = a*b
for i in range(3):
    print(area)
"""
#3
"""
1. The legs of two right triangles are given. Write a function to calculate the length of
the hypotenuse of these triangles. Compare and deduce which of the hypotenuses is greater and
which is smaller.
2. Convert a string so that the letters of each word in it are sorted
alphabetically.
"""
#1
#---
#2
"""
a = str(input('Enter the string: '))
print (''.join(sorted(a)))
"""
#4
"""
1. Two fractions A/B and C/D are given (A, B, C, D are natural numbers). Write a
program for dividing a fraction by a fraction. The answer must be an irreducible fraction. Use a
subroutine of the Euclid algorithm to determine the gcd.
2. Given a circle (xa)2 + (yb)2 = R2 and points Р(р1, р2), F(f1, f1), L(l1,l2).
Find out and display on the screen how many points lie inside the circle. Checking whether
a point lies inside a circle should be done in the form of a procedure.
"""
#1
#--
"""
#2
p1 = 12
p2 = 15
x = 1
y = 2
r = 3
def isitinside(x, y, r, p1, p2):
    if ((p1 - x) * (p1 - x) + (p2 - y) * (p2 - y) <= (r * r)):
        return True
    else:
        return False
if isitinside(x, y, r, p1, p2):
    print("Inside")
else:
    print("Outside")
"""
#5
"""
1. Two fractions A/B and C/D are given (A, B, C, D are natural numbers). Write
a program to subtract the second fraction from the first fraction. The answer must be an
irreducible fraction. Use a subroutine of the Euclid algorithm to determine the gcd.
2. Write a program that prints all the divisors of the given number in one
line, separating them with spaces.
"""
#1
#--
"""
#2

a = int(input('Enter the number: '))

def print1(a):
    for i in a:
        print(i, end = ' , ')

def division(a):
    b = []
    for i in range(1, (a+1)):
        if a%i == 0:
            b.append(i)
    print1(b)

division(a)
"""
#6
"""
1. Write a program to find the greatest common divisor (GCD) and the least
common multiple (LCM) of two natural numbers LCM(A, B) = (A*B)/GCD(A,B). Use a
subroutine of the Euclid algorithm to determine the gcd.
2. Write a program to calculate the area of a convex quadrilateral given the
lengths of four sides and a diagonal.
"""
#1
#3--
#2
"""
import math

x = list(map(float, input("enter 4 sides: ").split()))
d = float(input("enter the diagonal: "))

def AreaQuad(l, d):
    h1 = 2 * (areaTriangle(l[0], l[1], d) / d)
    h2 = 2 * (areaTriangle(l[2], l[3], d) / d)
    area1 = (1/2) * d * (h1 + h2)
    return area1


def areaTriangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

print("area of quadrilateral: ", AreaQuad(x, d))
"""
#7
"""
1. Numbers X, Y, Z, T are given — the lengths of the sides of the quadrilateral.
Calculate it area if the angle between sides of length X and Y is a right angle. Use two routines to
calculate areas: a right triangle and a rectangle.
2. Write a program that converts a non-negative integer given to it into a 10-digit
octal code, preserving leading zeros.
"""
#1
"""
import math

x = list(map(int, input("enter 4 sides: ").split()))
def AreaQuad(l):
    s = (l[0] + l[1] + l[2] + l[3]) / 2
    area = math.sqrt(((s - l[0]) * (s - l[1]) * (s - l[2]) * (s - l[3])) - (l[0] * l[1] * l[2] * l[3] * math.pow(math.cos(math.pi / 2), 2)))
    return area
print("Area of Quadrilateral: ", AreaQuad(x))
#2
a = int(input('Enter the number: '))
if a > 0:
    print(oct(a))
else:
    print("There is no way")
"""
#8
"""
1. Find all natural numbers not exceeding the given n that are divisible by
each of their digits.
2. Enter a one-dimensional array A of length m. Swap the first and last elements in
it. Enter the length of the array and its elements from the keyboard. In a program, describe a
procedure for replacing elements of an array. Output the original and resulting arrays.
"""
#1
"""
n = int(input("Enter the numb: "))

def div(n):
    for i in range(n):
        if divide(i) == True:
            print(i)


def divide(n):
    t = n
    while (t > 0):

        d = t % 10
        if ((d!= 0 and n % d == 0) == False):
            return False
            
            t = t // 10
            
            return True

div(n)

#2--
"""
#9
"""
1. Subtract the sum of its digits from a given number. The sum of its digits was
again subtracted from the result, and so on. How many such actions will result in zero?
2. You are given 3 different arrays of integers. In each array, find the
product of the elements and the arithmetic mean.
"""
#1--

#2--

#10
"""
1. On the interval [100, N] (210 < N < 231) find the number of numbers composed
of the digits a, b, c.
2. Write a program that reverses the sequence of words in a string.
"""
#1
"""
inter = []
for i in range(210, 231):
    inter.append(i)

r = [sub for sub in inter if len(set(str(sub))) == len(str(sub))]

print(str(r))
#2
string = input("Enter the string: ")
a = string.split()[::-1]
b = []
for i in a:
    b.append(i)
print(" ".join(b))
"""
#11
"""
1. Two prime numbers are called "twins" if they differ from each other by 2 (for
example, 41 and 43). Print all pairs of "twins" from the segment [n, 2n], where n is a given
natural number greater than 2..
2. Given two matrices A and B. Write a program that swaps the maximum
elements of these matrices. Finding the maximum element of the matrix to formalize in the
form of a procedure.
"""
#1

#2

#12
"""
1. Two natural numbers are called "friendly" if each of them
equals the sum of all divisors (except itself) of another (for example, the numbers 220
and 284). Find all pairs of "friendly" numbers that are not greater than the given number N.
2. Given the lengths of the sides of the triangle a, b, c. Find the medians of
a triangle whose sides are the medians of the original triangle. To calculate the
median drawn to side a, use the formula Calculate the median in the form of a
procedure.
"""
#1

#2

#13
"""
1. A natural number with n digits is called an Armstrong number if the sum
of its digits raised to the power of n is equal to the number itself. Find all Armstrong
numbers from 1 to k.
2. Three points are given by their coordinates X(x1, x2), Y(y1, y2) and Z(z1, z2).
Find and print the coordinates of the point for which the angle between the abscissa axis and
the ray connecting the origin with the point is minimal. Calculations to form in the form of a
procedure.
"""
#1

#2

#14
"""
1. Write a program to find numbers from the interval [M, N] that have the
largest number of divisors.
2. Four points are given by their coordinates X(x1, x2), Y(y1, y2), Z(z1, z2),
P(p1, p2). Find out which of them are at the maximum distance from each other and display
the value of this distance on the screen. Calculate the distance between two points in the
form of a procedure.
"""
#1

#2

#15
"""
1. Find all prime natural numbers not exceeding n whose binary notation is a
palindrome, i.e. reads the same from left to right and from right to left.
2. Four points are given by their coordinates X(x1, x2, x3), Y(y1, y2, y3), Z(z1,
z2, z3), T(t1,t2, t3). Find out which of them are at the minimum distance from each other and
display the value of this distance on the screen. Calculate the distance between two points in
the form of a procedure
"""
#1

#2
