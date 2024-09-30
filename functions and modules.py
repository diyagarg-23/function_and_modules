#!/usr/bin/env python
# coding: utf-8

# In[3]:


#function without parameter
def my_function():
    print("Hello! This is my first function.")
    
my_function() #calling a function


# In[6]:


#function with parameters - Creating a Function
def function(num):
    if num%2==0:
        return("even") #to let a function return a value, use return statement
    else:
        return("odd")
function(8)


# In[7]:


def power(a=2,b=2): #values assigned as default arguements
    return(a**b)
power(4)


# In[8]:


power(2,3) #positional arguements :- value 2 gets assigned to a and 3 to b based on positions 


# In[10]:


power(b=8,a=2) #keyword arguements- supercedes positional arguements


# In[11]:


#*args
#def mul(a,b,c)

def mul(*args): #it can be any word not just args, * tells the function that variable no of positional arguements
    product = 1
    for i in args:
        product =product *i
    return product

mul(1,2,3,4,5)
    


# In[14]:


#scope of variable 
a=1

#uses global because there is no local 'a'
def f():
    print('inside f(): ',a)
    
#variable 'a' is redefined as a local
def g():
    a=12
    print('inside g(): ',a)
    
#uses global keyword to modify global 'a'
def h():
    global a
    a=34
    print('inside g(): ',a)
    
#Global scope
print('global: ',a)
f()
print('global: ',a)
g()
print('global: ',a)
h()
print('global: ',a)


# In[15]:


#modules

import math

#constants
print('value of Pi: ',math.pi)

#square root
print('square root of 16: ',math.sqrt(16))

#power
print("2 raised to the power 4 is: ",math.pow(2,4))


# In[16]:


from math import sqrt,pi

#directly using the imported functions/variables
print(sqrt(25)) 
print(pi)


# In[17]:


#python defines a set of functions that are used to generate or manipulate random numbers through the function random
import random
num = random.random() #random() generates a random float number between 0.0 and 1.0
print(num)


# In[20]:


"""generating a random number using choice()
python random.choice() is an inbuilt function in the python programming language that returns a random number"""
import random
#prints a random item from the string
string= 'striver'
print(random.choice(string))


# In[22]:


#the random module offers a function that can generate python random numbers from a specified range and step size
print('a random number from range is: ',end='')
print(random.randrange(20,50,3))


# In[23]:


import random

def generate_lottery_numbers():
    return random.sample(range(1,50),6) #generates 6 unique lottery numbers between 1 and 49

lottery_numbers = generate_lottery_numbers()
print("your lottery numbers are: ",lottery_numbers)


# In[ ]:




