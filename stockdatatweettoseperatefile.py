
# coding: utf-8

# In[ ]:


import os
import tweepy as tw
import pandas as pd
import numpy as np


# In[2]:


consumer_key= 'Kzzmf7XB9oZCvjOEtMzamLLlx'
consumer_secret= 'Y2YQTkTjhjPQUFzGKsF6tk8gbPlH4ndkOgBVCCft2Xx8qyL3cA'
access_token= '1263115900733001733-zawsh3VoElT6KMcZ3vJiXnYchquHJg'
access_token_secret= '0Ht7ZyTxvL04crIhBJl32CYHPYVBOLeaeGMZHXkvqmooK'


# In[3]:


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
path='C:\\stockdata\\'


# In[4]:


search_words = ["#Altcoin","#Bitcoin","#Coindesk","#Cryptocurrency","#Gold","#APPL","#GOOG","#YHOO"]
date_since = "2019-07-24"
#new_search = search_words + " -filter:retweets"


# In[5]:


def search(search_word,date_since):
    tweets = tw.Cursor(api.search,q=search_word,
              lang="en",since=date_since).items(40)
    
    user_data=[[tweet.id,tweet.created_at.strftime('%y-%m-%d %a %H:%M:%S'),tweet.user.screen_name,tweet.text] for tweet in tweets]
    
    df = pd.DataFrame(user_data,columns=['tweet id','time of tweet','user id','text'])
    
    df.to_csv(path+search_word+'.csv', index=False)
    print(search_word)
    


# In[6]:


for searchword in search_words:
    search(searchword,date_since)


# In[ ]:


# [tweet.created_at for tweet in tweets]

