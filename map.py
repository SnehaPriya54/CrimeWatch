import pandas as pd
import numpy as np
import folium
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import random

# Load the data
print("Loading data...")
data = pd.read_csv('bengaluru_fir_data.csv', low_memory=False)
print(f"Total records: {len(data)}")

# Print column names
print("Available columns:")
print(data.columns.tolist())

# Filter for Bengaluru City and non-null coordinates
bengaluru_df = data[(data['District_Name'] == 'Bengaluru City') & 
                    (data['Latitude'].notnull()) & 
                    (data['Longitude'].notnull())]
print(f"Records for Bengaluru City with valid coordinates: {len(bengaluru_df)}")

# Filter out coordinates that are clearly outside Bengaluru's range
bengaluru_df = bengaluru_df[(bengaluru_df['Latitude'] >= 12.5) & (bengaluru_df['Latitude'] <= 13.5) &
                            (bengaluru_df['Longitude'] >= 77.0) & (bengaluru_df['Longitude'] <= 78.0)]
print(f"Records after filtering out-of-range coordinates: {len(bengaluru_df)}")

# Use the same threat_mapping as in your original code
threat_mapping = {
    'CRIMINAL INTIMIDATION': 'Medium',
    'CASES OF HURT': 'Medium',
    'CHEATING': 'Medium',
    'ROBBERY': 'Medium',
    'MISSING PERSON': 'Medium',
    'Karnataka State Local Act': 'Medium',
    'DACOITY': 'Medium',
    'THEFT': 'Medium',
    'KIDNAPPING AND ABDUCTION': 'Medium',
    'MURDER': 'High',
    'MOLESTATION': 'Medium',
    'ATTEMPT TO MURDER': 'Medium',
    'CRUELTY BY HUSBAND': 'Medium',
    'BURGLARY - NIGHT': 'Medium',
    'CRIMES RELATED TO WOMEN': 'High',
    'CHILDREN ACT': 'Medium',
    'POCSO': 'Medium',
    'BURGLARY - DAY': 'Medium',
    'RAPE': 'High',
    'MISCHIEF': 'Low',
    'NEGLIGENT ACT': 'Low',
    'CRIMINAL TRESPASS': 'Low',
    'CRIMINAL BREACH OF TRUST': 'Low',
    'CYBER CRIME': 'High',
    'Failure to appear to Court': 'Low',
    'OFFENCES AGAINST PUBLIC SERVANTS (Public servant is a victim)': 'Medium',
    'SUICIDE': 'Medium',
    'CONSUMER': 'Low',
    'RIOTS': 'High',
    'NARCOTIC DRUGS & PSYCHOTROPIC SUBSTANCES': 'High',
    'KARNATAKA POLICE ACT 1963': 'Medium',
    'COTPA, CIGARETTES AND OTHER TOBACCO PRODUCTS': 'Medium',
    'INSULTING MODESTY OF WOMEN (EVE TEASING)': 'High',
    'AFFRAY': 'Low',
    'IMMORAL TRAFFIC': 'High',
    'DOWRY DEATHS': 'Medium',
    'PASSPORT ACT': 'Medium',
    'ANIMAL': 'High',
    'SCHEDULED CASTE AND THE SCHEDULED TRIBES': 'Low',
    'DEATHS DUE TO RASHNESS/NEGLIGENCE': 'High',
    'CRIMINAL CONSPIRACY': 'High',
    'PREVENTION OF DAMAGE TO PUBLIC PROPERTY ACT 1984': 'Low',
    'BONDED LABOUR SYSTEM': 'Medium',
    'ARSON': 'High',
    'Disobedience to Order Promulgated by PublicServant': 'Low',
    'ARMS ACT 1959': 'High',
    'OFFENCES RELATED TO MARRIAGE': 'High',
    'FORGERY': 'Low',
    'FALSE EVIDENCE': 'Medium',
    'RECEIVING OF STOLEN PROPERTY': 'Low',
    'PUBLIC SAFETY': 'High',
    'ELECTION': 'Medium',
    'COMMUNAL / RELIGION': 'High',
    'ADULTERATION': 'High',
    'DEFAMATION': 'High',
    'MOTOR VEHICLE ACCIDENTS NON-FATAL': 'Low',
    'MOTOR VEHICLE ACCIDENTS FATAL': 'Medium',
    'CULPABLE HOMICIDE NOT AMOUNTING TO MURDER': 'Medium',
    'EXPOSURE AND ABANDONMENT OF CHILD': 'High',
    'COPYRIGHT ACT 1957': 'Low',
    'ESCAPE FROM LAWFUL CUSTODY AND RESISTANCE': 'Medium',
    'REPRESENTATION OF PEOPLE ACT 1951 & 1988': 'Low',
    'WRONGFUL RESTRAINT/CONFINEMENT': 'Medium',
    'PORNOGRAPHY': 'High',
    'FOREIGNER': 'Low',
    'PUBLIC NUISANCE': 'Low',
    'DEATHS-MISCARRIAGE': 'High',
    'Concealment of birth by secret disposal of Child': 'High',
    'OFFENCES PROMOTING ENMITY': 'Medium',
    'Attempting to commit offences': 'Medium',
    'ASSAULT': 'High',
    'SLAVERY': 'High',
    'POST & TELEGRAPH,TELEGRAPH WIRES(UNLAWFUL POSSESSION) ACT 1950': 'Low',
    'EXPLOSIVES': 'High',
    'CRIMINAL MISAPPROPRIATION': 'High',
    'COUNTERFEITING': 'Low',
    'POISONING-PROFESSIONAL': 'High',
    'IMPERSONATION': 'Medium',
    'Human Trafficking': 'High',
    'ANTIQUES (CULTURAL PROPERTY)': 'Low',
    'UNLAWFUL ACTIVITIES (Prevention) ACT 1967': 'Low',
    'ATTEMPT TO CULPABLE HOMICIDE NOT AMOUNTING TO MURDER': 'Medium',
    'UNNATURAL DEATH (Sec 174/174c/176)': 'Low',
    'CINEMATOGRAPH ACT 1952': 'Low',
    'PUBLIC JUSTICE': 'Low',
    'UNNATURAL SEX': 'High',
    'FOREST': 'High',
    'INDIAN MOTOR VEHICLE': 'Low',
    'OFFENCES BY PUBLIC SERVANTS (EXCEPT CORRUPTION) (Public servant is accused)': 'Medium',
    'DOCUMENTS & PROPERTY MARKS': 'Low',
    'ASSAULT OR USE OF CRIMINAL FORCE TO DISROBE WOMAN': 'High',
    'OF ABETMENT': 'High',
    'OFFICIAL SECURITY RELATED ACTS': 'High',
    'DEFENCE FORCES OFFENCES RELATING TO (also relating to desertion)': 'High',
    'SEDITION': 'Medium',
    'INDIAN ELECTRICITY ACT': 'Low',
    'Giving false information respecting an offence': 'Medium',
    'PREVENTION OF CORRUPTION ACT 1988': 'Low',
    'INFANTICIDE': 'High',
    'NATIONAL SECURITY ACT': 'High',
}
bengaluru_df['Threat_Level'] = bengaluru_df['CrimeHead_Name'].map(threat_mapping)

