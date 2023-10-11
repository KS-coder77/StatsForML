#!/usr/bin/env python
# coding: utf-8

# In[2]:


import statistics

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")


# In[3]:


forbes_data = pd.read_csv(r"C:\Users\Krupa\Documents\Krups Coding\Untitled Folder\datasets\forbes.csv")

forbes_data.head()


# In[4]:


forbes_data.isnull().sum()


# In[5]:


forbes_data.dropna(inplace=True)

forbes_data.isnull().sum()


# In[7]:


forbes_data.shape


# In[8]:


market_value_mean = forbes_data['Market Value'].mean()
market_value_mean


# In[9]:


market_value_med = forbes_data['Market Value'].median()
market_value_med


# In[10]:


diff_mean_med = market_value_mean - market_value_med
diff_mean_med

#this difference implies there are large number of outliers


# In[11]:


#mode useful for categorical data such as the Sector column 
forbes_data['Sector'].value_counts()


# In[12]:


sector_mode = forbes_data['Sector'].mode()

sector_mode


# In[13]:


#boxplot visual summarises the stats of your data 
plt.figure(figsize = (12,8))

sns.boxplot(data=forbes_data, y ='Market Value', showmeans=True)

plt.axhline(y=market_value_mean, color='r', linestyle='-')
plt.axhline(y=market_value_med, color='g', linestyle='-')

plt.title('Forbes Data')

plt.show()


# In[14]:


# figure above shows lots of outliers, let's limit the y-range to show a better illustration
#datapoints outside of the whiskers are considered to be outliers
#IQR is the blue shaded box (25th and 75th percentile)
plt.figure(figsize = (12,8))

sns.boxplot(data=forbes_data, y ='Market Value', showmeans=True)

plt.ylim(0, 80)

plt.axhline(y=market_value_mean, color='r', linestyle='-')
plt.axhline(y=market_value_med, color='g', linestyle='-')

plt.title('Forbes Data')

plt.show()


# In[15]:


forbes_data.head()


# In[16]:


prof_max = forbes_data['Profits'].max()
prof_max


# In[17]:


prof_min = forbes_data['Profits'].min()
prof_min


# In[18]:


prof_range = prof_max - prof_min
prof_range


# In[19]:


#range is very sensitive to outliers 
#lets use boxplt to visualise profits stats

plt.figure(figsize = (12,8))

sns.boxplot(data=forbes_data, y='Profits', showmeans=True)

plt.title('Forbes Profits Data')

plt.show()


# In[20]:


#due to lots of outliers beyond both upper and lower whiskers, let's limit the y-range 

plt.figure(figsize = (12,8))

sns.boxplot(data=forbes_data, y='Profits', showmeans=True)

plt.ylim(-3,8)

plt.title('Forbes Profits Data')

plt.show()


# In[21]:


#the IQR is not very sensitive to outliers 

Q1 = np.quantile(forbes_data['Profits'], 0.25)
Q1


# In[22]:


Q3 = np.quantile(forbes_data['Profits'], 0.75)
Q3


# In[23]:


IQR = Q3 - Q1 

IQR


# In[24]:


prof_std = forbes_data['Profits'].std()
prof_std


# In[26]:


#variance is square of standard deviation 
prof_var = prof_std **2
prof_var


# In[28]:


#measures of central tendency 
forbes_data.describe()

