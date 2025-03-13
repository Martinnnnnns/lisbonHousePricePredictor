"""
Utility functions for data operations in the Lisbon House Price Prediction project.
Contains functions moved from preprocessing.py for better code organization.
"""
import os
import pandas as pd

def load_data(filepath='./lisbon-houses.csv'):
    """
    Load the raw dataset from CSV.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Raw data
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def save_processed_data(df, filepath=None, decimal_places=3):
    """
    Save the processed dataframe to CSV with limited decimal places.
    
    Args:
        df (pd.DataFrame): Processed dataframe
        filepath (str): Path to save the CSV file
        decimal_places (int): Number of decimal places to round numeric values
        
    Returns:
        bool: True if saved successfully, False otherwise
    """
    try:
        df_rounded = df.copy()
        float_cols = df_rounded.select_dtypes(include=['float64']).columns
        
        if not float_cols.empty:
            df_rounded[float_cols] = df_rounded[float_cols].round(decimal_places)
        
        if filepath is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(script_dir, '..', 'data', 'processed', 'lisbon_houses_processed.csv')
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        df_rounded.to_csv(filepath, index=False, float_format=f'%.{decimal_places}f')
        print(f"Processed data saved to {filepath} with {decimal_places} decimal places")
        return True
    except Exception as e:
        print(f"Error saving processed data: {e}")
        return False

def check_missing_values(df):
    """
    Check and report missing values in a dataframe.
    
    Args:
        df (pd.DataFrame): Dataframe to check
        
    Returns:
        pd.Series: Series with count of missing values per column
    """
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("Missing values found:")
        missing = missing[missing > 0]
        missing_percent = (missing / len(df) * 100).round(2)
        missing_info = pd.DataFrame({
            'Count': missing,
            'Percentage': missing_percent
        })
        print(missing_info)
        return missing
    else:
        print("No missing values found.")
        return missing

def explore_numeric_features(df, target_column=None):
    """
    Provide basic statistics for numeric features in a dataframe.
    
    Args:
        df (pd.DataFrame): Dataframe to explore
        target_column (str): Optional target column to calculate correlations
        
    Returns:
        pd.DataFrame: Dataframe with statistics for numeric columns
    """
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    # Basic statistics
    stats = df[numeric_cols].describe().T
    
    # Add more statistics
    stats['missing'] = df[numeric_cols].isnull().sum()
    stats['missing_pct'] = (df[numeric_cols].isnull().sum() / len(df) * 100).round(2)
    
    # Add correlation with target if provided
    if target_column is not None and target_column in df.columns:
        stats['corr_with_target'] = [
            df[col].corr(df[target_column]) if col != target_column else 1.0
            for col in numeric_cols
        ]
    
    print("Numeric feature statistics:")
    print(stats)
    return stats

def preprocess_input(input_data, feature_names):
    """
    Preprocess input data to match the format expected by the model.
    
    Args:
        input_data (dict): Dictionary containing house features
        feature_names (list): List of feature names expected by the model
        
    Returns:
        pd.DataFrame: Preprocessed data ready for prediction
    """
    input_df = pd.DataFrame([input_data])
    
    # Handle condition encoding
    if 'Condition' in input_df.columns:
        condition_mapping = {'For Refurbishment': 1, 'Used': 2, 'As New': 3, 'New': 4}
        input_df['Condition'] = input_df['Condition'].map(condition_mapping)
    
    # Handle property type encoding
    if 'PropertyType' in input_df.columns:
        property_type_mapping = {'Homes': 1, 'Single Habitation': 2}
        input_df['PropertyType'] = input_df['PropertyType'].map(property_type_mapping)
    
    # One-hot encode categorical columns that were one-hot encoded during training
    categorical_cols = [col for col in input_df.columns if input_df[col].dtype == 'object']
    
    # Create dummy variables for categorical columns
    input_df = pd.get_dummies(input_df, columns=categorical_cols)
    
    # Ensure all expected features are present, adding missing ones with 0 values
    for feature in feature_names:
        if feature not in input_df.columns:
            input_df[feature] = 0
    
    # Ensure columns are in the same order as during training
    input_df = input_df[feature_names]
    
    return input_df