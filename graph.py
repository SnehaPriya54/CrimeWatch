import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load the dataset
file_path = r'C:\Users\snehc\Downloads\crime_hotspot\bengaluru_fir_data.csv'  # Update this to your correct file path
fir_data = pd.read_csv(file_path, low_memory=False)

# Clean and preprocess the data
fir_data.columns = fir_data.columns.str.strip()
fir_data['FIR_YEAR'] = pd.to_numeric(fir_data['FIR_YEAR'], errors='coerce')
fir_data['FIR_MONTH'] = pd.to_numeric(fir_data['FIR_MONTH'], errors='coerce')

# Drop rows with missing years or months
fir_data = fir_data.dropna(subset=['FIR_YEAR', 'FIR_MONTH'])

# Create a 'FIR_DATE' column
fir_data['FIR_DATE'] = pd.to_datetime(fir_data['FIR_YEAR'].astype(str) + '-' + fir_data['FIR_MONTH'].astype(str) + '-1')

# Create a new DataFrame for crime types
crime_types = fir_data['CrimeGroup_Name'].value_counts().reset_index()
crime_types.columns = ['Crime_Type', 'Count']

# Initialize Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='crime-type-dropdown',
            options=[{'label': row['Crime_Type'], 'value': row['Crime_Type']} for index, row in crime_types.iterrows()],
            value=crime_types['Crime_Type'].iloc[0],  # Default value
            clearable=False,
            style={'width': '50%', 'margin': '20px auto'}  # Center the dropdown
        ),
        dcc.Graph(id='main-graph', style={'width': '100%', 'height': '60vh'})
    ], style={'textAlign': 'center', 'marginBottom': '50px'})
], style={'textAlign': 'center'})

# Callback to update the main graph based on the selected crime type
@app.callback(
    Output('main-graph', 'figure'),
    Input('crime-type-dropdown', 'value')
)
def update_graph(selected_crime_type):
    # Filter data for the selected crime type
    filtered_data = fir_data[fir_data['CrimeGroup_Name'] == selected_crime_type]
    
    # Group by date to count the number of FIRs for the selected crime type
    crime_trends = filtered_data.groupby('FIR_DATE').size().reset_index(name='crime_count')

    # Create bar graph for the selected crime type
    bar_fig = px.bar(crime_trends, x='FIR_DATE', y='crime_count', 
                     title=f'Crime Trends for {selected_crime_type}', 
                     labels={'FIR_DATE': 'Date', 'crime_count': 'Number of Crimes'},
                     template='plotly_dark')

    return bar_fig

if __name__ == '__main__':
    app.run_server(debug=True)
