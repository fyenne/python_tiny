#!/usr/bin/env python
# coding: utf-8

# In[13]:


import re
from os import walk
import pdfkit
import os


# In[14]:


f = []
for (dirpath, dirnames, filenames) in walk('/Users/fyenne/Desktop/'):
    f.extend(filenames)
    break


# In[16]:


r = re.compile('.{1,}html')
newlist = list(filter(r.match, filenames))


# In[17]:


note = 'note'
num=1
path = r"/Users/fyenne/Desktop/"
for file in newlist:
    os.rename(os.path.join(path,file), os.path.join(path,note)+str(num)+".html")
    num = num + 1


# In[ ]:





# In[ ]:




