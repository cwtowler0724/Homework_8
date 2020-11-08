#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd


# In[2]:


import fiona


# In[3]:


import arcgis


# In[9]:


import numpy as np


# In[10]:


import matplotlib.pyplot as plt


# In[11]:


state = gpd.read_file('C:/Users/cwtow/OneDrive/Documents/CDC Ingo/va.shp')


# In[5]:


state.head()


# In[43]:


pop1997 = state[state['POP1997'] > 200000]


# In[46]:


population = pop1997['POP1997']


# In[50]:


location = pop1997['NAME']


# In[52]:


get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')

x = location
pop = population

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, pop, color='green')
plt.xlabel("Location")
plt.ylabel("Population")
plt.title("Population in Virginia")

plt.xticks(x_pos, x)

plt.show()


# In[ ]:




