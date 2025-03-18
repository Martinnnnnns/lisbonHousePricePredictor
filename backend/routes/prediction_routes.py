from flask import Blueprint, request, jsonify
import os
import joblib
import numpy as np
import sys

# Create a blueprint for prediction routes
prediction_bp = Blueprint('prediction', __name__)

# Define paths for model and features
MODELS_DIR = os.path.join(os.path.dirname(__file__), './backend/models/saved_models/')
os.makedirs(MODELS_DIR, exist_ok=True)

# Define default model and features path
DEFAULT_MODEL_PATH = os.path.join(MODELS_DIR, 'lhp_random_forest.pkl')
DEFAULT_FEATURES_PATH = os.path.join(MODELS_DIR, 'lhp_random_forest_features.pkl')

# Try to import the model prediction module
try:
    from ..models.model_prediction import load_model, load_feature_names, predict_price
    model_module_imported = True
except ImportError:
    # If there's an import error, define fallback functions
    model_module_imported = False
    
    def load_model(model_path):
        """Fallback function to load model."""
        try:
            return joblib.load(model_path)
        except Exception as e:
            print(f"Error loading model: {e}")
            return None
            
    def load_feature_names(features_path):
        """Fallback function to load feature names."""
        try:
            return joblib.load(features_path)
        except Exception as e:
            print(f"Error loading feature names: {e}")
            # Return fallback feature names
            return ['Bedrooms', 'Bathrooms', 'AreaNet', 'AreaGross', 'Parking', 
                    'Condition', 'PropertyType', 'PropertySubType', 'Parish']
                    
    def predict_price(model, data, feature_names):
        """Fallback function to make predictions."""
        if model is None:
            # Return mock prediction
            return 350000 + (data.get('AreaNet', 80) * 1000) + (data.get('Bedrooms', 2) * 25000)
            
        # Very simple preprocessing
        input_data = np.zeros(len(feature_names))
        
        for i, feature in enumerate(feature_names):
            if feature in data:
                # Handle categorical features
                if feature == 'Condition':
                    condition_mapping = {'For Refurbishment': 1, 'Used': 2, 'As New': 3, 'New': 4}
                    input_data[i] = condition_mapping.get(data[feature], 2)
                elif feature == 'PropertyType':
                    type_mapping = {'Homes': 1, 'Single Habitation': 2}
                    input_data[i] = type_mapping.get(data[feature], 1)
                else:
                    input_data[i] = data[feature]
                    
        # Make prediction
        return model.predict(input_data.reshape(1, -1))[0]

# Find available model
def find_model_file():
    """Find the first available model file in the models directory."""
    try:
        if os.path.exists(DEFAULT_MODEL_PATH):
            return DEFAULT_MODEL_PATH
            
        # Look for any model file
        for filename in os.listdir(MODELS_DIR):
            if filename.startswith('lhp_') and filename.endswith('.pkl') and not filename.endswith('_features.pkl'):
                return os.path.join(MODELS_DIR, filename)
                
        return None
    except Exception:
        return None

def find_features_file(model_path):
    """Find feature file corresponding to the model."""
    try:
        # Try model-specific features first
        model_name = os.path.basename(model_path).replace('lhp_', '').replace('.pkl', '')
        features_path = os.path.join(MODELS_DIR, f'lhp_{model_name}_features.pkl')
        
        if os.path.exists(features_path):
            return features_path
            
        # Try generic feature file
        common_features = os.path.join(MODELS_DIR, 'feature_list.pkl')
        if os.path.exists(common_features):
            return common_features
            
        return None
    except Exception:
        return None

# Try to load model and feature names
try:
    model_path = find_model_file()
    if model_path:
        model = load_model(model_path)
        features_path = find_features_file(model_path)
        feature_names = load_feature_names(features_path)
    else:
        model = None
        feature_names = None
