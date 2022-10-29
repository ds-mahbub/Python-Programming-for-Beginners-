#!/usr/bin/env python
# coding: utf-8

# ## Variables and Data Types

# In[1]:


print('Hello World!')


# In[2]:


print("-_-")


# In[3]:


print("*" * 10) #Expressions


# ## 1.Variables & Data Types
# 

# In[4]:


movie_name = "Hawa"  # String

released_year = 2022 # int

rating = 8.1         # Float

is_new = True        # Bool


# # 2. Receiving input

# In[5]:


# Receiving user input using input()
usr_input = input("What is your name? ")

print('Welcome! '+ usr_input) # concatenation, we are concatinating usr_input and "Welcome!"

# print('Welcome!', usr_input)


# In[6]:


# Receiving name from user
name = input('Please Enter Your Name: \n')

# Receiving user age
birth_year = int(input('Please Enter Year Birth Year: \n'))

# Declaring a variable present year 
present_year = 2022

'''Calculating age, we will get the age by Subtracting birth_year 
from present_year'''

age = present_year - birth_year

# Printing the output

print(name + " , You are " + str(age) + " years old.")


# ## Printing the output

# In[7]:


print(name + " , You are " + str(age) + " years old.")


# ## Strings 
# 

# Textual Data in Python is ultimately String.

# In[8]:


# Suppose we want to print a string.
print('Hello World')


# In[9]:


# If we assing that "Hello World" in a variable
message = "Hello World"


# # Some Functions & Methods for string handling 

# ## 1. len()

# In[10]:


# printing the lenght of our string "Hello World"
print(len(message))


# Access Individual Characters from a String

# In[12]:


print(message[0:5])


# In[13]:


print(message[:5])


# In[14]:


print(message[6:])


# In[15]:


print(message[-1])


# In[16]:


# To make a copy of a string 
print(message[:])


# ### Lower()

# In[17]:


print(message.lower())


# ### Upper()

# In[18]:


print(message.upper())


# ### Count()

# In[23]:


print(message.count('l'))
print(message.count('Hello'))
print(message.count('hello'))


# ### Find()

# In[25]:


message.find('l')


# ### Replace()

# In[29]:


new_msg = message.replace('Hello', 'Hola')
print(new_msg)


# ### Concatenating two or more strings

# In[33]:


greeting = 'Hello'
name = 'Mahbub'
msg = greeting + ', ' + name + ". Welcome!"
print(msg)


# ## String Formatting 

# In[34]:


new_msg = "{}, {}. Welcome!".format(greeting, name)
new_msg


# In[35]:


new_msg2 = f'{greeting}, {name}. Welcome!'
new_msg2


# ### Getting Help 

# In[37]:


print(dir(msg))


# In[38]:


print(help(str))


# In[42]:


print(help(str.lower))


# In[ ]:




