#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import numpy as np


# In[4]:


df = pd.read_csv('salaries1.csv')


# In[5]:


df.head()


# In[6]:


year = df['years']


# In[7]:


salary = df['total_value']


# In[21]:


plt.scatter(year, salary, marker ='x')

plt.xlabel('Year')
plt.ylabel('Salary')
title = 'Ken Griffey Jr Salary'
plt.title(title)
plt.show()


# In[ ]:




