#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[3]:


url = "https://iam.cn-north-1.myhuaweicloud.com/v3/auth/tokens"

data = {
  "auth": {
    "identity": {
      "methods": [
        "password"
      ],
      "password": {
        "user": {
          "name": "yangtianyu92",
          "password": "Jmsht1993",  
          "domain": {
            "name": "yangtianyu92"  
          }
        }
      }
    },
    "scope": {
      "project": {
        "name": "cn-north-1"  
      }
    }
  }
}

header = {"Content-Type":"application/json" }


# In[4]:


response = requests.post(url=url, headers=header, json=data)


# In[5]:


token = response.headers["X-Subject-Token"]
response.headers


# In[6]:


header_token = { "Content-Type" : "application/json",
"X-Auth-Token" : token }


# In[7]:


import base64
import wave


# In[83]:


with open("th4.wav", "rb+") as f:
    c1 = f.read()
wav_base64 = base64.b64encode(c1)


# In[84]:


url_s = "https://sis.cn-north-1.myhuaweicloud.com/v1.0/voice/asr/sentence"

data_s = {
  "data": wav_base64.decode(),
  "encode_type": "wav",
  "sample_rate": "16k"
} 

response = requests.post(url=url_s, headers=header_token, json=data_s)


# In[85]:


response.json()


# In[82]:


len(response.json()["result"]["words"])


# In[28]:


10/ 61


# In[86]:


asum  = [1, 0.9, 1, 1, 1]
sum(asum)/len(asum)


# In[ ]:




