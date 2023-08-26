

'''
# 1.Install and Import Dependencies

# In[26]:


get_ipython().system('pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117')


# In[27]:


get_ipython().system('pip install transformers requests beautifulsoup4 pandas numpy')


# In[28]:


from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re


# 2.Instantiate Model

# In[29]:


tokenizer=AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model= AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')


# 3.Encode and Calculate Sentiment

# In[38]:


tokens=tokenizer.encode('This is amazing, I loved it', return_tensors='pt')


# In[39]:


tokens


# In[40]:


tokenizer.decode(tokens[0])


# In[41]:


result=model(tokens)


# In[42]:


result


# In[43]:


int(torch.argmax(result.logits))+1


# 4.Collect Reviews

# In[44]:


r=requests.get('https://www.yelp.com/biz/mejico-sydney-2')
soup=BeautifulSoup(r.text, 'html.parser')
regex=re.compile('.*comment.*')
results=soup.find_all('p',{'class':regex})
reviews=[result.text for result in results]


# In[47]:


reviews[0]


# 5.Load Reviews into Dataframe and Score

# In[48]:


import pandas as pd
import numpy as np


# In[50]:


df=pd.DataFrame(np.array(reviews),columns=['review'])


# In[52]:


df['review'].iloc[0]


# In[53]:


def sentiment_score(review):
    tokens=tokenizer.encode(review, return_tensors='pt')
    result=model(tokens)
    return int(torch.argmax(result.logits))+1


# In[56]:


sentiment_score(df['review'].iloc[4])


# In[57]:


df['sentiment']=df['review'].apply(lambda x: sentiment_score(x[:512]))


# In[59]:


df


# In[ ]:'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re

def sentiment_analyser(link):
    tokenizer=AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    model= AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    
    #tokens=tokenizer.encode('This is amazing, I loved it', return_tensors='pt')
    #tokenizer.decode(tokens[0])
    #result=model(tokens)
    #r=requests.get('https://www.yelp.com/biz/mejico-sydney-2')
    
    r=requests.get(link)
    soup=BeautifulSoup(r.text, 'html.parser')
    regex=re.compile('.*comment.*')
    results=soup.find_all('p',{'class':regex})
    reviews=[result.text for result in results]
    df=pd.DataFrame(np.array(reviews),columns=['review'])
    def sentiment_score(review):
        tokens=tokenizer.encode(review, return_tensors='pt')
        result=model(tokens)
        return int(torch.argmax(result.logits))+1
    df['sentiment']=df['review'].apply(lambda x: sentiment_score(x[:512]))
    


