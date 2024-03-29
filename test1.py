

# Python program to check whether the string is Symmetrical or Palindrome.

def is_palindrome(a):
    a = a.replace(" ", "").lower()
    return a == a[::-1]
b= input("Enter a string: ")
if is_palindrome(b):
    print("The string is a palindrome.")
else:
    print("The string is Symmetric")

"""Create a program that checks if a given number is even or odd."""

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num," is an even number")
else:
    print(num, "is an odd number")

#Write a Python program to print S Shape Character Program

n=5
for i in range(n):
  for j in range(n):
    if (i == 0 or i == n - 1 or i == n // 2) or (j == 0 and i <= n // 2) or (j == n - 1 and i >= n // 2):
      print('*', end='')
    else:
        print(' ', end='')
  print()

#"""Create a Python program that validates and extracts URLs from a web page's source code using regular expressions."""

import re
def isValidURL(str):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False
print("enter the url")
url=input()
if(isValidURL(url) == True):
    print("Yes")
else:
    print("No")

#"""Write a Python program to multiply two matrices and display the resulting matrix."""

r1 = int(input("Enter the no of rows for first matrix: "))
c1 = int(input("Enter the no of columns for first matrix: "))
r2 = int(input("Enter the no of rows for second matrix: "))
c2 = int(input("Enter the no of columns for  second matrix: "))
if c1 != r2:
    print("Matrix multiplication is not possible.")
else:
    m1 = []
    print("Enter elements of the first matrix:")
    for i in range(r1):
        row = []
        for j in range(c1):
            element = float(input("Enter element at row " + str(i + 1) + ", column " + str(j + 1) + ": "))
            row.append(element)
        m1.append(row)
    m2 = []
    print("Enter elements of the second matrix:")
    for i in range(r2):
        row = []
        for j in range(c2):
            element = float(input("Enter element at row " + str(i + 1) + ", column " + str(j + 1) + ": "))
            row.append(element)
        m2.append(row)
    rm = [[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                rm[i][j] += m1[i][k] * m2[k][j]
    print("Resulting Matrix:")
    for row in rm:
        print(row)

#"""Create a program to find the transpose of a given matrix."""

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("Enter the elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = float(input("Enter element at row " + str(i + 1) + ", column " + str(j + 1) + ": "))
        row.append(element)
    matrix.append(row)
transpose = [[0 for _ in range(rows)] for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

print("Transpose of the Matrix:")
for row in transpose:
    print(row)

#"""Python Program to Sort a List According to the Length of the Elements"""

elements = input("Enter a list of elements : ").split()
def custom_sort(element):
    return len(element)
sorted_elements = sorted(elements, key=custom_sort)
print("Sorted List by Length of Elements:")
for element in sorted_elements:
    print(element, end=' ')

#"""Write a Python program to find the sum of all elements in an integer array."""

a = input("Enter the array elements: ").split()
a = [int(x) for x in a]
aa = sum(a)
print("Sum of the elements in the array:", aa)

#"""Create a program that takes an array of numbers as input and outputs the array in reverse order.


n = input("Enter the array of number: ").split()
n = [int(x) for x in n]
n.reverse()
print("Array in Reverse Order:", n)

#"""Write a program to convert temperature between Fahrenheit and Celsius."""

print("Choose conversion type:")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter your choice (1/2): "))
if choice == 1:
    celsius = (float(input("Enter temperature in Fahrenheit: ")) - 32) * 5/9
    print("temperature in Celsius is:", celsius, "*c")
elif choice == 2:
    fahrenheit = (float(input("Enter temperature in Celsius: ")) * 9/5) + 32
    print("temperature in Fahrenheit is:", fahrenheit, "*F")
else:
    print("Invalid choice")
