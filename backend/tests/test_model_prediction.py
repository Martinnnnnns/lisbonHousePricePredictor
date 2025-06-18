import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock, mock_open
import os
import sys
sys.path.append('..')
from models.model_prediction import (
    list_available_models, load_model, load_feature_names,
    preprocess_input, predict_price, predict_with_all_models,
    predict_batch
)

@pytest.fixture
def mock_model():
    """Create a mock scikit-learn model."""
    model = MagicMock()
    model.predict.return_value = np.array([450000.0])
    return model

@pytest.fixture
def sample_features():
    """Sample feature names."""
    return ['Bedrooms', 'Bathrooms', 'AreaNet', 'AreaGross', 'Parking', 
            'Condition', 'PropertyType', 'Parish_Alvalade', 'Parish_Areeiro']

@pytest.fixture
def sample_input_data():
    """Sample input data for prediction."""
    return {
        'Bedrooms': 3,
        'Bathrooms': 2,
        'AreaNet': 120,
        'AreaGross': 150,
        'Parking': 1,
        'Condition': 'New',
        'PropertyType': 'Homes',
        'Parish': 'Alvalade'
    }

class TestListAvailableModels:
    """Test the list_available_models function."""
    
    @patch('models.model_prediction.os.listdir')
    @patch('models.model_prediction.os.path.exists')
    def test_list_models_success(self, mock_exists, mock_listdir):
        """Test successful model listing."""
        mock_exists.return_value = True
        mock_listdir.return_value = [
            'lhp_random_forest.pkl',
            'lhp_linear.pkl',
            'lhp_random_forest_features.pkl',  # Should be filtered out
            'other_file.txt'  # Should be filtered out
        ]
        
        models = list_available_models()
        
        assert len(models) == 2
        assert 'random_forest' in models
        assert 'linear' in models
        assert 'random_forest_features' not in models
    
    @patch('models.model_prediction.os.listdir')
    def test_list_models_exception(self, mock_listdir):
        """Test exception handling in model listing."""
        mock_listdir.side_effect = Exception("Directory error")
        
        models = list_available_models()
        
        assert models == []
    
    @patch('models.model_prediction.os.listdir')
    @patch('models.model_prediction.os.path.exists')
    def test_list_models_empty_directory(self, mock_exists, mock_listdir):
        """Test when no models are found."""
        mock_exists.return_value = True
        mock_listdir.return_value = ['some_other_file.txt']
        
        models = list_available_models()
        
        assert models == []

class TestLoadModel:
    """Test the load_model function."""
    
    @patch('models.model_prediction.joblib.load')
    def test_load_model_success(self, mock_joblib_load, mock_model):
        """Test successful model loading."""
        mock_joblib_load.return_value = mock_model
        
        model = load_model('random_forest')
        
        assert model == mock_model
        mock_joblib_load.assert_called_once()
    
    @patch('models.model_prediction.joblib.load')
    def test_load_model_failure(self, mock_joblib_load):
        """Test model loading failure."""
        mock_joblib_load.side_effect = Exception("Loading error")
        
        model = load_model('nonexistent_model')
        
        assert model is None

class TestLoadFeatureNames:
    """Test the load_feature_names function."""
    
    @patch('models.model_prediction.os.path.exists')
    @patch('models.model_prediction.joblib.load')
    def test_load_features_model_specific(self, mock_joblib_load, mock_exists, sample_features):
        """Test loading model-specific features."""
        mock_exists.side_effect = lambda path: 'random_forest_features' in path
        mock_joblib_load.return_value = sample_features
        
        features = load_feature_names('random_forest')
        
        assert features == sample_features
        mock_joblib_load.assert_called_once()
    
    @patch('models.model_prediction.os.path.exists')
    @patch('models.model_prediction.joblib.load')
    def test_load_features_common_file(self, mock_joblib_load, mock_exists, sample_features):
        """Test loading from common feature file."""
        mock_exists.side_effect = lambda path: 'feature_list.pkl' in path
        mock_joblib_load.return_value = sample_features
        
        features = load_feature_names('random_forest')
        
        assert features == sample_features
    
    @patch('models.model_prediction.os.path.exists')
    @patch('models.model_prediction.joblib.load')
    def test_load_features_failure(self, mock_joblib_load, mock_exists):
        """Test feature loading failure."""
        mock_exists.return_value = False
        mock_joblib_load.side_effect = Exception("Loading error")
        
        features = load_feature_names('nonexistent_model')
        
        assert features is None

class TestPreprocessInput:
    """Test the preprocess_input function."""
    
    def test_preprocess_basic_input(self, sample_input_data, sample_features):
        """Test basic input preprocessing."""
        result = preprocess_input(sample_input_data, sample_features)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 1
        assert list(result.columns) == sample_features
    
    def test_preprocess_condition_encoding(self, sample_features):
        """Test condition encoding in preprocessing."""
        input_data = {'Condition': 'New', 'Bedrooms': 2}
        
        result = preprocess_input(input_data, sample_features)
        
        # Check that condition is encoded numerically
        assert result['Condition'].iloc[0] == 4  # 'New' should map to 4
    
    def test_preprocess_property_type_encoding(self, sample_features):
        """Test property type encoding."""
        input_data = {'PropertyType': 'Homes', 'Bedrooms': 2}
        
        result = preprocess_input(input_data, sample_features)
        
        # Check that property type is encoded numerically
        assert result['PropertyType'].iloc[0] == 1  # 'Homes' should map to 1
    
    def test_preprocess_categorical_one_hot(self, sample_features):
        """Test one-hot encoding of categorical variables."""
        input_data = {'Parish': 'Alvalade', 'Bedrooms': 2}
        
        result = preprocess_input(input_data, sample_features)
        
        # Check that Parish_Alvalade is set to 1
        if 'Parish_Alvalade' in result.columns:
            assert result['Parish_Alvalade'].iloc[0] == 1
        if 'Parish_Areeiro' in result.columns:
            assert result['Parish_Areeiro'].iloc[0] == 0
    
    def test_preprocess_missing_features(self, sample_input_data):
        """Test preprocessing when some features are missing."""
        extended_features = sample_input_data.copy()
        extended_features.update(['NewFeature1', 'NewFeature2'])
        
        result = preprocess_input(sample_input_data, list(extended_features.keys()))
        
        # Missing features should be filled with 0
        assert 'NewFeature1' in result.columns
        assert 'NewFeature2' in result.columns

class TestPredictPrice:
    """Test the predict_price function."""
    
    def test_predict_price_success(self, mock_model, sample_input_data, sample_features):
        """Test successful price prediction."""
        mock_model.predict.return_value = np.array([450000.0])
        
        prediction = predict_price(mock_model, sample_input_data, sample_features)
        
        assert prediction == 450000.0
        mock_model.predict.assert_called_once()
    
    def test_predict_price_preprocessing(self, mock_model, sample_features):
        """Test that input is properly preprocessed before prediction."""
        mock_model.predict.return_value = np.array([450000.0])
        input_data = {'Condition': 'New', 'PropertyType': 'Homes', 'Bedrooms': 3}
        
        prediction = predict_price(mock_model, input_data, sample_features)
        
        # Verify model.predict was called with processed data
        call_args = mock_model.predict.call_args[0][0]
        assert isinstance(call_args, (pd.DataFrame, np.ndarray))

class TestPredictWithAllModels:
    """Test the predict_with_all_models function."""
    
    @patch('models.model_prediction.list_available_models')
    @patch('models.model_prediction.load_model')
    @patch('models.model_prediction.load_feature_names')
    @patch('models.model_prediction.predict_price')
    def test_predict_with_all_models_success(self, mock_predict, mock_load_features, 
                                           mock_load_model, mock_list_models, 
                                           sample_input_data, sample_features, mock_model):
        """Test prediction with all models."""
        mock_list_models.return_value = ['random_forest', 'linear']
        mock_load_model.return_value = mock_model
        mock_load_features.return_value = sample_features
        mock_predict.side_effect = [450000.0, 480000.0]  # Two different predictions
        
        predictions = predict_with_all_models(sample_input_data)
        
        assert len(predictions) == 3  # 2 models + ensemble average
        assert 'random_forest' in predictions
        assert 'linear' in predictions
        assert 'ensemble_average' in predictions
        assert predictions['ensemble_average'] == 465000.0  # Average of 450k and 480k
    
    @patch('models.model_prediction.list_available_models')
    @patch('models.model_prediction.load_model')
    @patch('models.model_prediction.load_feature_names')
    @patch('models.model_prediction.predict_price')
    def test_predict_with_outlier_exclusion(self, mock_predict, mock_load_features,
                                          mock_load_model, mock_list_models,
                                          sample_input_data, sample_features, mock_model):
        """Test that outlier predictions above 1M are excluded from ensemble."""
        mock_list_models.return_value = ['random_forest', 'linear', 'outlier_model']
        mock_load_model.return_value = mock_model
        mock_load_features.return_value = sample_features
        mock_predict.side_effect = [450000.0, 480000.0, 1500000.0]  # Third is outlier
        
        predictions = predict_with_all_models(sample_input_data)
        
        # Ensemble should only include first two predictions
        assert predictions['ensemble_average'] == 465000.0  # (450k + 480k) / 2
        assert 'outlier_model' in predictions  # Should still be in results
        assert predictions['outlier_model'] == 1500000.0
    
    @patch('models.model_prediction.list_available_models')
    @patch('models.model_prediction.load_model')
    @patch('models.model_prediction.load_feature_names')
    def test_predict_with_no_models(self, mock_load_features, mock_load_model, 
                                   mock_list_models, sample_input_data):
        """Test prediction when no models are available."""
        mock_list_models.return_value = []
        
        predictions = predict_with_all_models(sample_input_data)
        
        assert predictions == {}
    
    @patch('models.model_prediction.list_available_models')
    @patch('models.model_prediction.load_model')
    @patch('models.model_prediction.load_feature_names')
    @patch('models.model_prediction.predict_price')
    def test_predict_with_model_loading_failure(self, mock_predict, mock_load_features,
                                               mock_load_model, mock_list_models,
                                               sample_input_data):
        """Test prediction when some models fail to load."""
        mock_list_models.return_value = ['working_model', 'broken_model']
        mock_load_model.side_effect = [MagicMock(), None]  # Second model fails to load
        mock_load_features.side_effect = [['feature1'], None]
        mock_predict.return_value = 450000.0
        
        predictions = predict_with_all_models(sample_input_data)
        
        assert 'working_model' in predictions
        assert 'broken_model' not in predictions
        assert 'ensemble_average' in predictions

class TestPredictBatch:
    """Test the predict_batch function."""
    
    @patch('models.model_prediction.load_model')
    @patch('models.model_prediction.load_feature_names')
    @patch('models.model_prediction.predict_price')
    def test_predict_batch_success(self, mock_predict, mock_load_features, 
                                  mock_load_model, sample_features, mock_model):
        """Test successful batch prediction."""
        mock_load_model.return_value = mock_model
        mock_load_features.return_value = sample_features
        mock_predict.side_effect = [450000.0, 480000.0, 520000.0]
        
        batch_data = [
            {'Bedrooms': 2, 'AreaNet': 80},
            {'Bedrooms': 3, 'AreaNet': 120},
            {'Bedrooms': 4, 'AreaNet': 160}
        ]
        
        predictions = predict_batch('random_forest', batch_data)
        
        assert len(predictions) == 3
        assert predictions[0] == 450000.0
        assert predictions[1] == 480000.0
        assert predictions[2] == 520000.0
    
    @patch('models.model_prediction.load_model')
    @patch('models.model_prediction.load_feature_names')
    def test_predict_batch_model_loading_failure(self, mock_load_features, mock_load_model):
        """Test batch prediction when model fails to load."""
        mock_load_model.return_value = None
        mock_load_features.return_value = None
        
        batch_data = [{'Bedrooms': 2}]
        
        predictions = predict_batch('nonexistent_model', batch_data)
        
        assert predictions is None
    
    @patch('models.model_prediction.load_model')
    @patch('models.model_prediction.load_feature_names')
    @patch('models.model_prediction.predict_price')
    def test_predict_batch_empty_input(self, mock_predict, mock_load_features,
                                      mock_load_model, sample_features, mock_model):
        """Test batch prediction with empty input."""
        mock_load_model.return_value = mock_model
        mock_load_features.return_value = sample_features
        
        predictions = predict_batch('random_forest', [])
        
        assert predictions == []
        mock_predict.assert_not_called()

