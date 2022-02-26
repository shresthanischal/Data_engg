#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import json


# In[2]:


string = open('websiteData.txt',encoding='utf-8').read()
words = open('websiteData.txt',encoding='utf-8').read().split()


# In[3]:


email=re.findall(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)',string)
human_email=re.compile(r'([a-zA-Z]+\.[a-zA-Z]+@)')


# In[7]:


temp={}
for i in range(len(email)):
    count=0
    typ=''
    for j in range(len(words)):
        if(email[i]==words[j]):
            count+=1
    if(human_email.match(email[i])==None):
        typ='NotHuman'
    else:
        typ='Human'
    temp[email[i]]={
            'occurence':count,
            'emailtype':typ
    }


# In[5]:


with open("result.json", "w") as outfile:
    json.dump(temp, outfile)


# In[ ]:




