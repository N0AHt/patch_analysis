import plotly.express as px
import pandas as pd

# Sample DataFrame
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14],
    'category': ['A', 'B', 'C', 'D', 'E']
}

df = pd.DataFrame(data)

# Create an interactive scatter plot
fig = px.scatter(df, 
                 x='x', 
                 y='y', 
                 hover_data=['category'],  # This column will appear when hovering
                 title="Interactive Scatter Plot with Hover",
                 labels={"x": "X Axis", "y": "Y Axis"})

# Show the plot
fig.write_html('first_figure.html', auto_open=True) # https://stackoverflow.com/questions/68924471/plotly-express-doesnt-load-and-refuse-to-connect
