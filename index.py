import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv('retail_price.csv')
print(data.head())
print(data.isnull().sum())
print(data.describe())

fig = px.histogram(data, 
                   x='total_price', 
                   nbins=20, 
                   title='Distribution of Total Price')
fig.show()

fig = px.box(data, 
             y='unit_price', 
             title='Box Plot of Unit Price')
fig.show()

fig = px.scatter(data, 
                 x='qty', 
                 y='total_price', 
                 title='Quantity vs Total Price', trendline="ols")
fig.show()