#!/usr/bin/env python
# coding: utf-8

# # Luno Take Home Test

# ### Import Data as Dataframes Into the Notebook

# In[ ]:


import pandas as pd

SampleAccounts = pd.read_csv("https://raw.githubusercontent.com/aqeelwilliams/Luno_TakeHomeTest/main/SampleAccounts.csv")
SampleLedgerEntries = pd.read_csv("https://raw.githubusercontent.com/aqeelwilliams/Luno_TakeHomeTest/main/SampleLedgerEntries.csv")
SampleRates = pd.read_csv("https://raw.githubusercontent.com/aqeelwilliams/Luno_TakeHomeTest/main/SampleRates.csv")
SampleTransactionTypes = pd.read_csv("https://raw.githubusercontent.com/aqeelwilliams/Luno_TakeHomeTest/main/SampleTransactionTypes.csv")


# ## Task 1

# ### Data Exploration

# In[ ]:


SampleLedgerEntries


# In[ ]:


SampleLedgerEntries.describe(include="all")


# In[ ]:


SampleLedgerEntries.dtypes


# In[ ]:


SampleAccounts


# In[ ]:


SampleAccounts.describe(include="all")


# In[ ]:


SampleAccounts.dtypes


# In[ ]:


SampleTransactionTypes


# In[ ]:


SampleTransactionTypes.describe(include="all")


# In[ ]:


SampleTransactionTypes.dtypes


# In[74]:


SampleRates


# In[ ]:


SampleRates.describe(include="all")


# In[75]:


SampleRates.dtypes


# ### Combine Data

# In[67]:


merge = pd.merge(SampleLedgerEntries, SampleAccounts, on='account_id')
merge


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


trans_statement = pd.DataFrame(columns = ['customer_ID', 'transaction_datetime', 'transaction_type', 'transaction_name', 
                                         'currency', 'transaction_amount'])


# In[ ]:


def trans_amount(b, a):
    amt = (a - b) / (10**8)
    return amt

avail = SampleLedgerEntries['available_1e8']
bal = SampleLedgerEntries['balance_1e8']

trans_amount(bal, avail)


# In[ ]:





# In[ ]:





# In[ ]:





# ## Task 2

# In[69]:


SampleRates


# In[ ]:


exchange_rate = SampleRates['exchange_rate_1e6'] / (10**6)


# In[78]:



x = pd.to_datetime(1483228707311, format='%Y%m%d%H%M%S')