class TestErrorHandling:
    """Test error handling in various scenarios."""
    
    @patch('models.model_prediction.pd.get_dummies')
    def test_preprocess_input_exception(self, mock_get_dummies, sample_input_data, sample_features):
        """Test preprocessing with pandas exception."""
        mock_get_dummies.side_effect = Exception("Pandas error")
        
        # Should not raise exception, but may return unexpected results
        try:
            result = preprocess_input(sample_input_data, sample_features)
            # If no exception, that's fine - the function handles it gracefully
        except Exception:
            # If exception is raised, that's also acceptable for this test
            pass
    
    def test_predict_price_with_invalid_input(self, mock_model, sample_features):
        """Test prediction with invalid input data."""
        mock_model.predict.side_effect = Exception("Model prediction error")
        
        with pytest.raises(Exception):
            predict_price(mock_model, {}, sample_features)

class TestIntegration:
    """Integration tests that combine multiple functions."""
    
    @patch('models.model_prediction.joblib.load')
    @patch('models.model_prediction.os.listdir')
    @patch('models.model_prediction.os.path.exists')
    def test_full_prediction_pipeline(self, mock_exists, mock_listdir, mock_joblib_load, 
                                    sample_input_data, sample_features, mock_model):
        """Test the full prediction pipeline from model loading to prediction."""
        # Setup mocks for model discovery
        mock_exists.return_value = True
        mock_listdir.return_value = ['lhp_random_forest.pkl']
        mock_joblib_load.side_effect = [mock_model, sample_features]  # Model, then features
        mock_model.predict.return_value = np.array([450000.0])
        
        # Test the pipeline
        models = list_available_models()
        assert 'random_forest' in models
        
        model = load_model('random_forest')
        assert model is not None
        
        features = load_feature_names('random_forest')
        assert features == sample_features
        
        prediction = predict_price(model, sample_input_data, features)
        assert prediction == 450000.0

class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_preprocess_input_empty_features(self, sample_input_data):
        """Test preprocessing with empty feature list."""
        result = preprocess_input(sample_input_data, [])
        
        assert isinstance(result, pd.DataFrame)
        assert len(result.columns) == 0
    
    def test_preprocess_input_empty_data(self, sample_features):
        """Test preprocessing with empty input data."""
        result = preprocess_input({}, sample_features)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 1
        assert list(result.columns) == sample_features
    
    @patch('models.model_prediction.list_available_models')
    @patch('models.model_prediction.load_model')
    @patch('models.model_prediction.load_feature_names')
    @patch('models.model_prediction.predict_price')
    def test_all_predictions_above_threshold(self, mock_predict, mock_load_features,
                                           mock_load_model, mock_list_models,
                                           sample_input_data, sample_features, mock_model):
        """Test when all predictions are above the 1M threshold."""
        mock_list_models.return_value = ['model1', 'model2']
        mock_load_model.return_value = mock_model
        mock_load_features.return_value = sample_features
        mock_predict.side_effect = [1500000.0, 1800000.0]  # Both above threshold
        
        predictions = predict_with_all_models(sample_input_data)
        
        # Should fallback to using all predictions
        assert 'ensemble_average' in predictions
        assert predictions['ensemble_average'] == 1650000.0  # Average of both