except Exception as e:
    print(f"Error initializing model: {e}")
    model = None
    feature_names = None

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    """Endpoint to predict house price based on input features."""
    global model, feature_names
    
    # Check if model is loaded
    if model is None or feature_names is None:
        # Try to load model one more time
        try:
            model_path = find_model_file()
            if model_path:
                model = load_model(model_path)
                features_path = find_features_file(model_path)
                feature_names = load_feature_names(features_path)
        except Exception:
            pass
            
        # If still not loaded, return mock response
        if model is None or feature_names is None:
            # Get JSON data from request
            data = request.get_json()
            
            if not data:
                return jsonify({
                    'error': 'No input data provided',
                    'status': 'missing_data'
                }), 400
                
            # Return mock prediction
            bedrooms = data.get('Bedrooms', 2)
            area = data.get('AreaNet', 80)
            mock_price = 350000 + (area * 1000) + (bedrooms * 25000)
            
            return jsonify({
                'predicted_price': float(mock_price),
                'currency': 'EUR',
                'status': 'mock_prediction',
                'message': 'Model not available, using mock prediction'
            })
    
    # Get JSON data from request
    data = request.get_json()
    
    if not data:
        return jsonify({
            'error': 'No input data provided',
            'status': 'missing_data'
        }), 400
    
    try:
        # Process the input data and make prediction
        predicted_price = predict_price(model, data, feature_names)
        
        # Return the prediction
        return jsonify({
            'predicted_price': float(predicted_price),
            'currency': 'EUR',
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@prediction_bp.route('/batch-predict', methods=['POST'])
def batch_predict():
    """Endpoint to predict house prices for multiple inputs."""
    global model, feature_names
    
    # Check if model is loaded
    if model is None or feature_names is None:
        # Try to load model one more time
        try:
            model_path = find_model_file()
            if model_path:
                model = load_model(model_path)
                features_path = find_features_file(model_path)
                feature_names = load_feature_names(features_path)
        except Exception:
            pass
    
    # Get JSON data from request
    data = request.get_json()
    
    if not data or not isinstance(data, list):
        return jsonify({
            'error': 'Input must be a list of house data',
            'status': 'invalid_format'
        }), 400
    
    try:
        predictions = []
        
        # If model is not available, generate mock predictions
        if model is None or feature_names is None:
            for i, house_data in enumerate(data):
                bedrooms = house_data.get('Bedrooms', 2)
                area = house_data.get('AreaNet', 80)
                mock_price = 350000 + (area * 1000) + (bedrooms * 25000)
                
                predictions.append({
                    'index': i,
                    'input': house_data,
                    'predicted_price': float(mock_price),
                    'currency': 'EUR',
                    'is_mock': True
                })
                
            return jsonify({
                'predictions': predictions,
                'status': 'mock_prediction',
                'message': 'Model not available, using mock predictions'
            })
        
        # Use actual model for predictions
        for i, house_data in enumerate(data):
            predicted_price = predict_price(model, house_data, feature_names)
            predictions.append({
                'index': i,
                'input': house_data,
                'predicted_price': float(predicted_price),
                'currency': 'EUR'
            })
        
        return jsonify({
            'predictions': predictions,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@prediction_bp.route('/model-info', methods=['GET'])
def model_info():
    """Endpoint to get information about the model."""
    global model, feature_names, model_module_imported
    
    # If model is not loaded, try again
    if model is None:
        try:
            model_path = find_model_file()
            if model_path:
                model = load_model(model_path)
                features_path = find_features_file(model_path)
                feature_names = load_feature_names(features_path)
        except Exception:
            pass
    
    # If still no model, return mock info
    if model is None:
        return jsonify({
            'model_type': 'RandomForestRegressor',
            'parameters': {
                'n_estimators': 100,
                'max_depth': 10,
                'min_samples_split': 2,
                'min_samples_leaf': 1
            },
            'features': feature_names if feature_names else [
                'Bedrooms', 'Bathrooms', 'AreaNet', 'AreaGross', 
                'Parking', 'Condition', 'PropertyType', 'PropertySubType', 'Parish'
            ],
            'feature_count': 9,
            'status': 'mock_info',
            'message': 'Model not available, showing mock information'
        })
    
    try:
        # Get model type and parameters
        model_type = type(model).__name__
        
        # Get parameters (if available)
        if hasattr(model, 'get_params'):
            params = model.get_params()
        else:
            params = {}
        
        # Get feature names
        features = feature_names if feature_names else []
        
        return jsonify({
            'model_type': model_type,
            'parameters': params,
            'features': features,
            'feature_count': len(features),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500