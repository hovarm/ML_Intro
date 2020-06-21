#!/usr/bin/env python
# coding: utf-8

# ### Problem 1

# In[8]:


def avg(x,y,z):
    return x+y+z
a=avg(1,2,5)
a


# ### Problem 2

# In[15]:


def even(l):
    l2=[i for i in l if i%2==0]
    return len(l2)
my_list=[15,32,16,13,55,53]
even(my_list)


# ### Problem 3

# In[88]:


def func(name, *args):
    if len(args)>=1:        
        print(name + ", your average grade is: " , sum(args)/len(args))
    else:
        print("No grades available for " + name)
a=func("Anne", 15, 17)
a


# ### Problem 4

# In[132]:


class Circle:
    def __init__(self, color, radius):
        self.radius=radius
        self.color=color
        
    def getDesc(self):
        print("A %s circle with radius %s"  % (self.color, self.radius))


# In[133]:


c1=Circle('red', 3)
c1.getDesc()


# ### Problem 5

# In[155]:


class Employee:
    def __init__(self, name, last_name, monthly_salary):
        self.name=name
        self.last_name=last_name
        self.__monthly_salary=monthly_salary
    def getFullName(self):
        return self.name+ " "+ self.last_name
    def annualSalary(self):
        if self.__monthly_salary>100:
            print("High")
        else:
            print("Low")
emp1=Employee("Lily", "Park", 300)
print(emp1.getFullName())
emp1.annualSalary()


# ### Problem 6

# In[237]:


class Car:
    def __init__(self, model,color, max_speed):
        self.model=model
        self.color=color
        self.max_speed=max_speed
    def compareCar(self, car2):
        if self.max_speed>car2.max_speed:
            print("car1 is better than car2")
        else:
            print("car2 is better than car1")

car1=Car("Mercedes", "white", 250)
car2=Car("BMW", "black", 330)
car1.compareCar(car2)


# ### Problem 7

# In[255]:


class Animal:
    def __init__(self, name):
        self.name=name
    def move1(self):
        print('I can move.')
    def move2(self):
        print("I can run really fast")
class Dog(Animal):
    def __init__(self):
       Animal.__init__(self,"Dog") 
d=Dog()
d.move1()
d.move2()


# In[ ]:




