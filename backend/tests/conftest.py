# backend/tests/conftest.py
"""
Pytest configuration file for shared fixtures and test setup.
This file is automatically discovered by pytest and provides common fixtures
that can be used across all test files.
"""

import pytest
import pandas as pd
import numpy as np
import tempfile
import os
import sys
from unittest.mock import MagicMock, patch
from flask import Flask

# Add the backend directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture(scope="session")
def app():
    """Create a Flask app for testing."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret-key'
    
    # Register blueprints
    try:
        from routes.data_routes import data_bp
        from routes.prediction_routes import prediction_bp
        app.register_blueprint(data_bp, url_prefix='/api/data')
        app.register_blueprint(prediction_bp, url_prefix='/api/predictions')
    except ImportError:
        # If routes can't be imported, create a basic app
        pass
    
    return app

@pytest.fixture
def client(app):
    """Create a test client for the Flask app."""
    return app.test_client()

@pytest.fixture
def sample_house_data():
    """Standard house data for testing predictions."""
    return {
        'Bedrooms': 3,
        'Bathrooms': 2,
        'AreaNet': 120,
        'AreaGross': 150,
        'Parking': 1,
        'Condition': 'New',
        'PropertyType': 'Homes',
        'PropertySubType': 'Apartment',
        'Parish': 'Alvalade'
    }

@pytest.fixture
def sample_dataframe():
    """Standard dataframe for testing data operations."""
    np.random.seed(42)  # For reproducible tests
    return pd.DataFrame({
        'Price': [300000, 450000, 600000, 250000, 380000],
        'AreaNet': [80.5, 120.7, 150.3, 70.1, 95.2],
        'AreaGross': [100.2, 140.8, 180.5, 90.3, 115.7],
        'Bedrooms': [2, 3, 4, 1, 2],
        'Bathrooms': [1, 2, 2, 1, 1],
        'Parking': [1, 1, 2, 0, 1],
        'Parish': ['Alvalade', 'Areeiro', 'Alvalade', 'Benfica', 'Lumiar'],
        'PropertyType': ['Homes', 'Homes', 'Single Habitation', 'Homes', 'Homes'],
        'PropertySubType': ['Apartment', 'Apartment', 'House', 'Studio', 'Apartment'],
        'Condition': ['Used', 'New', 'As New', 'Used', 'New']
    })

@pytest.fixture
def sample_dataframe_with_issues():
    """Dataframe with common data quality issues for testing cleaning functions."""
    return pd.DataFrame({
        'Id': [1, 2, 3, 4, 5, 5],  # Duplicate row
        'Price': [300000, 450000, 600000, 2000000, 250000, 250000],  # Outlier
        'AreaNet': [80, 120, np.nan, 200, 70, 70],  # Missing values
        'AreaGross': [100, 140, 180, 250, np.nan, np.nan],
        'Bedrooms': [2, 3, 4, 5, 1, 1],
        'Parish': ['Alvalade', 'Areeiro', None, 'Benfica', 'Lumiar', 'Lumiar'],
        'PropertyType': ['Homes', 'Homes', 'Single Habitation', None, 'Homes', 'Homes'],
        'ConstantColumn': [1, 1, 1, 1, 1, 1],  # Single value column
        'Price M2': [3000, 3200, 3400, 8000, 3571, 3571]  # For correlation testing
    })

@pytest.fixture
def mock_trained_model():
    """Mock trained scikit-learn model."""
    model = MagicMock()
    model.predict.return_value = np.array([450000.0])
    model.get_params.return_value = {
        'n_estimators': 100,
        'max_depth': 10,
        'min_samples_split': 2
    }
    model.__class__.__name__ = 'RandomForestRegressor'
    return model

@pytest.fixture
def sample_feature_names():
    """Standard feature names for testing."""
    return [
        'Bedrooms', 'Bathrooms', 'AreaNet', 'AreaGross', 'Parking',
        'Condition', 'PropertyType', 'Parish_Alvalade', 'Parish_Areeiro',
        'Parish_Benfica', 'PropertySubType_Apartment', 'PropertySubType_House'
    ]

@pytest.fixture
def temp_csv_file(sample_dataframe):
    """Create a temporary CSV file with sample data."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        sample_dataframe.to_csv(f.name, index=False)
        yield f.name
    
    # Cleanup
    if os.path.exists(f.name):
        os.unlink(f.name)

@pytest.fixture
def temp_directory():
    """Create a temporary directory for testing file operations."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir

@pytest.fixture
def mock_models_directory(temp_directory):
    """Create a mock models directory with sample model files."""
    models_dir = os.path.join(temp_directory, 'models')
    os.makedirs(models_dir, exist_ok=True)
    
    # Create mock model files
    model_files = [
        'lhp_random_forest.pkl',
        'lhp_linear.pkl',
        'lhp_decision_tree.pkl',
        'lhp_random_forest_features.pkl',
        'feature_list.pkl'
    ]
    
    for filename in model_files:
        filepath = os.path.join(models_dir, filename)
        with open(filepath, 'w') as f:
            f.write('mock model data')
    
    return models_dir

@pytest.fixture(scope="function", autouse=True)
def reset_mocks():
    """Reset all mocks after each test to prevent test interference."""
    yield
    # This runs after each test
    patch.stopall()

@pytest.fixture
def mock_performance_data():
    """Mock model performance data for testing."""
    return {
        'models': [
            {
                'model_name': 'random_forest',
                'rmse': 45000,
                'mae': 35000,
                'r2': 0.82,
                'mape': 12.5
            },
            {
                'model_name': 'linear',
                'rmse': 65000,
                'mae': 49000,
                'r2': 0.71,
                'mape': 18.3
            },
            {
                'model_name': 'decision_tree',
                'rmse': 55000,
                'mae': 42000,
                'r2': 0.75,
                'mape': 15.8
            }
        ],
        'best_model': 'random_forest',
        'status': 'success'
    }

@pytest.fixture
def batch_prediction_data():
    """Sample batch data for testing batch predictions."""
    return [
        {
            'Bedrooms': 2,
            'Bathrooms': 1,
            'AreaNet': 80,
            'AreaGross': 100,
            'Parking': 1,
            'Condition': 'Used',
            'PropertyType': 'Homes',
            'Parish': 'Alvalade'
        },
        {
            'Bedrooms': 3,
            'Bathrooms': 2,
            'AreaNet': 120,
            'AreaGross': 150,
            'Parking': 1,
            'Condition': 'New',
            'PropertyType': 'Homes',
            'Parish': 'Areeiro'
        },
        {
            'Bedrooms': 4,
            'Bathrooms': 2,
            'AreaNet': 160,
            'AreaGross': 200,
            'Parking': 2,
            'Condition': 'As New',
            'PropertyType': 'Single Habitation',
            'Parish': 'Benfica'
        }
    ]

# Test markers for categorizing tests
def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line("markers", "unit: mark test as a unit test")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "api: mark test as an API test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "mock: mark test as using mocks")

# Pytest hooks for custom behavior
def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers automatically."""
    for item in items:
        # Add markers based on test file names
        if "test_data_routes" in item.nodeid or "test_prediction_routes" in item.nodeid:
            item.add_marker(pytest.mark.api)
        
        if "mock" in item.name.lower() or "Mock" in item.nodeid:
            item.add_marker(pytest.mark.mock)
        
        # Mark tests that might be slow
        if any(keyword in item.name.lower() for keyword in ['batch', 'large', 'performance']):
            item.add_marker(pytest.mark.slow)

@pytest.fixture
def capture_logs():
    """Capture logs during testing for verification."""
    import logging
    from io import StringIO
    
    log_capture_string = StringIO()
    ch = logging.StreamHandler(log_capture_string)
    ch.setLevel(logging.DEBUG)
    
    # Get the root logger
    logger = logging.getLogger()
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)
    
    yield log_capture_string
    
    # Clean up
    logger.removeHandler(ch)

# Mock external dependencies that might not be available in test environment
@pytest.fixture(autouse=True)
def mock_external_dependencies():
    """Mock external dependencies that might not be available during testing."""
    with patch('joblib.load') as mock_joblib, \
         patch('joblib.dump') as mock_joblib_dump:
        
        # Configure default behaviors
        mock_joblib.return_value = MagicMock()
        mock_joblib_dump.return_value = None
        
        yield {
            'joblib_load': mock_joblib,
            'joblib_dump': mock_joblib_dump
        }