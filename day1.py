""" say "Hello, World!" with pyhton """
print("Hello, World!")

""" leap year or not in python using function and return boolean value"""
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
Year = int(input("Enter your year: "))
result = leap_year(Year)
print(result)

""" find first repeating alphanumeric in string"""
def frist_find(s):
    for i in range(len(s)-1):
        if s[i].isalnum() and s[i] == s[i + 1]:
            return s[i]
    return -1
    
s = input().strip()
result = frist_find(s)
print(result)

""" WAP to cprincipal: alc
rate = ulate compound simple interest after taking the principle, rate and time."""
def simple_interest(p,t,r):
    a = p * t * r / 100
    return a

principal = float(input("Enter your principal: "))
rate = float(input("Enter your rate: "))
time = int(input("Enter your time: "))
interest = simple_interest(principal,rate,time) 
print("your interest is = ",interest)

""" WAP to take the temperatures of all 7 days of the week and displays the average temperature of that week."""
def average_temprature():
    l = []
    for i in range(1,8):
        D = float(input(f"Enter your {i} day temprature: "))
        l.append(D)
    average = float(sum(l)/len(l))
    print(f"Your average temprature is = {average:.6f}")

average_temprature()

""" WAP that searches for prime numbers from 10 through 100."""
def priem_number(frist,last):
    for i in range(frist,last+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count+=1
        if count == 2:
            print(i)

a = int(input("Enter your frist number: "))
b = int(input("Enter your last number: "))
priem_number(a,b)