from sklearn.metrics import r2_score
import pandas as pd
import os

def evaluate_consistency():
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)

    # Read the actual and computed monthly values from CSV files
    actual_monthly_values = pd.read_csv(script_dir+'/monthlyValues.csv')
    computed_monthly_values = pd.read_csv(script_dir+'/monthlyComputed.csv')

    # Adjust the lengths of dataframes if they are not equal
    if len(actual_monthly_values) != len(computed_monthly_values):
        if len(actual_monthly_values) > len(computed_monthly_values):
            actual_monthly_values = actual_monthly_values[:len(computed_monthly_values)]
        else:
            computed_monthly_values = computed_monthly_values[:len(actual_monthly_values)]
    
    # Compute the R-squared score to evaluate consistency between actual and computed values
    r2 = r2_score(actual_monthly_values, computed_monthly_values)
    
    # Check if the dataset is consistent based on the R-squared score
    if r2 >= 0.9:
        print('The dataset is consistent')
    else:
        print('The dataset is not consistent')
    
    # Return the R-squared score
    return r2

# Call the evaluate_consistency function to execute the consistency evaluation
evaluate_consistency()
