#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import numpy as np

import scipy.stats

import seaborn as sns 
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")


# In[3]:


def flip(n):
    
    result = []
    
    for i in range(1, n+1):
        result.append(random.choice(['Heads', 'Tails']))
        
    return result


# In[4]:


result = flip(10)

result 


# In[5]:


plt.figure(figsize=(12,8))

sns.countplot(x=result)

plt.xlabel('Coin Flip')
plt.title('Counts')

plt.show()


# In[6]:


result = flip(100)

plt.figure(figsize=(12,8))

sns.countplot(x=result)

plt.xlabel('Coin Flip')
plt.title('Counts')

plt.show()


# In[7]:


result = flip(100000)

plt.figure(figsize=(12,8))

sns.countplot(x=result)

plt.xlabel('Coin Flip')
plt.title('Counts')

plt.show()

