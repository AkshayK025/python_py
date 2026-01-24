import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
load_dotenv() 
apr_ppm = os.getenv("apr_ppm")
l1 = list(range(1,11))
print(l1,"type:",type(l1))
s = pd.Series(l1)
print(s,"type:",type(s))
data = {'Name':['Elon','Jeff','Mark'],
        'Age':[40,50,35]}
df = pd.DataFrame(data)

print(df,type(df))
df= pd.read_excel(apr_ppm,names='partwise rejection')
df.head()
