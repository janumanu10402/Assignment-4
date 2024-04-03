import pandas as pd
from zipfile import ZipFile
import os
import yaml

def execute_process():
    # Get the directory of the current script
    SCRIPTDIR = os.path.dirname(__file__)
    # Load parameters from YAML file
    with open(script_dir+'/fileParams.yaml', 'r') as file:
        params = yaml.safe_load(file)
    # Extract parameters
    file_name = params['file_name']
    field_name = params['field_name']
    
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(file_name)

    # Convert 'DATE' column to datetime format
    data['DATE'] = pd.to_datetime(data['DATE'])
    # Extract month from 'DATE' and create a new column 'Month'
    data['Month'] = data['DATE'].dt.month

    # Calculate the mean of the specified field for each month
    monthly_values = data.groupby('Month')[field_name].mean()

    # Print the monthly mean values
    print(monthly_values)

    # Save the computed monthly mean values to a new CSV file
    monthly_values.to_csv(script_dir+'/monthlyComputed.csv', index=False)

# Call the execute_process function to execute the script
execute_process()
