#!/usr/bin/env python
# coding: utf-8

# In[1]:


##scrape a text
from urllib import request 


# In[2]:


url="https://www.gutenberg.org/files/98/98-0.txt"


# In[3]:


response=request.urlopen(url)


# In[5]:


##read and decode it
raw=response.read().decode('utf8')


# In[6]:


import nltk
from nltk.tokenize import word_tokenize
tokens=word_tokenize(raw)
##list of words separated by


# In[7]:


print(tokens[:200])


# In[8]:


##to clean we write regular expression like"\ufee to get rid of tags 
##beautiful soup for scraping different languages
##with loop befor print cam do sen or word token
##how many adj used personal pronouns penstate pos(45)
##can also tty with html re


# In[9]:


#beautifulsoup
#preprocessiong-RE to clean any html tagg
#POS Tagging
#!!


# In[10]:


# 2##nd Experiment
#Stemming:snowball,lanscat,porters


# In[11]:


import nltk
from nltk.stem import PorterStemmer
porter=PorterStemmer()
porter.stem('cacti')


# In[12]:


#works well for certain stemmerPorterStemmer


# In[13]:


import nltk
from nltk.stem import PorterStemmer
porter=PorterStemmer()
porter.stem('happiness')


# In[14]:


import nltk
from nltk.stem import PorterStemmer
porter=PorterStemmer()
porter.stem('Thirsha')


# In[15]:


import nltk
from nltk.stem import PorterStemmer
porter=PorterStemmer()
porter.stem('Singing')


# In[16]:


import nltk
from nltk.stem import LancasterStemmer
porter=PorterStemmer()
porter.stem('Singing')


# In[17]:


import nltk
from nltk.stem import RegexpStemmer
porter=RegexpStemmer('ing')
porter.stem('Walking')


# In[18]:


import nltk
from nltk.stem import RegexpStemmer
porter=RegexpStemmer('ing')
porter.stem('singing')


# In[20]:


import nltk
from nltk.stem import RegexpStemmer
porter=RegexpStemmer('ing$')
porter.stem('singing')
#sing,ring can break this


# In[21]:


#snowball stemmer
import nltk
from nltk.stem import SnowballStemmer
snow=SnowballStemmer('french')
snow.stem('manges')


# In[22]:


##The following languages are supported: Arabic, Danish, Dutch, English, Finnish, French, German, Hungarian, Italian,
##Norwegian, Portuguese, Romanian, Russian, Spanish and Swedish.
##The algorithm for English is documented here: Porter, M.


# In[24]:


##add for loop to stem the entire passage
import nltk
from nltk.stem import PorterStemmer
porter=PorterStemmer()
text="Natural language processing (NLP) is an interdisciplinary subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. The goal is a computer capable of understanding the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves."
stemmed=[porter.stem(token) for token in text.split(" ")]


# In[25]:


print(stemmed[:50])


# In[26]:


##eliminates e in porter


# In[27]:


##add for loop to stem the entire passage
import nltk
from nltk.stem import LancasterStemmer
porter=PorterStemmer()
text="Natural language processing (NLP) is an interdisciplinary subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. The goal is a computer capable of understanding the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves."
stemmed=[porter.stem(token) for token in text.split(" ")]


# In[28]:


print(stemmed[:50])


# In[30]:


from nltk.stem import WordNetLemmatizer
lemma=WordNetLemmatizer()
print(lemma.lemmatize("madam"))


# In[31]:


from nltk.stem import WordNetLemmatizer
lemma=WordNetLemmatizer()
print(lemma.lemmatize("cacti"))


# In[33]:


from nltk.stem import WordNetLemmatizer
lemma=WordNetLemmatizer()
print(lemma.lemmatize("mice"))


# In[35]:


##lemmatizer allows to give am as be
from nltk.stem import WordNetLemmatizer
lemma=WordNetLemmatizer()
print(lemma.lemmatize("am",pos='v'))


# In[36]:


##lemmatizer allows to give am as be
from nltk.stem import WordNetLemmatizer
lemma=WordNetLemmatizer()
print(lemma.lemmatize("is",pos='v'))


# In[37]:


##lemmatizer allows to give am as be
#pos is parts of speech
from nltk.stem import WordNetLemmatizer
lemma=WordNetLemmatizer()
print(lemma.lemmatize("good",pos='v'))


# In[ ]:




