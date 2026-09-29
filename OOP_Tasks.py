#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 1
class Person:
    name = ""
    gender = ""
    profession = ""
    study_hour = ""

    def working(self):
        print(self.name, "is working.")

    def study(self):
        print(self.name, "is studying")

p = Person()
p.name= "Ali"
p.gender= "Male"
p.profession= "Student"
p.study_hour= 4

p.working()
p.study()


# In[3]:


#Task 2
class Student:
    name = ""
    roll_no = 0
    program = ""
    marks = 0

s1 = Student()
s1.name = "Ali"
s1.roll_no = 101
s1.program = "BSCS"
s1.marks = 85

print("Name:", s1.name)
print("Roll No:", s1.roll_no)
print("Program:", s1.program)
print("Marks:", s1.marks)


# In[4]:


#Task 3
class Rectangle:
    length = 0
    width = 0

    def calculate_area(self):
        print("Area =", self.length * self.width)

r1= Rectangle()
r1.length = 10
r1.width = 5

r2= Rectangle()
r2.length = 8
r2.width = 4

r1.calculate_area()
r2.calculate_area()


# In[8]:


#Task 4
class BankAccount:
    def __init__(self , account_holder , account_number , balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount

    def withdraw(self , amount):
        self.balance -= amount

    def display_balance(self):
        print("Balance:", self.balance)

account1 = BankAccount("Ali" , 101 , 5000)
account1.deposit(2000)
account1.withdraw(1000)
account1.display_balance()


# In[ ]:




