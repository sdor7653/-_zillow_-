'''Графики с Plotly'''

import pandas as pd
import plotly.express as px

df = pd.read_csv('../trees.csv')
pd.read_csv('../trees.csv', delimiter=',', index_col=False)
fig = px.imshow(df,
                labels=dict(x="Long",y="Volume"),
                x=['Girth', 'Height'],
                y='Volume'
                )
fig.show()
