#!/usr/bin/env python
# coding: utf-8

# In[1]:


import regOps
import getWb


# In[2]:


(x,y,z)=getWb.getWb(2013)


# In[3]:


regResults=regOps.regress(x/1000,(y/z))

print('Slope of the regression is: {:8.6f}'.format(float(regResults[0])))
print('Intercept of the regression is: {:8.6f}'.format(float(regResults[1])))
print('SE of the regression is: {:8.6f}'.format(float(regResults[2])))
print('95% CI Upper limit is: {:8.6f}'.format(float(regResults[3])))
print('95% CI Lower limit is: {:8.6f}'.format(float(regResults[4])))


# In[4]:


regOps.regPlot(x/1000,(y/z))


# In[5]:


from sklearn.linear_model import LinearRegression

model = LinearRegression().fit(x/1000, (y/z))
print('Slope of the regression is: {:8.6f}'.format(model.coef_[0,0]))
print('Intercept of the regression is: {:8.6f}'.format(model.intercept_[0]))


# In[ ]:





