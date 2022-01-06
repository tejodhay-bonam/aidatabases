#!/usr/bin/env python
# coding: utf-8

# In[66]:


class Arithmatic:
    def multiplication(self,a,b):
        self.a = a
        self.b = b
        try:
            c = a*b
            return c
        
        except Exception as e:
            return e
    def division(self,a,b):
        
        self.a = a
        self.b = b
        try:
            c = a/b
            return c
        
        except Exception as e:
            return e
    def f1(self,x):
        self.x = x
        y = x*x + 3
        return y
        


# In[ ]:




