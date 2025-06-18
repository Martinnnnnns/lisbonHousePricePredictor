import pytest
import json
import os
import tempfile
import pandas as pd
from unittest.mock import patch, mock_open
from flask import Flask
import sys
sys.path.append('..')
from routes.data_routes import data_bp

@pytest.fixture
def app():
    """Create a test Flask app."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(data_bp, url_prefix='/api/data')
    return app

@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()

@pytest.fixture
def sample_dataframe():
    """Create a sample dataframe for testing."""
    return pd.DataFrame({
        'Price': [300000, 450000, 600000],
        'AreaNet': [80, 120, 150],
        'Bedrooms': [2, 3, 4],
        'Bathrooms': [1, 2, 2],
        'Parish': ['Alvalade', 'Areeiro', 'Alvalade'],
        'PropertyType': ['Homes', 'Homes', 'Single Habitation'],
        'Condition': ['Used', 'New', 'As New']
    })

class TestModelList:
    """Test the /model-list endpoint."""
    
    @patch('routes.data_routes.os.path.exists')
    @patch('routes.data_routes.os.listdir')
    def test_get_model_list_success(self, mock_listdir, mock_exists, client):
        """Test successful model list retrieval."""
        mock_exists.return_value = True
        mock_listdir.return_value = [
            'lhp_random_forest.pkl',
            'lhp_linear.pkl',
            'lhp_random_forest_features.pkl',  # Should be filtered out
            'other_file.txt'  # Should be filtered out
        ]
        
        response = client.get('/api/data/model-list')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['count'] == 2
        assert 'random_forest' in data['models']
        assert 'linear' in data['models']
        assert 'random_forest_features' not in data['models']
    
    @patch('routes.data_routes.os.path.exists')
    def test_get_model_list_no_directory(self, mock_exists, client):
        """Test when models directory doesn't exist."""
        mock_exists.return_value = False
        
        response = client.get('/api/data/model-list')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'No models directory found'
        assert data['count'] == 0
        assert data['models'] == []
    
    @patch('routes.data_routes.os.path.exists')
    @patch('routes.data_routes.os.listdir')
    def test_get_model_list_no_models(self, mock_listdir, mock_exists, client):
        """Test when no models are found."""
        mock_exists.return_value = True
        mock_listdir.return_value = ['some_other_file.txt']
        
        response = client.get('/api/data/model-list')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['count'] == 0
        assert 'No models found' in data['status']

class TestModelFeatures:
    """Test the /model-features/<model_name> endpoint."""
    
    @patch('routes.data_routes.os.path.exists')
    @patch('routes.data_routes.joblib.load')
    def test_get_model_features_success(self, mock_joblib, mock_exists, client):
        """Test successful feature retrieval."""
        mock_exists.return_value = True
        mock_joblib.return_value = ['Bedrooms', 'Bathrooms', 'AreaNet']
        
        response = client.get('/api/data/model-features/random_forest')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['model'] == 'random_forest'
        assert data['feature_count'] == 3
        assert 'Bedrooms' in data['features']
    
    @patch('routes.data_routes.os.path.exists')
    def test_get_model_features_fallback(self, mock_exists, client):
        """Test fallback features when no feature file exists."""
        mock_exists.return_value = False
        
        response = client.get('/api/data/model-features/random_forest')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'fallback_features'
        assert len(data['features']) > 0
        assert 'Bedrooms' in data['features']

class TestDataSummary:
    """Test the /data-summary endpoint."""
    
    @patch('routes.data_routes.os.path.exists')
    @patch('routes.data_routes.pd.read_csv')
    def test_get_data_summary_success(self, mock_read_csv, mock_exists, client, sample_dataframe):
        """Test successful data summary retrieval."""
        mock_exists.return_value = True
        mock_read_csv.return_value = sample_dataframe
        
        response = client.get('/api/data/data-summary')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['records_count'] == 3
        assert 'numeric_statistics' in data
        assert 'categorical_summary' in data
    
    @patch('routes.data_routes.os.path.exists')
    def test_get_data_summary_no_file(self, mock_exists, client):
        """Test data summary when file doesn't exist."""
        mock_exists.return_value = False
        
        response = client.get('/api/data/data-summary')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'mock_data'
        assert 'Using mock data' in data['message']

class TestParishList:
    """Test the /parish-list endpoint."""
    
    @patch('routes.data_routes.os.path.exists')
    @patch('routes.data_routes.pd.read_csv')
    def test_get_parish_list_success(self, mock_read_csv, mock_exists, client, sample_dataframe):
        """Test successful parish list retrieval."""
        mock_exists.return_value = True
        mock_read_csv.return_value = sample_dataframe
        
        response = client.get('/api/data/parish-list')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['total_count'] == 2  # Alvalade and Areeiro
        assert any(p['name'] == 'Alvalade' for p in data['parishes'])
    
    @patch('routes.data_routes.os.path.exists')
    def test_get_parish_list_no_file(self, mock_exists, client):
        """Test parish list when file doesn't exist."""
        mock_exists.return_value = False
        
        response = client.get('/api/data/parish-list')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'mock_data'
        assert len(data['parishes']) > 0

class TestModelPerformance:
    """Test the /model-performance endpoint."""
    
    @patch('routes.data_routes.os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='{"models": [{"model_name": "test", "rmse": 50000}]}')
    def test_get_model_performance_success(self, mock_file, mock_exists, client):
        """Test successful model performance retrieval."""
        mock_exists.return_value = True
        
        response = client.get('/api/data/model-performance')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert 'models' in data
    
    @patch('routes.data_routes.os.path.exists')
    def test_get_model_performance_mock_data(self, mock_exists, client):
        """Test model performance with mock data."""
        mock_exists.return_value = False
        
        response = client.get('/api/data/model-performance')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'mock_data'
        assert len(data['models']) > 0

class TestErrorHandling:
    """Test error handling across all endpoints."""
    
    @patch('routes.data_routes.os.listdir')
    @patch('routes.data_routes.os.path.exists')
    def test_model_list_exception(self, mock_exists, mock_listdir, client):
        """Test exception handling in model list."""
        mock_exists.return_value = True
        mock_listdir.side_effect = Exception("Test error")
        
        response = client.get('/api/data/model-list')
        data = json.loads(response.data)
        
        assert response.status_code == 500
        assert data['status'] == 'error'
        assert 'error' in data
    
    @patch('routes.data_routes.pd.read_csv')
    @patch('routes.data_routes.os.path.exists')
    def test_data_summary_exception(self, mock_exists, mock_read_csv, client):
        """Test exception handling in data summary."""
        mock_exists.return_value = True
        mock_read_csv.side_effect = Exception("Test error")
        
        response = client.get('/api/data/data-summary')
        data = json.loads(response.data)
        
        assert response.status_code == 500
        assert data['status'] == 'error'