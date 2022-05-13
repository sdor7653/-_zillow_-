'''Git_Доровских_ИВТ-13'''

import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv('zillow.csv')
pd.read_csv('zillow.csv',delimiter=',',index_col=False)
sort = table.sort_values(by='ListPrice')
table = pd.DataFrame()
grf = table.groupby('Beds').ListPrice.sum()
grf.plot.bar(x='Beds)',y='ListPrice',rot=0,color='g')
plt.show()
