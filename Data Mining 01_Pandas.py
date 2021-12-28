#!/usr/bin/env python
# coding: utf-8

# 
# # 1: Data Warm-Up

# ## What I can do:
# - Explore the Dataset -- using Python's Pandas.
#     - Upload the CSV file to this machine.
#     - Load the dataset from the CSV file.
#     - Get general information about the data.
#     
# - Basic exploratory questions using Python.
# - Basic data visualisation using Python.

# ## 1.   Explore the Dataset -- using Python's `Pandas`
# ### 1.1   Upload the CSV file to this machine.
# ### 1.2   Load the dataset from the CSV file:

# In[1]:


import pandas as pd
df = pd.read_csv('./LondonCars2014.csv')


# ### 1.3   Get general information about the data:
# 
# 

# In[2]:


df.head()


# We have noticed that the data-types are not exactly correct. For instance, the type for the `Doors` attribute (column) is inferred as numeric (64-bit integer), so we need to fix them.

# In[3]:


df = df.astype({'Make':'category', 'Model':'category', 'Year':'category', 
                'Mileage':'int32', 'Price':'int64', 'Body Style':'category', 
                'Ex Color':'category' , 'In Color':'category', 
                'Engine':'category', 'Transmission':'category', 'Doors':'category'})


# Now, use the `info` method again to check if it had the desired effect:

# In[4]:


df.info()


# 
# 
# ## 2. Basic exploratory questions using Python
# 
# 

# Here we compute various summary statistics, which are quantities, such as the mean and standard deviation, that capture various characteristics of a potentially large set of values with a single number or a small set of numbers. 
# 

# In[5]:


print(df.shape)


# In[6]:


# a pandas dataframe has an attribute called columns:
print(df.columns)


# In[7]:


# the "unique" method helps: 
print('Possible body styles:')
print(df['Body Style'].unique())


# In[8]:


print(df['Doors'].value_counts())


# In[9]:


# the average price of a Honda car versus a Mercedes-Benz car?

# For Honda:
print('Average price of a Honda car = {:.2f}'.format(df[df['Make'] == 'Honda']['Price'].mean()))
# For Mercedes-Benz:
print('Average price of a Mercedes-Benz car = {:.2f}'.format(df[df['Make'] == 'Mercedes-Benz']['Price'].mean()))


# It is also possible to display the summary for all the attributes simultaneously in a table using the describe() function. If an attribute is quantitative, it will display its mean, standard deviation and various quantiles (including minimum, median, and maximum) values. If an attribute is qualitative, it will display its number of unique values and the top (most frequent) values. 
# 

# In[10]:


df.describe(include='all')


# Note that count refers to the number of non-missing values for each attribute.

# In[11]:


print('Covariance:')
df.cov()


# In[12]:


print('Correlation:')
df.corr()


# ---

# ## 3. Basic data visualisation using Python
# 

# Data visualization is the display of information in a graphic or tabular format. Successful visualization requires that the data (information) be converted into a visual format so that the characteristics of the data and the relationships among data items or attributes can be analyzed or reported. 
# 

# ---
# > To display the histogram for the milieage attribute by discretizing it into 8 separate bins and counting the frequency for each bin, run this code:
# 
# **<font color="red"></font>**

# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')

df['Mileage'].hist(bins=8)


# > A boxplot can also be used to show the distribution of values for each attribute.
# 
# **<font color="red"></font>**

# In[14]:


df.boxplot()


# > We can finally plot pairwise relationships in a dataset by running the code below. By default, this function will create a grid of axes such that each numeric variable in our dataset will be shared across the y-axes across a single row and the x-axes across a single column. In the diagonal plots, a univariate distribution plot is drawn to show the marginal distribution of the data in each column. Here scatterplot() is used for each pairing of the variables and histplot() for the marginal plots along the diagonal.
# 
# **<font color="red"></font>**

# In[15]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(df)

