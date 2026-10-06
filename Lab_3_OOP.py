#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Example 1
class Time:
    def __init__(self, hour, min):
        self.setHour(hour)
        self.setMin(min)

    def setHour(self, hour):
        if 0 <= hour <= 23:
            self.__hour = hour
        else:
            raise ValueError("Invalid hour value")

    def setMin(self, min):
        if 0 <= min <= 59:
            self.__min = min
        else:
            raise ValueError("Invalid min value")

    def getHour(self):
        return self.__hour

    def getMin(self):
        return self.__min

t = Time(15 , 45)

print(t.getHour())

t.setHour(22)

print(t.getHour())










# In[14]:


#Example 2
class Student:
    def __init__(self, n, a):
        self.setName(n)
        self.setAge(a)

    def setName(self , n):
        self.__name = n 

    def setAge(self , a):
        if a < 100 and a > 0:
            self.__age = a
        else:
            raise ValueError("Age is not proper!")

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def display(self):
        print("Name: ", self.__name, "Age: ", self.__age)

s1= Student("Ali" , 22)
s2= Student("Ahmed" , 23)

s1.setAge(34)

s1.display()
s2.display()


# In[21]:


#Example 3
class Person:
    def __init__(self):
        self.__age = 1

    def setage(self, age):
        if 0<= age <=100:
            self.__age = age
        else:
            raise ValueError("Invalid age Value")

    def getage(self):
        return self.__age

    def display(self):
        print("Your age is ", self.__age)

p1 = Person()

print(p1.getage())

p1.setage(34)

p1.display()


# In[23]:


#Example 4 
class Room:
    def __init__(self, l , w):
        self.__length = l
        self.__width = w

    @property 
    def length(self):
        return self.__length

    @length.setter
    def length(self, l):
        self.__length = l

    def area(self):
        return self.__length * self.__width

r1 = Room(2, 3)

print("Area of room is:" , r1.area())

r1.length = 4

print("Area of room is:" , r1.area())

print("Length of room is:" , r1.length)




# In[28]:


#Task 
class Room:
    def __init__(self, l ,w):
        self.setLength(l)
        self.setWidth(w)

    def setLength(self , l):
        if l >0:
            self.__length = l
        else:
            raise ValueError("Invalid length")

    def setWidth(self , w):
        if w >0:
            self.__width = w
        else:
            raise ValueError("Invalid width")

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

    def __calculateArea(self):
        return self.__length * self.__width

    def display(self):
        print("Length:" ,self.__length)
        print("Width:" , self.__width)
        print("Area:" , self.__calculateArea())

r1 = Room(5 , 4)

r1.display()

r1.setLength(6)

r1.display()




# In[29]:


#Lab Program
class Name:
    def __init__(self, age):
        self.__age = age

    def set_age(self , x):
        self.__age = x

    def get_age(self):
        return self.__age

Saif = Name(0)
Saif.set_age(20)
print(Saif.get_age())


# In[ ]:




