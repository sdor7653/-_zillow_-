'''Графики с Plotly_8_работа'''

import pandas as pd
import plotly.express as px

pd.read_csv('../trees.csv', delimiter=',', index_col=False)
figs = px.imshow(df,
                labels=dict(x="Long",y="Volume"),
                x=['Girth', 'Height'],
                y='Volume'
                )
figs.show()

male = pd.read_csv("oscar_age_male.csv")
female = pd.read_csv("oscar_age_female.csv")
male['floor'] = 'm'
female['floor'] = 'w'
cont = pd.concat([male, female])
fig = px.scatter(cont, x='Year', y='Age', color='g', title='ID')

fig.show()
