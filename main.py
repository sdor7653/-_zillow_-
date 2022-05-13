'''Задача_5'''

import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv('udemy_courses.csv')
pd.read_csv('udemy_courses.csv',delimiter=',',index_col=False)
sort = table.sort_values(by='level')
table = pd.DataFrame(sort)
sum_sub_subject = table.groupby('subject').num_subscribers.sum()
sum_sub_subject.plot.bar(x='subject',y='num_subscribers',color='r',
                         rot=0,subplots=True,figsize=(8,5))
plt.show()
sum_sub_levels = table.groupby('level').num_subscribers.sum()
sum_sub_levels.plot.bar(x='level',y='num_subscribers',color='g',
                        rot=0,subplots=True)
plt.show()
