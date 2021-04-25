#!/usr/bin/env python
# coding: utf-8

# In[2]:


import wbdata
import datetime
import pandas as pd
import numpy as np




def getWb(year):
    data_date = datetime.datetime(year, 1, 1)
    x=wbdata.get_data("NY.GDP.PCAP.CD", data_date = data_date, pandas = True)
    y=wbdata.get_data("1.1_TOTAL.FINAL.ENERGY.CONSUM", data_date = data_date, pandas = True)
    z=wbdata.get_data("SP.POP.TOTL", data_date = data_date, pandas = True)
    
    data = pd.concat([x, y, z], axis = 1)
    data.columns=["GDP","Energy_Consumption", "Population"]
    data = data.dropna(axis=0, how="any")
    df=pd.DataFrame(data)
    df.to_csv("out.csv")
    x=np.transpose(np.array([data["GDP"].tolist()]))
    y=np.transpose(np.array([data["Energy_Consumption"].tolist()]))
    z=np.transpose(np.array([data["Population"].tolist()]))
    return(x,y,z)

# In[ ]:




