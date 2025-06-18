import pytest
import pandas as pd
import numpy as np
import os
import tempfile
from unittest.mock import patch, mock_open, MagicMock
import sys
sys.path.append('..')
from utils.data_utils import (
    load_data, save_processed_data, check_missing_values,
    explore_numeric_features, preprocess_input
)

@pytest.fixture
def sample_dataframe():
    """Create a sample dataframe for testing."""
    return pd.DataFrame({
        'Price': [300000, 450000, 600000, 250000],
        'AreaNet': [80.5, 120.7, 150.3, 70.1],
        'AreaGross': [100.2, 140.8, 180.5, 90.3],
        'Bedrooms': [2, 3, 4, 1],
        'Bathrooms': [1, 2, 2, 1],
        'Parking': [1, 1, 2, 0],
        'Parish': ['Alvalade', 'Areeiro', 'Alvalade', 'Benfica'],
        'PropertyType': ['Homes', 'Homes', 'Single Habitation', 'Homes'],
        'Condition': ['Used', 'New', 'As New', 'Used']
    })

@pytest.fixture
def sample_dataframe_with_missing():
    """Create a sample dataframe with missing values."""
    return pd.DataFrame({
        'Price': [300000, 450000, np.nan, 250000],
        'AreaNet': [80.5, np.nan, 150.3, 70.1],
        'Bedrooms': [2, 3, 4, np.nan],
        'Parish': ['Alvalade', None, 'Alvalade', 'Benfica'],
        'PropertyType': ['Homes', 'Homes', None, 'Homes']
    })

class TestLoadData:
    """Test the load_data function."""
    
    @patch('utils.data_utils.pd.read_csv')
    def test_load_data_success(self, mock_read_csv, sample_dataframe):
        """Test successful data loading."""
        mock_read_csv.return_value = sample_dataframe
        
        result = load_data('test_file.csv')
        
        assert result is not None
        assert len(result) == 4
        assert 'Price' in result.columns
        mock_read_csv.assert_called_once_with('test_file.csv')
    
    @patch('utils.data_utils.pd.read_csv')
    def test_load_data_file_not_found(self, mock_read_csv):
        """Test loading data when file doesn't exist."""
        mock_read_csv.side_effect = FileNotFoundError("File not found")
        
        result = load_data('nonexistent_file.csv')
        
        assert result is None
    
    @patch('utils.data_utils.pd.read_csv')
    def test_load_data_general_exception(self, mock_read_csv):
        """Test loading data with general exception."""
        mock_read_csv.side_effect = Exception("General error")
        
        result = load_data('problem_file.csv')
        
        assert result is None
    
    def test_load_data_default_filepath(self):
        """Test load_data with default filepath."""
        # This will likely fail since the default file doesn't exist,
        # but we're testing that the function can be called with no arguments
        result = load_data()
        
        # Should return None if file doesn't exist
        assert result is None

class TestSaveProcessedData:
    """Test the save_processed_data function."""
    
    def test_save_processed_data_success(self, sample_dataframe):
        """Test successful data saving."""
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
            temp_path = tmp.name
        
        try:
            result = save_processed_data(sample_dataframe, temp_path)
            
            assert result is True
            assert os.path.exists(temp_path)
            
            # Verify the saved data
            loaded_data = pd.read_csv(temp_path)
            assert len(loaded_data) == len(sample_dataframe)
            assert list(loaded_data.columns) == list(sample_dataframe.columns)
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_save_processed_data_decimal_rounding(self, sample_dataframe):
        """Test that decimal places are properly rounded."""
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
            temp_path = tmp.name
        
        try:
            result = save_processed_data(sample_dataframe, temp_path, decimal_places=2)
            
            assert result is True
            
            # Check that float values are rounded to 2 decimal places
            loaded_data = pd.read_csv(temp_path)
            float_col = loaded_data['AreaNet'].iloc[0]
            
            # Check that we don't have more than 2 decimal places
            decimal_part = str(float_col).split('.')[-1] if '.' in str(float_col) else ''
            assert len(decimal_part) <= 2
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_save_processed_data_default_path(self, sample_dataframe):
        """Test saving with default path (will create directories)."""
        # This tests the directory creation functionality
        result = save_processed_data(sample_dataframe)
        
        # Even if it fails due to path issues, it should return a boolean
        assert isinstance(result, bool)
    
    @patch('utils.data_utils.os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_save_processed_data_exception(self, mock_to_csv, mock_makedirs, sample_dataframe):
        """Test saving with exception."""
        mock_to_csv.side_effect = Exception("Save error")
        
        result = save_processed_data(sample_dataframe, 'test_path.csv')
        
        assert result is False

class TestCheckMissingValues:
    """Test the check_missing_values function."""
    
    def test_check_missing_values_no_missing(self, sample_dataframe):
        """Test checking missing values when there are none."""
        result = check_missing_values(sample_dataframe)
        
        # Should return a Series with all zeros
        assert isinstance(result, pd.Series)
        assert result.sum() == 0
    
    def test_check_missing_values_with_missing(self, sample_dataframe_with_missing):
        """Test checking missing values when there are some."""
        result = check_missing_values(sample_dataframe_with_missing)
        
        # Should return a Series with missing counts
        assert isinstance(result, pd.Series)
        assert result.sum() > 0
        
        # Should only include columns with missing values
        missing_columns = result[result > 0]
        assert 'Price' in missing_columns.index
        assert 'AreaNet' in missing_columns.index
    
    def test_check_missing_values_empty_dataframe(self):
        """Test checking missing values with empty dataframe."""
        empty_df = pd.DataFrame()
        
        result = check_missing_values(empty_df)
        
        assert isinstance(result, pd.Series)
        assert len(result) == 0

class TestExploreNumericFeatures:
    """Test the explore_numeric_features function."""
    
    def test_explore_numeric_features_basic(self, sample_dataframe):
        """Test basic numeric feature exploration."""
        result = explore_numeric_features(sample_dataframe)
        
        assert isinstance(result, pd.DataFrame)
        
        # Should include all numeric columns
        numeric_cols = sample_dataframe.select_dtypes(include=['int64', 'float64']).columns
        for col in numeric_cols:
            assert col in result.index
        
        # Should have standard statistics columns
        expected_stats = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
        for stat in expected_stats:
            assert stat in result.columns
    
    def test_explore_numeric_features_with_target(self, sample_dataframe):
        """Test numeric feature exploration with target correlation."""
        result = explore_numeric_features(sample_dataframe, target_column='Price')
        
        assert isinstance(result, pd.DataFrame)
        assert 'corr_with_target' in result.columns
        
        # Price should have correlation of 1.0 with itself
        assert result.loc['Price', 'corr_with_target'] == 1.0
    
    def test_explore_numeric_features_missing_info(self, sample_dataframe_with_missing):
        """Test that missing value information is included."""
        result = explore_numeric_features(sample_dataframe_with_missing)
        
        assert 'missing' in result.columns
        assert 'missing_pct' in result.columns
        
        # Should show missing values for columns that have them
        if 'Price' in result.index:
            assert result.loc['Price', 'missing'] > 0
    
    def test_explore_numeric_features_no_numeric_columns(self):
        """Test with dataframe that has no numeric columns."""
        text_df = pd.DataFrame({
            'A': ['text1', 'text2', 'text3'],
            'B': ['cat1', 'cat2', 'cat3']
        })
        
        result = explore_numeric_features(text_df)
        
        # Should return empty dataframe or handle gracefully
        assert isinstance(result, pd.DataFrame)
    
    def test_explore_numeric_features_nonexistent_target(self, sample_dataframe):
        """Test with nonexistent target column."""
        result = explore_numeric_features(sample_dataframe, target_column='NonExistentColumn')
        
        # Should not crash and should not have correlation column
        assert isinstance(result, pd.DataFrame)
        assert 'corr_with_target' not in result.columns

class TestPreprocessInput:
    """Test the preprocess_input function."""
    
    def test_preprocess_input_basic(self):
        """Test basic input preprocessing."""
        input_data = {
            'Bedrooms': 3,
            'Bathrooms': 2,
            'AreaNet': 120,
            'Condition': 'New',
            'PropertyType': 'Homes',
            'Parish': 'Alvalade'
        }
        feature_names = ['Bedrooms', 'Bathrooms', 'AreaNet', 'Condition', 'PropertyType', 'Parish_Alvalade']
        
        result = preprocess_input(input_data, feature_names)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 1
        assert list(result.columns) == feature_names
    
    def test_preprocess_input_condition_encoding(self):
        """Test condition encoding in input preprocessing."""
        input_data = {'Condition': 'New'}
        feature_names = ['Condition']
        
        result = preprocess_input(input_data, feature_names)
        
        # 'New' should be encoded as 4
        assert result['Condition'].iloc[0] == 4
    
    def test_preprocess_input_property_type_encoding(self):
        """Test property type encoding in input preprocessing."""
        input_data = {'PropertyType': 'Homes'}
        feature_names = ['PropertyType']
        
        result = preprocess_input(input_data, feature_names)
        
        # 'Homes' should be encoded as 1
        assert result['PropertyType'].iloc[0] == 1
    
    def test_preprocess_input_one_hot_encoding(self):
        """Test one-hot encoding of categorical variables."""
        input_data = {'Parish': 'Alvalade'}
        feature_names = ['Parish_Alvalade', 'Parish_Areeiro', 'Parish_Benfica']
        
        result = preprocess_input(input_data, feature_names)
        
        # Only Parish_Alvalade should be 1, others should be 0
        assert result['Parish_Alvalade'].iloc[0] == 1
        assert result['Parish_Areeiro'].iloc[0] == 0
        assert result['Parish_Benfica'].iloc[0] == 0
    
    def test_preprocess_input_missing_features(self):
        """Test preprocessing when expected features are missing from input."""
        input_data = {'Bedrooms': 3}
        feature_names = ['Bedrooms', 'Bathrooms', 'AreaNet', 'MissingFeature']
        
        result = preprocess_input(input_data, feature_names)
        
        # Missing features should be filled with 0
        assert result['MissingFeature'].iloc[0] == 0
        assert result['Bedrooms'].iloc[0] == 3
    
    def test_preprocess_input_extra_input_features(self):
        """Test preprocessing when input has extra features not in feature_names."""
        input_data = {
            'Bedrooms': 3,
            'ExtraFeature': 'extra_value',
            'AnotherExtra': 123
        }
        feature_names = ['Bedrooms', 'Bathrooms']
        
        result = preprocess_input(input_data, feature_names)
        
        # Result should only have features from feature_names
        assert list(result.columns) == feature_names
        assert result['Bedrooms'].iloc[0] == 3
        assert result['Bathrooms'].iloc[0] == 0  # Missing, so filled with 0
    
    def test_preprocess_input_empty_input(self):
        """Test preprocessing with empty input data."""
        input_data = {}
        feature_names = ['Bedrooms', 'Bathrooms', 'AreaNet']
        
        result = preprocess_input(input_data, feature_names)
        
        # All features should be filled with 0
        assert all(result.iloc[0] == 0)
    
    def test_preprocess_input_empty_features(self):
        """Test preprocessing with empty feature names."""
        input_data = {'Bedrooms': 3, 'Bathrooms': 2}
        feature_names = []
        
        result = preprocess_input(input_data, feature_names)
        
        # Should return dataframe with no columns
        assert len(result.columns) == 0
        assert len(result) == 1

class TestConditionPropertyTypeMapping:
    """Test specific encoding mappings."""
    
    def test_all_condition_values(self):
        """Test all possible condition values are encoded correctly."""
        condition_mapping = {
            'For Refurbishment': 1,
            'Used': 2,
            'As New': 3,
            'New': 4
        }
        
        for condition, expected_value in condition_mapping.items():
            input_data = {'Condition': condition}
            feature_names = ['Condition']
            
            result = preprocess_input(input_data, feature_names)
            assert result['Condition'].iloc[0] == expected_value
    
    def test_all_property_type_values(self):
        """Test all possible property type values are encoded correctly."""
        property_type_mapping = {
            'Homes': 1,
            'Single Habitation': 2
        }
        
        for prop_type, expected_value in property_type_mapping.items():
            input_data = {'PropertyType': prop_type}
            feature_names = ['PropertyType']
            
            result = preprocess_input(input_data, feature_names)
            assert result['PropertyType'].iloc[0] == expected_value
    
    def test_unknown_condition_value(self):
        """Test handling of unknown condition values."""
        input_data = {'Condition': 'Unknown Condition'}
        feature_names = ['Condition']
        
        result = preprocess_input(input_data, feature_names)
        
        # Unknown values should be handled gracefully (likely NaN or some default)
        # The exact behavior depends on implementation
        assert 'Condition' in result.columns
    
    def test_unknown_property_type_value(self):
        """Test handling of unknown property type values."""
        input_data = {'PropertyType': 'Unknown Type'}
        feature_names = ['PropertyType']
        
        result = preprocess_input(input_data, feature_names)
        
        # Unknown values should be handled gracefully
        assert 'PropertyType' in result.columns

class TestIntegrationScenarios:
    """Test integration scenarios combining multiple functions."""
    
    def test_load_explore_save_workflow(self, sample_dataframe):
        """Test a typical workflow of loading, exploring, and saving data."""
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
            temp_input_path = tmp.name
        
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
            temp_output_path = tmp.name
        
        try:
            # Save sample data first
            sample_dataframe.to_csv(temp_input_path, index=False)
            
            # Load the data
            loaded_data = load_data(temp_input_path)
            assert loaded_data is not None
            
            # Explore the data
            stats = explore_numeric_features(loaded_data, target_column='Price')
            assert isinstance(stats, pd.DataFrame)
            
            # Check missing values
            missing = check_missing_values(loaded_data)
            assert isinstance(missing, pd.Series)
            
            # Save processed data
            save_result = save_processed_data(loaded_data, temp_output_path)
            assert save_result is True
            
        finally:
            for path in [temp_input_path, temp_output_path]:
                if os.path.exists(path):
                    os.unlink(path)

class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_functions_with_none_input(self):
        """Test functions with None as input."""
        # These should handle None gracefully without crashing
        try:
            check_missing_values(None)
        except (AttributeError, TypeError):
            # Expected to fail with None
            pass
        
        try:
            explore_numeric_features(None)
        except (AttributeError, TypeError):
            # Expected to fail with None
            pass
    
    def test_save_with_readonly_directory(self, sample_dataframe):
        """Test saving to a read-only directory."""
        # Try to save to a path that should fail
        readonly_path = '/readonly/path/file.csv'
        
        result = save_processed_data(sample_dataframe, readonly_path)
        
        # Should return False and not crash
        assert result is False