#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytest
import unittest


# In[2]:


from arithmatic import Arithmatic


# In[8]:


class Test_arithmatic(unittest.TestCase):
    global s
    s = Arithmatic()
    def test_arithmatic(self):
        z = s.division(12,4)
        self.assertEqual(z,3)
        
        z = s.multiplication(2,3)
        self.assertEqual(z,6)
        
        z = s.f1(3)
        self.assertEqual(z,s.f1(3))
        
    def test_zeroDiv(self):
        z = s.division(9,0)
        self.assertEqual(str(z),str(ZeroDivisionError('division by zero')))
        

        
    def test_alphabetMul(self):
        z = s.multiplication('s','t')
        self.assertEqual(str(z),str(TypeError("can't multiply sequence by non-int of type 'str'")))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[9]:


d = Test_arithmatic()


# In[10]:


d.test_arithmatic()


# In[11]:


d.test_zeroDiv()


# In[12]:


d.test_alphabetMul()


# In[ ]:




