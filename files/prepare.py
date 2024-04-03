import pandas as pd
from zipfile import ZipFile
import os

# Define field names
field1 = "HourlyDewPointTemperature"
field2 = "MonthlyDewPointTemperature"

def prepare():
    # Get the directory of the current script
    SCRIPTDIR = os.path.dirname(__file__)

    # Extract contents of the zip file
    with ZipFile(SCRIPTDIR+'/weather.zip', 'r') as zObject: 
        zObject.extractall(path=SCRIPTDIR) 

    # List all files in the directory
    files = os.listdir(SCRIPTDIR)
    # Filter out only CSV files
    files = [file for file in files if file.endswith('.csv')]

    file_name = ''

    # Loop through each CSV file
    for f in files:
        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv(f)
        # Check if both field1 and field2 have no missing values
        if data[field2].isnull().sum() < len(data[field2]) and data[field1].isnull().sum() < len(data[field1]):
            # Store the file name
            file_name = f 
            field_name = field1
            # Write file name and field name to a YAML file
            with open(SCRIPTDIR+'/fileParams.yaml', 'w') as file:
                file.write(f'file_name: {file_name}\n')
                file.write(f'field_name: {field_name}\n')

    # Get monthly values from field2 and remove any missing values
    monthlyValues = data[field2]
    monthlyValues.dropna(inplace=True)

    # Save monthlyValues to a new CSV file
    monthlyValues.to_csv(SCRIPTDIR+'/monthlyValues.csv', index=False)

# Call the prepare function to execute the script
prepare()
