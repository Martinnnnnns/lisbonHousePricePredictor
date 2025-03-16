import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from model_logging import log_model_operation

def load_processed_data(filepath='./backend/data/processed/lisbon_houses_processed.csv'):
    """
    Args:
        filepath (str): Path to the processed CSV file
    
    Returns:
        pandas.DataFrame or None: The loaded dataset or None if loading fails
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def prepare_data_for_modeling(df):
    """
    Args:
        df (pandas.DataFrame): Input dataframe with raw features
    
    Returns:
        pandas.DataFrame: Processed dataframe with encoded categorical features
    """
    model_df = df.copy()
    
    # Get categorical columns
    categorical_cols = model_df.select_dtypes(include=['object']).columns.tolist()
    
    # For Condition, create ordinal encoding
    if 'Condition' in categorical_cols:
        condition_mapping = {'For Refurbishment': 1, 'Used': 2, 'As New': 3, 'New': 4}
        model_df['Condition'] = model_df['Condition'].map(condition_mapping)
    
    # For PropertyType, create binary encoding
    if 'PropertyType' in categorical_cols:
        property_type_mapping = {'Homes': 1, 'Single Habitation': 2}
        model_df['PropertyType'] = model_df['PropertyType'].map(property_type_mapping)
    
    # For other categorical columns, use one-hot encoding
    remaining_cat_cols = [col for col in categorical_cols 
                          if col not in ['Condition', 'PropertyType']]
    model_df = pd.get_dummies(model_df, columns=remaining_cat_cols, drop_first=True)
    
    return model_df

def split_data(df, target_column='Price', test_size=0.2, random_state=42):
    """
    Args:
        df (pandas.DataFrame): Input dataframe
        target_column (str): Name of the target variable column
        test_size (float): Proportion of data to use for testing
        random_state (int): Random seed for reproducibility
    
    Returns:
        tuple: (X_train, X_test, y_train, y_test) - Training and test sets for features and target
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Testing set: {X_test.shape[0]} samples")
    
    return X_train, X_test, y_train, y_test

def save_model_and_features(model, X_train, model_name, save_dir='./backend/models/saved_models/'):
    """
    Args:
        model: Trained scikit-learn model
        X_train (pandas.DataFrame): Training features dataframe
        model_name (str): Name to use for saving the model
        save_dir (str): Directory path to save model and feature files
    
    Returns:
        None: Saves model and feature files to disk
    """
    os.makedirs(save_dir, exist_ok=True)
    
    # Create model filename with lhp prefix
    model_filename = f'{save_dir}/lhp_{model_name}.pkl'
    joblib.dump(model, model_filename)
    print(f"{model_name} model saved to {model_filename}")
    
    # Save feature names for this model
    feature_list = X_train.columns.tolist()
    feature_filename = f'{save_dir}/lhp_{model_name}_features.pkl'
    joblib.dump(feature_list, feature_filename)
    print(f"Feature list for {model_name} saved to {feature_filename}")
    
    # Save a common feature list for convenience
    common_feature_filename = f'{save_dir}/feature_list.pkl'
    joblib.dump(feature_list, common_feature_filename)
    print(f"Common feature list saved to {common_feature_filename}")

def train_random_forest(X_train, y_train, save_dir=None):
    """
    Args:
        X_train (pandas.DataFrame): Training features
        y_train (pandas.Series): Training target values
        save_dir (str, optional): Directory to save model and features
    
    Returns:
        RandomForestRegressor: Trained Random Forest model with optimized hyperparameters
    """
    # Define the parameter grid for GridSearchCV
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10]
    }
    
    # Perform grid search with cross-validation
    rf_cv = GridSearchCV(
        RandomForestRegressor(random_state=42), 
        param_grid=param_grid,
        cv=5, 
        scoring='neg_mean_squared_error',
        n_jobs=-1
    )
    
    rf_cv.fit(X_train, y_train)
    
    print(f"Best parameters for Random Forest: {rf_cv.best_params_}")
    
    # Train the model with the best parameters
    best_model = RandomForestRegressor(**rf_cv.best_params_, random_state=42)
    best_model.fit(X_train, y_train)
    
    # Save the model if a path is provided
    if save_dir:
        save_model_and_features(best_model, X_train, "random_forest", save_dir)
    
    return best_model

def train_decision_tree(X_train, y_train, save_dir=None):
    """
    Args:
        X_train (pandas.DataFrame): Training features
        y_train (pandas.Series): Training target values
        save_dir (str, optional): Directory to save model and features
    
    Returns:
        DecisionTreeRegressor: Trained Decision Tree model with optimized hyperparameters
    """
    param_grid = {
        'max_depth': [3, 5, 7, 10, None],
        'min_samples_split': [2, 5, 10]
    }
    
    dt_cv = GridSearchCV(
        DecisionTreeRegressor(random_state=42),
        param_grid=param_grid,
        cv=5,
        scoring='neg_mean_squared_error',
        n_jobs=-1
    )
    
    dt_cv.fit(X_train, y_train)
    print(f"Best parameters for Decision Tree: {dt_cv.best_params_}")
    
    best_model = DecisionTreeRegressor(**dt_cv.best_params_, random_state=42)
    best_model.fit(X_train, y_train)
    
    if save_dir:
        save_model_and_features(best_model, X_train, "decision_tree", save_dir)
    
    return best_model

