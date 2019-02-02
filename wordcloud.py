#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image


# In[3]:


im=cv2.imread("use_img.png")


# In[4]:


mask=np.array(im)


# In[5]:


wc = WordCloud(background_color="Black", max_words=1000, mask=mask,max_font_size=90, random_state=42)


# In[6]:


text="Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. Van Rossum led the language community until stepping down as leader in July 2018.Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python other implementations. Python and CPython are managed by the non-profit Python Software Foundation."


# In[7]:


wf=wc.generate(text)


# In[10]:


plt.figure(figsize=(10,10))
plt.imshow(wf)


# In[ ]:





# In[ ]:




