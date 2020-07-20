
# coding: utf-8

# In[52]:


import os
import tweepy as tw
import pandas as pd
import numpy as np


# In[53]:


consumer_key= 'Kzzmf7XXXXXXXXXXXXXXXXXXXXXXXXXXXXXzamLLlx'
consumer_secret= 'Y2YXXXXXXXXXXXXXXXXXXXXL3cA'
access_token= '126XXXXXXXXXXXXXXXXXXXXHJg'
access_token_secret= '0HXXXXXXXXXXXXXXXXXXXXK'


# In[54]:


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# In[55]:


def Search(username):
    for tweet in api.user_timeline(id=username, count=count):
        myposts.append((tweet.created_at.strftime('%y-%m-%d %a %H:%M:%S'),tweet.user.screen_name,tweet.text))


# In[56]:


myposts=[]
username = 'augustin3_jose'
count = 10
Search(username)
df = pd.DataFrame(myposts,columns=['Date Posted','User Name','Tweet'])


# In[57]:


#print(df) 
df

