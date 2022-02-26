#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Import libraries
import numpy as np

import pandas as pd

from pandas_profiling import ProfileReport #the report will display the EDA report


# In[19]:


from sklearn.datasets import load_diabetes #load dataset already present in sklearn


# In[20]:


diab_data=load_diabetes() #initialize load_diabetes


# In[21]:


df=pd.DataFrame(data=diab_data.data,columns=diab_data.feature_names) #.data=dataset,, .features_names=features


# In[22]:


df.head()


# In[23]:


df.columns


# In[24]:


##To create the simple report quickly

profile=ProfileReport(df, title='Pandas Profiling Report', explorative=True)


# In[25]:


profile.to_widgets()


# In[26]:


profile.to_file('output.html')


# ## Titanic Dataset
# 

# In[28]:


df=pd.read_csv(r"C:\Users\miria\OneDrive\GoogleDataAnalytics\Project\train.csv")


# In[29]:


df.head()


# In[30]:


## create  profile report quickly
profile=ProfileReport(df,title='Pandas profiling report', explorative=True)


# In[31]:


profile.to_widgets()


# In[32]:


profile.to_file('output1.html')


# In[ ]:




