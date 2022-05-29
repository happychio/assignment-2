#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Assignment 2

This assignment covers your intermediate profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.

This assignment places heavy emphasis on Python data structures.
'''


# In[ ]:


def specific_filter(l):
    '''Item 1.
    Specific Filter. 2 points.

    Returns the elements of a list that are greater than the integer 50.
    This is called "filtering" each number based on whether it is greater than 50. 
        Filtering is a very common pattern in high-level (i.e., human-readable)
        programming.
    For this number:
        1. The parameter l will be a list of either floats or ints.
    
    Parameters
    ----------
    l: list
        a list of numbers (floats or ints)

    Returns
    -------
    list
        a list of elements in l that are greater than the integer 50
    '''
    # Write your code below this line


# In[46]:


def specific_filter(l):
    x = len(l)
    numlist =[]
    for i in range (x):
        if l[i] > 50:
            numlist.append(l[i])
        
    return numlist


# In[47]:


l = [0,2,3,43,55,66,34,53,52,13]

result = specific_filter(l)
print(result)


# In[ ]:


def general_filter(l, filter_function):
    '''Item 2.
    General Filter. 3 points.

    Returns the elements of a list that return True when passed to a filtering function.
    This is how general filters are done.
    For this number:
        1. The parameter l will be a list of any data type.
        2. The filter_function is just a function that has been passed as an argument to 
            the general_filter function. It accepts a single argument and returns either
            True or False.
    
    Parameters
    ----------
    l: list
        a list of any data type
    filter_function: function
        a function which accepts any data type and returns bool

    Returns
    -------
    '''
    # Write your code below this line


# In[12]:


def general_filter(l, filter_function):
    x = len(l)
    for i in range (x):
        if str(l[i]) == filter_function:
            return True
            break
        else:
            return False


# In[13]:


l = [23,2.3,24,1.3]
filter_function = input("Enter function: ")
test = general_filter(l, filter_function)
print(test)


# In[ ]:


def specific_map(l):
    '''Item 3.
    Specific Map. 2 points.

    Accepts a list of numbers. Returns another list which contains the squares of the
        numbers.
    This is called "mapping" each number to its square. Mapping is a very common pattern
        in high-level (i.e., human-readable) programming.
    For this number:
        1. The parameter l will be a list of either floats or ints.

    Example:
    specific_map([1, 2, 3, 4, 5]) -> [1, 4, 9, 16, 25]
    
    Parameters
    ----------
    l: list
        a list of numbers (floats or ints)

    Returns
    -------
    list
        a list of the squares of the elements in l
    '''
    # Write your code below this line
    
    


# In[44]:


def specific_map(l):
    squares = []
    length = len(l)
    
    for i in range (length):
        num =  int(l[i])
        num = num*num
        squares.append(num)
        
    return squares


# In[45]:


l = []

while True:
    x = input("Enter element: ")
    ask = l.append(x)
    ender = input("Add more? (Y/N)")
    
    if ender == "N":
        break
        
put = specific_map(l)

print(put)


# In[ ]:


def general_map(l, map_function):
    '''Item 4.
    General Map. 3 points.

    Accepts a list of any data type. Returns another list which uses a function to map
        the first lists's elements to the second list.
    This is how general maps are done.
    
    Parameters
    ----------
    l: list
        a list of any data type
    map_function: function
        a function which accepts one argument and returns any data type

    Returns
    -------
    list
        a list which contains the mapped elements of l
    '''
    # Write your code below this line


# In[52]:


def general_map(l, map_function):
    length = len(l)
    new = []
    for i in range (length):
        num =  int(l[i])
        num = l[i] + map_function
        new.append(num)
        
    return new


# In[53]:


l = []

while True:
    x = input("Enter element: ")
    ask = l.append(x)
    ender = input("Add more? (Y/N)")
    
    if ender == "N":
        map_function = input("Enter Something: ")
        break

put = general_map(l, map_function)

print(put)


# In[ ]:




