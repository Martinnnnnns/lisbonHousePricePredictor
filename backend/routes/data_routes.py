from flask import Blueprint, jsonify, request
import os
import pandas as pd
import json

# Create a blueprint for data routes
data_bp = Blueprint('data', __name__)

# Define path for data
DATA_DIR = os.path.join(os.path.dirname(__file__), './backend/data/processed/')
MODELS_DIR = os.path.join(os.path.dirname(__file__), './backend/models/saved_models/')
VISUALS_DIR = os.path.join(os.path.dirname(__file__), './backend/models/visuals/')

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(VISUALS_DIR, exist_ok=True)

@data_bp.route('/model-list', methods=['GET'])
def get_model_list():
    """Endpoint to get list of available models."""
    try:
        if not os.path.exists(MODELS_DIR):
            return jsonify({
                'models': [],
                'count': 0,
                'status': 'No models directory found'
            })
            
        # Filter model files (exclude feature files)
        model_files = [
            f.replace('lhp_', '').replace('.pkl', '') 
            for f in os.listdir(MODELS_DIR) 
            if f.startswith('lhp_') and f.endswith('.pkl') and not f.endswith('_features.pkl')
        ]
        
        if not model_files:
            return jsonify({
                'models': [],
                'count': 0,
                'status': 'No models found. You may need to train models first.'
            })
        
        return jsonify({
            'models': model_files,
            'count': len(model_files),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'models': [],
            'count': 0,
            'status': 'error'
        }), 500

@data_bp.route('/model-features/<model_name>', methods=['GET'])
def get_model_features(model_name):
    """Endpoint to get features used by a specific model."""
    try:
        if not os.path.exists(MODELS_DIR):
            return jsonify({
                'error': 'Models directory not found',
                'features': [],
                'feature_count': 0,
                'status': 'no_models_directory'
            }), 404
            
        # First try model-specific features
        features_path = os.path.join(MODELS_DIR, f'lhp_{model_name}_features.pkl')
        
        # If not found, try the common features file
        if not os.path.exists(features_path):
            features_path = os.path.join(MODELS_DIR, 'feature_list.pkl')
            
        if not os.path.exists(features_path):
            # If no feature files exist, return a fallback set of common features
            # This allows frontend development even without models
            fallback_features = [
                'Bedrooms', 'Bathrooms', 'AreaNet', 'AreaGross', 
                'Parking', 'Condition', 'PropertyType', 'PropertySubType', 'Parish'
            ]
            
            return jsonify({
                'model': model_name,
                'features': fallback_features,
                'feature_count': len(fallback_features),
                'status': 'fallback_features'
            })
            
        import joblib
        feature_names = joblib.load(features_path)
        
        return jsonify({
            'model': model_name,
            'features': feature_names,
            'feature_count': len(feature_names),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'features': [],
            'feature_count': 0,
            'status': 'error'
        }), 500

@data_bp.route('/data-summary', methods=['GET'])
def get_data_summary():
    """Endpoint to get summary statistics of the training data."""
    try:
        data_file = os.path.join(DATA_DIR, 'lisbon_houses_processed.csv')
        
        if not os.path.exists(data_file):
            return jsonify({
                'status': 'mock_data',
                'message': 'Using mock data since processed data file not found',
                'records_count': 0,
                'numeric_statistics': {
                    'Price': {'mean': 350000, 'min': 150000, 'max': 900000},
                    'AreaNet': {'mean': 100, 'min': 40, 'max': 300},
                    'Bedrooms': {'mean': 2.5, 'min': 1, 'max': 5}
                },
                'categorical_summary': {
                    'Parish': {'Alvalade': 50, 'Areeiro': 40, 'Avenidas Novas': 45},
                    'PropertyType': {'Homes': 80, 'Single Habitation': 20},
                    'Condition': {'Used': 70, 'New': 20, 'As New': 10}
                },
                'columns': ['Price', 'AreaNet', 'AreaGross', 'Bedrooms', 'Bathrooms', 
                           'Parish', 'PropertyType', 'PropertySubType', 'Condition', 'Parking']
            })
            
        df = pd.read_csv(data_file)
        
        # Generate basic statistics
        numeric_cols = df.select_dtypes(include=['number']).columns
        stats = df[numeric_cols].describe().to_dict()
        
        # Count categorical values for important columns
        categorical_summary = {}
        categorical_cols = ['Parish', 'PropertyType', 'PropertySubType', 'Condition']
        
        for col in categorical_cols:
            if col in df.columns:
                value_counts = df[col].value_counts().to_dict()
                categorical_summary[col] = value_counts
            
        return jsonify({
            'status': 'success',
            'records_count': len(df),
            'numeric_statistics': stats,
            'categorical_summary': categorical_summary,
            'columns': df.columns.tolist()
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error',
            'records_count': 0
        }), 500

