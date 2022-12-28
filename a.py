
# --------------------Q.1a-----------------------------------------
# n=int(input("Enter n value:"))
# for i in range(1,n+1):
#     print(i,end=" ")

# -------------------Q.1b-----------------------------------------
# num = int(input("Enter a number: "))
# if num > 1: 
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#        print(num,"is a prime number")
# else:
#    print(num,"is not a prime number")

# -------------------Q.1c-----------------------------------------
# n=int(input( " Enter the number :" ))
# factorial = 1
# if n < 0:
#       print ("Factorial cannot be calculated, non-integer input")
# elif n == 0:
#      print ("Factorial of the number is 1")
# else:
#     for i in range (1, n+1):
#         factorial = factorial *i      
#     print ("Factorial of the given number is: ", factorial)

# -------------------Q.1d-----------------------------------------
# print("Enter a Number: ")
# num = int(input())
# sum = 0
# while num!=0:
#     rem = num%10
#     sqr = rem*rem
#     sum = sum+sqr
#     num = int(num/10)
# print("\nsquares of Sum of digits of given number is: ")
# print(sum)

# -------------------Q.1e-----------------------------------------

# nums = []
# totEven = 0
# totOdd = 0
# print(end="Enter the Size: ")
# size = int(input())
# print(end="Enter " +str(size)+ " Numbers: ")
# for i in range(size):
#   nums.insert(i, int(input()))
# for i in range(size):
#   if nums[i]%2==0:
#     totEven = totEven+1
#   else:
#     totOdd = totOdd+1
# print("\nEven Number: " +str(totEven))
# print("Odd Number: " +str(totOdd))

# -------------------Q.2-----------------------------------------
# import random
# import time
# while True:
#     for x in range(1):
#         print(random.randint(1,6))
#     time.sleep(5)


 # -------------------Q.3-----------------------------------------   

# x={'usn':'4mk21cs401','fname':'sujan','lname':'devadiga','contact':'9482569993'}  
# print("details of "+x['fname'].upper(),x['lname'].upper()+" is :")
# print("usn : "+x["usn"])
# print("first name : "+x["fname"])
# print("Last name : "+x["lname"])
# print("contact number : "+x["contact"])



# -------------------Q.5-----------------------------------------

# import re
# def isValidURL(str):
#     regex = ("((http|https)://)(www.)?" +
#              "[a-zA-Z0-9@:%._\\+~#?&//=]" +
#              "{2,256}\\.[a-z]" +
#              "{2,6}\\b([-a-zA-Z0-9@:%" +
#              "._\\+~#?&//=]*)")
#     p = re.compile(regex)
#     if (str == None):
#         return False
#     if(re.search(p, str)):
#         return True
#     else:
#         return False
# print("enter the url")
# url=input()
# if(isValidURL(url) == True):
#     print("Yes")
# else:
#     print("No")



# -------------------Q.8-----------------------------------------
# import datetime
# inputDate = input("Enter the date in format 'dd/mm/yy' : ")
# day, month, year = inputDate.split('/') 
# isValidDate = True
# try:
#     datetime.datetime(int(year), int(month), int(day))
# except ValueError:
#     isValidDate = False
# if year<str(1990) or year>str(2050):
#     print("Input date is not valid..")
# elif(isValidDate):
#     print("Input date is valid ..")
# else:
#     print("Input date is not valid..")


# -------------------Q.9-----------------------------------------

# lower, upper, digit = 0, 0, 0
# password = input("Enter your password")
# if (len(password) >= 8):
#     for i in password:

#         for word in password.split():
#             if(word[0].isupper()):
#                 upper += 1

#         if(i.islower()):
#             lower += 1

#         if(i.isdigit()):
#             digit += 1
# else:
#     print("Password should be more than 6 characters")
# if (lower >= 1 and upper >= 1 and digit >= 1):
#     print("Valid Password")
# else:
#     print("Invalid Password")

# -------------------Q.6-----------------------------------------
# import re

# pattern = r"[0-9][a-z A-Z][a-z A-Z][0-9][0-9][a-z A-Z][a-z A-Z][0-9][0-9][0-9]"

# usn =input("enter your usn :")

# if re.search(pattern, usn):
#     print("Valid USN")
# else:
#     print("Invalid USN")

# -------------------Q.7-----------------------------------------
# import re 
# usn=input("enter the usn : ")
# name=input("enter the name : ")
# phno=input("enter the phone no : ")
# email=input("enter the email id : ")
# if len(str(phno)) > 10 or len(str(phno)) < 10:
#     print("Phone Number is not valid")
# else:
#     print("Phone number is valid")
# def solve(email):
#    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
#    if re.match(pat,email):
#       return True
#    return False
# if(solve(email)==True):
#     print("email id is valid")
# else:
#     print("email id is Invalid")

# -------------------Q.4-----------------------------------------

# fruits={1:"apple",2:"orange",3:"mango",4:"kiwi",5:"banana"}
# for i in fruits:
#     print(fruits[i])
