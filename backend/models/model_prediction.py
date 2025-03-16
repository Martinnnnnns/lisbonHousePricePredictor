import joblib
import pandas as pd
import numpy as np
import os

def list_available_models(models_dir='./backend/models/saved_models/'):
    """
    Args:
        models_dir (str): Directory path containing the saved models
    
    Returns:
        list: List of available model names without the 'lhp_' prefix and '.pkl' extension
    """
    try:
        # Filter out feature files
        model_files = [f for f in os.listdir(models_dir) 
                     if f.startswith('lhp_') and f.endswith('.pkl')
                     and not f.endswith('_features.pkl')]
        
        # Extract model names from filenames
        model_names = [f.replace('lhp_', '').replace('.pkl', '') for f in model_files]
        
        if model_names:
            print("Available models:")
            for i, name in enumerate(model_names, 1):
                print(f"  {i}. {name}")
        else:
            print("No models found in the specified directory.")
            
        return model_names
    except Exception as e:
        print(f"Error listing models: {e}")
        return []

def load_model(model_name, models_dir='./backend/models/saved_models/'):
    """
    Args:
        model_name (str): Name of the model to load
        models_dir (str): Directory path containing the saved models
    
    Returns:
        object or None: Loaded scikit-learn model object or None if loading fails
    """
    try:
        model_path = f"{models_dir}/lhp_{model_name}.pkl"
        model = joblib.load(model_path)
        print(f"Model '{model_name}' loaded successfully from {model_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def load_feature_names(model_name, models_dir='./backend/models/saved_models/'):
    """
    Args:
        model_name (str): Name of the model to load features for
        models_dir (str): Directory path containing the saved models and features
    
    Returns:
        list or None: List of feature names used by the model or None if loading fails
    """
    try:
        # First try model-specific features
        features_path = f"{models_dir}/lhp_{model_name}_features.pkl"
        
        # If not found, try the common features file
        if not os.path.exists(features_path):
            features_path = f"{models_dir}/feature_list.pkl"
            
        feature_names = joblib.load(features_path)
        print(f"Feature names loaded from {features_path}")
        return feature_names
    except Exception as e:
        print(f"Error loading feature names: {e}")
        return None

def preprocess_input(input_data, feature_names):
    """
    Args:
        input_data (dict): Dictionary containing house features
        feature_names (list): List of feature names expected by the model
        
    Returns:
        pandas.DataFrame: Preprocessed data ready for prediction with columns matching model features
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

def predict_price(model, input_data, feature_names, model_name=None, models_dir='./backend/models/saved_models/'):
    """
    Args:
        model: Trained scikit-learn model object
        input_data (dict): Dictionary containing house features
        feature_names (list): List of feature names expected by the model
        model_name (str, optional): Name of the model for logging purposes
        models_dir (str): Directory containing models
        
    Returns:
        float: Predicted house price
    """
    processed_input = preprocess_input(input_data, feature_names)
    
    prediction = model.predict(processed_input)[0]
    return prediction

def predict_with_all_models(input_data, models_dir='./backend/models/saved_models/'):
    """
    Args:
        input_data (dict): Dictionary containing house features
        models_dir (str): Directory containing the trained models
        
    Returns:
        dict: Dictionary with model names as keys and their predictions as values,
              includes 'ensemble_average' key with the average of valid predictions
    """
    model_names = list_available_models(models_dir)
    predictions = {}
    valid_predictions = []
    excluded_models = []
    
    for model_name in model_names:
        model = load_model(model_name, models_dir)
        feature_names = load_feature_names(model_name, models_dir)
        
        if model is not None and feature_names is not None:
            try:
                pred = predict_price(model, input_data, feature_names, model_name, models_dir)
                predictions[model_name] = pred
                
                # Check if prediction is above 1 million euros
                if pred > 1000000:
                    print(f"{model_name.capitalize()} prediction: €{pred:.2f} (excluded from ensemble - above €1M)")
                    excluded_models.append(model_name)
                else:
                    print(f"{model_name.capitalize()} prediction: €{pred:.2f}")
                    valid_predictions.append(pred)
            except Exception as e:
                print(f"Error making prediction with {model_name}: {e}")
    
    # Calculate average prediction using only valid predictions (below 1 million euros)
    if valid_predictions:
        avg_prediction = sum(valid_predictions) / len(valid_predictions)
        predictions['ensemble_average'] = avg_prediction
        print(f"Ensemble average prediction: €{avg_prediction:.2f} (excluding {len(excluded_models)} models with predictions above €1M)")
        
        if excluded_models:
            print(f"Excluded models: {', '.join(excluded_models)}")
    else:
        print("Warning: No valid predictions below €1M threshold.")
        
        # Fallback to using all predictions if none are below threshold
        all_predictions = [predictions[name] for name in model_names if name in predictions]
        if all_predictions:
            avg_all = sum(all_predictions) / len(all_predictions)
            predictions['ensemble_average'] = avg_all
            print(f"Using overall average instead: €{avg_all:.2f}")
    
    return predictions

def predict_batch(model_name, batch_data, models_dir='./backend/models/saved_models/'):
    """
    Args:
        model_name (str): Name of the model to use
        batch_data (list): List of dictionaries, each containing house features
        models_dir (str): Directory containing the trained models
        
    Returns:
        list or None: List of predicted prices for each input in batch_data, or None if model loading fails
    """
    model = load_model(model_name, models_dir)
    feature_names = load_feature_names(model_name, models_dir)
    
    if model is None or feature_names is None:
        return None
    
    predictions = []
    
    for input_data in batch_data:
        prediction = predict_price(model, input_data, feature_names, model_name, models_dir)
        predictions.append(prediction)
    
    return predictions

def main():
    """
    Args:
        None
    
    Returns:
        None: Demonstrates model prediction functionality with a sample input
    """
    models_dir = './backend/models/saved_models/'
    
    print("Available models in the system:")
    list_available_models(models_dir)
    
    sample_input = {
        'Condition': 'New',
        'PropertyType': 'Homes',
        'PropertySubType': 'Apartment',
        'Bedrooms': 3,
        'Bathrooms': 2,
        'AreaNet': 120,
        'AreaGross': 240,
        'Parking': 1,
        'Parish': 'Alvalade'
    }
    
    print("\nPredicting with all available models:")
    predictions = predict_with_all_models(sample_input, models_dir)

if __name__ == "__main__":
    main()