def train_ridge(X_train, y_train, save_dir=None):
    """
    Args:
        X_train (pandas.DataFrame): Training features
        y_train (pandas.Series): Training target values
        save_dir (str, optional): Directory to save model and features
    
    Returns:
        Ridge: Trained Ridge Regression model with optimized alpha parameter
    """
    param_grid = {
        'alpha': np.logspace(-3, 3, 10)
    }
    
    ridge_cv = GridSearchCV(
        Ridge(random_state=42),
        param_grid=param_grid,
        cv=5,
        scoring='neg_mean_squared_error',
        n_jobs=-1
    )
    
    ridge_cv.fit(X_train, y_train)
    print(f"Best parameters for Ridge: {ridge_cv.best_params_}")
    
    # Train final model with best parameters
    best_model = Ridge(alpha=ridge_cv.best_params_['alpha'], random_state=42)
    best_model.fit(X_train, y_train)
    
    if save_dir:
        save_model_and_features(best_model, X_train, "ridge", save_dir)
    
    return best_model

def train_lasso(X_train, y_train, save_dir=None):
    """
    Args:
        X_train (pandas.DataFrame): Training features
        y_train (pandas.Series): Training target values
        save_dir (str, optional): Directory to save model and features
    
    Returns:
        Lasso: Trained Lasso Regression model with optimized alpha parameter
    """
    param_grid = {
        'alpha': np.logspace(-3, 3, 10) 
    }
    
    # Convergence settings
    lasso_cv = GridSearchCV(
        Lasso(
            max_iter=50000,  
            tol=0.01,        
            selection='random',
            random_state=42
        ),
        param_grid=param_grid,
        cv=5,
        scoring='neg_mean_squared_error',
        n_jobs=-1
    )
    
    lasso_cv.fit(X_train, y_train)
    print(f"Best parameters for Lasso: {lasso_cv.best_params_}")
    
    best_model = Lasso(
        alpha=lasso_cv.best_params_['alpha'],
        max_iter=100000,  
        tol=0.01,
        selection='random',
        random_state=42
    )
    best_model.fit(X_train, y_train)
    
    if save_dir:
        save_model_and_features(best_model, X_train, "lasso", save_dir)
    
    return best_model

def train_linear(X_train, y_train, save_dir=None):
    """
    Args:
        X_train (pandas.DataFrame): Training features
        y_train (pandas.Series): Training target values
        save_dir (str, optional): Directory to save model and features
    
    Returns:
        LinearRegression: Trained Linear Regression model
    """
    
    model = LinearRegression(
        fit_intercept=True,  
        n_jobs=-1             
    )
    
    print("Training simple Linear Regression model...")
    model.fit(X_train, y_train)
    
    if save_dir:
        save_model_and_features(model, X_train, "linear", save_dir)
    
    return model

def train_svr(X_train, y_train, save_dir=None):
    """
    Args:
        X_train (pandas.DataFrame): Training features
        y_train (pandas.Series): Training target values
        save_dir (str, optional): Directory to save model and features
    
    Returns:
        SVR: Trained Support Vector Regression model with optimized hyperparameters
    """
    # Simple parameter set
    param_grid = {
        'C': [1.0, 10.0, 100.0],
        'gamma': ['scale', 0.1],
        'kernel': ['rbf', 'linear'],
        'epsilon': [0.01, 0.1]
    }
    
    svr_cv = GridSearchCV(
        SVR(),
        param_grid=param_grid,
        cv=2,                    
        scoring='neg_mean_squared_error',
        n_jobs=-1,
        verbose=1               
    )
    
    print("Starting SVR grid search. This may take a few minutes...")
    svr_cv.fit(X_train, y_train)
    print(f"Best parameters for SVR: {svr_cv.best_params_}")
    
    best_model = SVR(**svr_cv.best_params_)
    best_model.fit(X_train, y_train)
    
    if save_dir:
        save_model_and_features(best_model, X_train, "svr", save_dir)
    
    return best_model

def train_all_models(X_train, y_train, save_dir=None):
    """
    Args:
        X_train (pandas.DataFrame): Training features
        y_train (pandas.Series): Training target values
        save_dir (str, optional): Directory to save models and features
    
    Returns:
        dict: Dictionary of trained models with model names as keys
    """
    models = {}
    
    print("\nTraining Random Forest model...")
    models['random_forest'] = train_random_forest(X_train, y_train, save_dir)
    
    print("\nTraining Decision Tree model...")
    models['decision_tree'] = train_decision_tree(X_train, y_train, save_dir)
    
    print("\nTraining Ridge Regression model...")
    models['ridge'] = train_ridge(X_train, y_train, save_dir)
    
    print("\nTraining Lasso Regression model...")
    models['lasso'] = train_lasso(X_train, y_train, save_dir)
    
    print("\nTraining Linear Regression model...")
    models['linear'] = train_linear(X_train, y_train, save_dir)
    
    print("\nTraining SVR model...")
    models['svr'] = train_svr(X_train, y_train, save_dir)
    
    return models

def main():
    @log_model_operation
    def run_training():
        df = load_processed_data()
        if df is None:
            return
        
        model_df = prepare_data_for_modeling(df)
        X_train, X_test, y_train, y_test = split_data(model_df)
        
        save_dir = './backend/models/saved_models/'
        models = train_all_models(X_train, y_train, save_dir)
        
        print("All models trained and saved successfully!")
        return models, X_train, X_test, y_train, y_test
    
    return run_training()

if __name__ == "__main__":
    main()