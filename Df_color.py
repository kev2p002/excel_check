import pandas as pd

# Sample DataFrame
data = {
    'Item': ['A', 'B', 'C', 'D'],
    'Importance': ['High', 'Medium', 'Low', 'High']
}

df = pd.DataFrame(data)

# Function to apply colors based on importance
def color_importance(val):
    color = ''
    if val == 'High':
        color = 'red'
    elif val == 'Medium':
        color = 'orange'
    elif val == 'Low':
        color = 'yellow'
    return f'color: {color}'

# Apply the style
styled_df = df.style.applymap(color_importance, subset=['Importance'])

# Display the styled DataFrame in Jupyter Notebook
styled_df
