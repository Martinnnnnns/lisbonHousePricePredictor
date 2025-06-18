import pytest
import json
import os
from unittest.mock import patch, MagicMock
from flask import Flask
import sys
sys.path.append('..')
from routes.prediction_routes import prediction_bp

@pytest.fixture
def app():
    """Create a test Flask app."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(prediction_bp, url_prefix='/api/predictions')
    return app

@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()

@pytest.fixture
def sample_house_data():
    """Sample house data for predictions."""
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
def mock_model():
    """Create a mock model."""
    model = MagicMock()
    model.predict.return_value = [450000.0]
    return model

@pytest.fixture
def sample_features():
    """Sample feature names."""
    return ['Bedrooms', 'Bathrooms', 'AreaNet', 'AreaGross', 'Parking']

class TestPredictEndpoint:
    """Test the /predict endpoint."""
    
    @patch('routes.prediction_routes.model', new=None)
    @patch('routes.prediction_routes.feature_names', new=None)
    @patch('routes.prediction_routes.find_model_file')
    def test_predict_mock_response(self, mock_find_model, client, sample_house_data):
        """Test prediction with mock response when no model is available."""
        mock_find_model.return_value = None
        
        response = client.post('/api/predictions/predict', 
                             data=json.dumps(sample_house_data),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'mock_prediction'
        assert 'predicted_price' in data
        assert data['currency'] == 'EUR'
        assert isinstance(data['predicted_price'], float)
    
    def test_predict_no_data(self, client):
        """Test prediction endpoint with no input data."""
        response = client.post('/api/predictions/predict',
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert data['status'] == 'missing_data'
        assert 'error' in data
    
    @patch('routes.prediction_routes.model')
    @patch('routes.prediction_routes.feature_names')
    @patch('routes.prediction_routes.predict_price')
    def test_predict_with_model(self, mock_predict, mock_features, mock_model, 
                               client, sample_house_data, sample_features):
        """Test prediction with actual model."""
        mock_features.__bool__ = lambda self: True
        mock_model.__bool__ = lambda self: True
        mock_predict.return_value = 450000.0
        
        response = client.post('/api/predictions/predict',
                             data=json.dumps(sample_house_data),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['predicted_price'] == 450000.0
        assert data['currency'] == 'EUR'
        mock_predict.assert_called_once()
    
    @patch('routes.prediction_routes.model')
    @patch('routes.prediction_routes.feature_names') 
    @patch('routes.prediction_routes.predict_price')
    def test_predict_exception(self, mock_predict, mock_features, mock_model,
                              client, sample_house_data):
        """Test prediction endpoint exception handling."""
        mock_features.__bool__ = lambda self: True
        mock_model.__bool__ = lambda self: True
        mock_predict.side_effect = Exception("Prediction error")
        
        response = client.post('/api/predictions/predict',
                             data=json.dumps(sample_house_data),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 500
        assert data['status'] == 'error'
        assert 'error' in data

class TestBatchPredictEndpoint:
    """Test the /batch-predict endpoint."""
    
    @patch('routes.prediction_routes.model', new=None)
    @patch('routes.prediction_routes.feature_names', new=None)
    def test_batch_predict_mock_response(self, client, sample_house_data):
        """Test batch prediction with mock response."""
        batch_data = [sample_house_data, sample_house_data]
        
        response = client.post('/api/predictions/batch-predict',
                             data=json.dumps(batch_data),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'mock_prediction'
        assert len(data['predictions']) == 2
        assert all('predicted_price' in pred for pred in data['predictions'])
        assert all(pred['is_mock'] for pred in data['predictions'])
    
    def test_batch_predict_invalid_format(self, client):
        """Test batch prediction with invalid input format."""
        response = client.post('/api/predictions/batch-predict',
                             data=json.dumps({'not': 'a list'}),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert data['status'] == 'invalid_format'
    
    def test_batch_predict_no_data(self, client):
        """Test batch prediction with no data."""
        response = client.post('/api/predictions/batch-predict',
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert data['status'] == 'invalid_format'
    
    @patch('routes.prediction_routes.model')
    @patch('routes.prediction_routes.feature_names')
    @patch('routes.prediction_routes.predict_price')
    def test_batch_predict_with_model(self, mock_predict, mock_features, mock_model,
                                    client, sample_house_data):
        """Test batch prediction with actual model."""
        mock_features.__bool__ = lambda self: True
        mock_model.__bool__ = lambda self: True
        mock_predict.side_effect = [450000.0, 520000.0]
        
        batch_data = [sample_house_data, sample_house_data]
        
        response = client.post('/api/predictions/batch-predict',
                             data=json.dumps(batch_data),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert len(data['predictions']) == 2
        assert data['predictions'][0]['predicted_price'] == 450000.0
        assert data['predictions'][1]['predicted_price'] == 520000.0

class TestModelInfoEndpoint:
    """Test the /model-info endpoint."""
    
    @patch('routes.prediction_routes.model', new=None)
    @patch('routes.prediction_routes.feature_names', new=None)
    def test_model_info_no_model(self, client):
        """Test model info when no model is available."""
        response = client.get('/api/predictions/model-info')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'mock_info'
        assert data['model_type'] == 'RandomForestRegressor'
        assert 'parameters' in data
        assert 'features' in data
        assert data['feature_count'] == 9
    
    @patch('routes.prediction_routes.model')
    @patch('routes.prediction_routes.feature_names')
    def test_model_info_with_model(self, mock_features, mock_model, client, sample_features):
        """Test model info with actual model."""
        # Setup mock model
        mock_model.__bool__ = lambda self: True
        mock_model.__class__.__name__ = 'RandomForestRegressor'
        mock_model.get_params.return_value = {'n_estimators': 100, 'max_depth': 10}
        
        # Setup mock features
        mock_features.__bool__ = lambda self: True
        mock_features.__iter__ = lambda self: iter(sample_features)
        mock_features.__len__ = lambda self: len(sample_features)
        
        response = client.get('/api/predictions/model-info')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['model_type'] == 'RandomForestRegressor'
        assert data['feature_count'] == len(sample_features)
        assert 'n_estimators' in data['parameters']

class TestUtilityFunctions:
    """Test utility functions in prediction routes."""
    
    @patch('routes.prediction_routes.os.path.exists')
    @patch('routes.prediction_routes.os.listdir')
    def test_find_model_file_success(self, mock_listdir, mock_exists):
        """Test finding model file successfully."""
        from routes.prediction_routes import find_model_file
        
        mock_exists.side_effect = lambda path: 'random_forest' in path
        mock_listdir.return_value = ['lhp_random_forest.pkl', 'other_file.txt']
        
        result = find_model_file()
        assert result is not None
        assert 'random_forest' in result
    
    @patch('routes.prediction_routes.os.path.exists')
    def test_find_model_file_not_found(self, mock_exists):
        """Test when no model file is found."""
        from routes.prediction_routes import find_model_file
        
        mock_exists.return_value = False
        
        result = find_model_file()
        assert result is None
    
    @patch('routes.prediction_routes.os.path.exists')
    @patch('routes.prediction_routes.os.path.basename')
    def test_find_features_file(self, mock_basename, mock_exists):
        """Test finding features file."""
        from routes.prediction_routes import find_features_file
        
        mock_basename.return_value = 'lhp_random_forest.pkl'
        mock_exists.side_effect = lambda path: 'random_forest_features' in path
        
        result = find_features_file('/path/to/lhp_random_forest.pkl')
        assert result is not None
        assert 'features' in result

class TestErrorScenarios:
    """Test various error scenarios."""
    
    def test_predict_malformed_json(self, client):
        """Test prediction with malformed JSON."""
        response = client.post('/api/predictions/predict',
                             data='{"invalid": json',
                             content_type='application/json')
        
        # Flask should return 400 for malformed JSON
        assert response.status_code == 400
    
    @patch('routes.prediction_routes.model')
    @patch('routes.prediction_routes.feature_names')
    @patch('routes.prediction_routes.predict_price')
    def test_batch_predict_partial_failure(self, mock_predict, mock_features, mock_model,
                                         client, sample_house_data):
        """Test batch prediction with some predictions failing."""
        mock_features.__bool__ = lambda self: True
        mock_model.__bool__ = lambda self: True
        mock_predict.side_effect = [450000.0, Exception("Error"), 520000.0]
        
        batch_data = [sample_house_data, sample_house_data, sample_house_data]
        
        response = client.post('/api/predictions/batch-predict',
                             data=json.dumps(batch_data),
                             content_type='application/json')
        data = json.loads(response.data)
        
        # Should return error status due to exception
        assert response.status_code == 500
        assert data['status'] == 'error'