# Drop rows with NaN in Threat_Level
bengaluru_df = bengaluru_df.dropna(subset=['Threat_Level'])
print(f"Records after mapping threat levels: {len(bengaluru_df)}")

# Prepare features
selected_features = ['FIR_YEAR', 'Latitude', 'Longitude']
features = bengaluru_df[selected_features]

# Convert columns to numeric, replacing non-numeric values with NaN
for col in features.columns:
    features[col] = pd.to_numeric(features[col], errors='coerce')

# Drop rows with NaN in features
features = features.dropna()
print(f"\nRecords after dropping NaN values: {len(features)}")

if len(features) == 0:
    print("Error: No valid data points remaining after preprocessing.")
else:
    # Scale features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Apply PCA
    pca = PCA(n_components=0.5)
    features_pca = pca.fit_transform(features_scaled)

    # For demonstration, let's use random predictions
    # In practice, you would use your trained model here
    predicted_threat_levels = [random.choice(['Low', 'Medium', 'High']) for _ in range(len(features))]

    # Add predicted threat levels to the features DataFrame
    features['Predicted_Threat'] = predicted_threat_levels

    # Create a map centered on Bengaluru
    bengaluru_map = folium.Map(location=[12.9716, 77.5946], zoom_start=11)

    # Define color scheme for threat levels
    color_map = {'Low': 'green', 'Medium': 'orange', 'High': 'red'}

    # Function to create popup content
    def create_popup_content(row, predicted_threat):
        content = f"Year: {int(row['FIR_YEAR'])}<br>"
        content += f"Predicted Threat Level: {predicted_threat}<br>"
        if 'CrimeHead_Name' in row:
            content += f"Crime Type: {row['CrimeHead_Name']}<br>"
        if 'UnitName' in row:
            content += f"Police Station: {row['UnitName']}<br>"
        if 'FIR Type' in row:
            content += f"FIR Type: {row['FIR Type']}"
        return content

    # Add markers for each crime location (limit to 5000 for performance)
    for idx, row in features.head(5000).iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,
            popup=create_popup_content(bengaluru_df.loc[idx], row['Predicted_Threat']),
            color=color_map[row['Predicted_Threat']],
            fill=True,
            fillColor=color_map[row['Predicted_Threat']]
        ).add_to(bengaluru_map)

    # Add a legend
    legend_html = '''
        <div style="position: fixed; bottom: 50px; left: 50px; width: 120px; height: 90px; 
        border:2px solid grey; z-index:9999; font-size:14px; background-color:white;">
        &nbsp; Threat Level <br>
        &nbsp; <i class="fa fa-circle fa-1x" style="color:green"></i> Low <br>
        &nbsp; <i class="fa fa-circle fa-1x" style="color:orange"></i> Medium <br>
        &nbsp; <i class="fa fa-circle fa-1x" style="color:red"></i> High
        </div>
        '''
    bengaluru_map.get_root().html.add_child(folium.Element(legend_html))

    # Save the map
    bengaluru_map.save("bengaluru_threat_map.html")

    print("Map has been saved as 'bengaluru_threat_map.html'")

    # Print some statistics about the predicted threat levels
    threat_level_counts = features['Predicted_Threat'].value_counts()
    print("\nPredicted Threat Level Distribution:")
    print(threat_level_counts)
    print(f"\nTotal points plotted: {min(5000, len(features))}")