@data_bp.route('/parish-list', methods=['GET'])
def get_parish_list():
    """Endpoint to get list of parishes in Lisbon with property counts."""
    try:
        data_file = os.path.join(DATA_DIR, 'lisbon_houses_processed.csv')
        
        if not os.path.exists(data_file):
            # Provide a list of common Lisbon parishes for frontend development
            mock_parishes = [
                {'name': 'Alvalade', 'count': 50},
                {'name': 'Areeiro', 'count': 40},
                {'name': 'Avenidas Novas', 'count': 45},
                {'name': 'Belém', 'count': 30},
                {'name': 'Benfica', 'count': 55},
                {'name': 'Campo de Ourique', 'count': 35},
                {'name': 'Estrela', 'count': 25},
                {'name': 'Lumiar', 'count': 60},
                {'name': 'Marvila', 'count': 20},
                {'name': 'Misericórdia', 'count': 15}
            ]
            
            return jsonify({
                'parishes': mock_parishes,
                'total_count': len(mock_parishes),
                'status': 'mock_data',
                'message': 'Using mock data since processed data file not found'
            })
            
        df = pd.read_csv(data_file)
        
        if 'Parish' not in df.columns:
            return jsonify({
                'error': 'Parish column not found in data',
                'parishes': [],
                'total_count': 0,
                'status': 'missing_column'
            }), 500
            
        # Get parish counts
        parish_counts = df['Parish'].value_counts().to_dict()
        parishes = [{'name': parish, 'count': count} for parish, count in parish_counts.items()]
        
        return jsonify({
            'parishes': parishes,
            'total_count': len(parishes),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'parishes': [],
            'total_count': 0,
            'status': 'error'
        }), 500

@data_bp.route('/model-performance', methods=['GET'])
def get_model_performance():
    """Endpoint to get performance metrics for models."""
    try:
        # Check if performance file exists
        performance_file = os.path.join(MODELS_DIR, 'model_performance.json')
        
        if os.path.exists(performance_file):
            with open(performance_file, 'r') as f:
                performance_data = json.load(f)
                performance_data['status'] = 'success'
                return jsonify(performance_data)
        
        # If the file doesn't exist, check visuals directory
        if os.path.exists(VISUALS_DIR):
            try:
                # Try to gather metrics from visuals directory
                model_names = [
                    f.replace('_predictions.png', '')
                    for f in os.listdir(VISUALS_DIR)
                    if f.endswith('_predictions.png')
                ]
                
                if model_names:
                    # Return minimal info with model names
                    return jsonify({
                        'models': model_names,
                        'note': 'Detailed performance metrics not available. Please run model evaluation to generate them.',
                        'status': 'partial',
                        'metrics_available': False
                    })
            except:
                pass
                
        # Provide mock data for frontend development
        mock_performance = {
            'models': [
                {
                    'model_name': 'random_forest',
                    'rmse': 45000,
                    'mae': 35000,
                    'r2': 0.82,
                    'mape': 12.5
                },
                {
                    'model_name': 'linear_regression',
                    'rmse': 65000,
                    'mae': 49000,
                    'r2': 0.71,
                    'mape': 18.3
                },
                {
                    'model_name': 'gradient_boosting',
                    'rmse': 42000,
                    'mae': 32000,
                    'r2': 0.85,
                    'mape': 10.9
                }
            ],
            'best_model': 'gradient_boosting',
            'status': 'mock_data',
            'message': 'Using mock performance data since no real metrics are available'
        }
        
        return jsonify(mock_performance)
            
    except Exception as e:
        return jsonify({
            'error': str(e),
            'models': [],
            'status': 'error',
            'metrics_available': False
        }), 500