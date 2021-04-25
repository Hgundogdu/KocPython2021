#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def regress(npX, npY):
    #beta= np.linalg.inv(np.matmul(np.transpose(npX),npX))*np.matmul(np.transpose(npX),npY)
    
    x_mean=np.mean(npX)
    y_mean=np.mean(npY)
    
    beta=(np.sum(npX*npY) - len(npX)*x_mean*y_mean) / (np.sum(npX*npX)-len(npX)*x_mean*x_mean)
    epsilon=(y_mean-beta*x_mean)
    
    y_head= epsilon + beta*npX
    e=y_head-npY
    
    SE=np.sqrt(np.sum(e**2)/(len(npX)-2))
    CI_Up=beta + SE*norm.ppf(0.975)
    CI_Lw=beta - SE*norm.ppf(0.975)
    
    return(beta,epsilon,SE,CI_Up,CI_Lw)

def regPlot(npX, npY):
    reg_result=regress(npX,npY)
    m=reg_result[0]
    n=reg_result[1]

    x_head=np.linspace(np.min(npX),np.max(npX),10001)
    y_head=x_head*m+n


    fig = plt.figure(figsize = (15,10))

    plt.scatter(npX, npY, color = "r", marker = "*", linewidth=2.0)
    plt.plot(x_head, y_head, linewidth=3.0)
    plt.xlabel('GDP')
    plt.ylabel('Electricity Consumption')
    plt.show()


# In[ ]:




