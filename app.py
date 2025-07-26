import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load your processed data
df = pd.read_csv('output.csv')

# Ensure data is sorted and date is datetime
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create a line chart
fig = px.line(
    df, 
    x='date', 
    y='sales', 
    color='region',
    title="Pink Morsels Sales Over Time",
    labels={'date': 'Date', 'sales': 'Total Sales ($)'}
)

# Add a vertical line using add_shape and annotation
price_increase = pd.Timestamp('2021-01-15')
fig.add_shape(
    type="line",
    x0=price_increase,
    x1=price_increase,
    y0=0,
    y1=1,
    xref='x',
    yref='paper',
    line=dict(color="red", dash="dash")
)
fig.add_annotation(
    x=price_increase,
    y=1,
    yref="paper",
    text="Price Increase",
    showarrow=False,
    xanchor="left"
)

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div(children=[
    html.H1("Pink Morsels Sales Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(
        id='sales-chart',
        figure=fig
    )
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
