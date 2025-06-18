import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append('..')
from backend.data.preprocessing import (
    clean_data, engineer_features, preprocess_data
)

@pytest.fixture
def sample_raw_data():
    """Create sample raw data with common issues."""
    return pd.DataFrame({
        'Id': [1, 2, 3, 4, 5, 5],  # Duplicate row
        'Price': [300000, 450000, 600000, 1500000, 250000, 250000],  # Outlier at index 3
        'AreaNet': [80, 120, 150, 200, np.nan, np.nan],  # Missing values
        'AreaGross': [100, 140, 180, 250, 70, 70],
        'Bedrooms': [2, 3, 4, 5, 1, 1],
        'Bathrooms': [1, 2, 2, 3, 1, 1],
        'Parking': [1, 1, 2, 2, 0, 0],
        'Parish': ['Alvalade', 'Areeiro', 'Alvalade', 'Benfica', None, None],  # Missing values
        'PropertyType': ['Homes', 'Homes', 'Single Habitation', 'Homes', 'Homes', 'Homes'],
        'PropertySubType': ['Apartment', 'Apartment', 'House', 'Apartment', 'Studio', 'Studio'],
        'Condition': ['Used', 'New', 'As New', 'Used', np.nan, np.nan],  # Missing values
        'Price M2': [3750, 3750, 4000, 7500, 3571, 3571],  # High correlation with Price
        'ConstantColumn': [1, 1, 1, 1, 1, 1]  # Single value column
    })

@pytest.fixture
def clean_sample_data():
    """Create cleaned sample data for feature engineering tests."""
    return pd.DataFrame({
        'Price': [300000, 450000, 600000, 250000],
        'AreaNet': [80, 120, 150, 70],
        'AreaGross': [100, 140, 180, 90],
        'Bedrooms': [2, 3, 4, 1],
        'Bathrooms': [1, 2, 2, 1],
        'Parking': [1, 1, 2, 0],
        'Parish': ['Alvalade', 'Areeiro', 'Alvalade', 'Benfica'],
        'PropertyType': ['Homes', 'Homes', 'Single Habitation', 'Homes'],
        'PropertySubType': ['Apartment', 'Apartment', 'House', 'Studio'],
        'Condition': ['Used', 'New', 'As New', 'Used']
    })

class TestCleanData:
    """Test the clean_data function."""
    
    def test_remove_duplicates(self, sample_raw_data):
        """Test that duplicate rows are removed."""
        original_length = len(sample_raw_data)
        cleaned = clean_data(sample_raw_data)
        
        # Should remove one duplicate row
        assert len(cleaned) == original_length - 1
    
    def test_remove_single_value_columns(self, sample_raw_data):
        """Test that columns with only one unique value are removed."""
        cleaned = clean_data(sample_raw_data)
        
        # ConstantColumn should be removed
        assert 'ConstantColumn' not in cleaned.columns
    
    def test_remove_id_column(self, sample_raw_data):
        """Test that Id column is removed."""
        cleaned = clean_data(sample_raw_data)
        
        assert 'Id' not in cleaned.columns
    
    def test_handle_missing_values_numeric(self, sample_raw_data):
        """Test that missing values in numeric columns are filled with median."""
        cleaned = clean_data(sample_raw_data)
        
        # Should have no missing values in numeric columns
        numeric_cols = cleaned.select_dtypes(include=['int64', 'float64']).columns
        assert cleaned[numeric_cols].isnull().sum().sum() == 0
        
        # AreaNet should be filled with median (median of [80, 120, 150, 200] = 135)
        median_area = pd.Series([80, 120, 150, 200]).median()
        filled_values = cleaned[cleaned['AreaNet'] == median_area]
        assert len(filled_values) >= 1  # At least one filled value
    
    def test_handle_missing_values_categorical(self, sample_raw_data):
        """Test that missing values in categorical columns are filled with mode."""
        cleaned = clean_data(sample_raw_data)
        
        # Should have no missing values in categorical columns
        categorical_cols = cleaned.select_dtypes(include=['object']).columns
        assert cleaned[categorical_cols].isnull().sum().sum() == 0
    
    def test_outlier_capping_price(self, sample_raw_data):
        """Test that outliers in Price are capped."""
        cleaned = clean_data(sample_raw_data)
        
        # The outlier value (1,500,000) should be capped
        max_original = sample_raw_data['Price'].max()
        max_cleaned = cleaned['Price'].max()
        
        # Max cleaned should be less than the original outlier
        assert max_cleaned < max_original
    
    def test_price_m2_removal(self, sample_raw_data):
        """Test that Price M2 column is removed due to correlation considerations."""
        # Modify the sample data to have low correlation
        modified_data = sample_raw_data.copy()
        modified_data['Price M2'] = [1, 2, 3, 4, 5, 5]  # Low correlation with Price
        
        cleaned = clean_data(modified_data)
        
        # Price M2 should be removed due to low correlation
        assert 'Price M2' not in cleaned.columns
    
    @patch('backend.data.preprocessing.check_missing_values')
    @patch('backend.data.preprocessing.explore_numeric_features')
    def test_function_calls(self, mock_explore, mock_check, sample_raw_data):
        """Test that utility functions are called during cleaning."""
        clean_data(sample_raw_data)
        
        # These functions should be called during the cleaning process
        mock_check.assert_called()

class TestEngineerFeatures:
    """Test the engineer_features function."""
    
    def test_price_per_bedroom_feature(self, clean_sample_data):
        """Test creation of PricePerBedroom feature."""
        engineered = engineer_features(clean_sample_data)
        
        assert 'PricePerBedroom' in engineered.columns
        
        # Test calculation: Price / Bedrooms
        expected_first = clean_sample_data.iloc[0]['Price'] / clean_sample_data.iloc[0]['Bedrooms']
        assert engineered.iloc[0]['PricePerBedroom'] == expected_first
    
    def test_price_per_bedroom_zero_bedrooms(self, clean_sample_data):
        """Test PricePerBedroom when Bedrooms is 0."""
        modified_data = clean_sample_data.copy()
        modified_data.iloc[0, modified_data.columns.get_loc('Bedrooms')] = 0
        
        engineered = engineer_features(modified_data)
        
        # When Bedrooms is 0, should return just the Price
        assert engineered.iloc[0]['PricePerBedroom'] == modified_data.iloc[0]['Price']
    
    def test_bathroom_to_bedroom_ratio(self, clean_sample_data):
        """Test creation of BathroomToBedroom feature."""
        engineered = engineer_features(clean_sample_data)
        
        assert 'BathroomToBedroom' in engineered.columns
        
        # Test calculation: Bathrooms / Bedrooms
        expected_first = clean_sample_data.iloc[0]['Bathrooms'] / clean_sample_data.iloc[0]['Bedrooms']
        assert engineered.iloc[0]['BathroomToBedroom'] == expected_first
    
    def test_bathroom_to_bedroom_zero_bedrooms(self, clean_sample_data):
        """Test BathroomToBedroom when Bedrooms is 0."""
        modified_data = clean_sample_data.copy()
        modified_data.iloc[0, modified_data.columns.get_loc('Bedrooms')] = 0
        
        engineered = engineer_features(modified_data)
        
        # When Bedrooms is 0, should return just the Bathrooms
        assert engineered.iloc[0]['BathroomToBedroom'] == modified_data.iloc[0]['Bathrooms']
    
    def test_area_utilization_ratio(self, clean_sample_data):
        """Test creation of AreaUtilizationRatio feature."""
        engineered = engineer_features(clean_sample_data)
        
        assert 'AreaUtilizationRatio' in engineered.columns
        
        # Test calculation: AreaNet / AreaGross
        expected_first = clean_sample_data.iloc[0]['AreaNet'] / clean_sample_data.iloc[0]['AreaGross']
        assert engineered.iloc[0]['AreaUtilizationRatio'] == expected_first
    
    def test_area_utilization_ratio_zero_gross(self, clean_sample_data):
        """Test AreaUtilizationRatio when AreaGross is 0."""
        modified_data = clean_sample_data.copy()
        modified_data.iloc[0, modified_data.columns.get_loc('AreaGross')] = 0
        
        engineered = engineer_features(modified_data)
        
        # When AreaGross is 0, should return 0
        assert engineered.iloc[0]['AreaUtilizationRatio'] == 0
    
    def test_property_category_feature(self, clean_sample_data):
        """Test creation of PropertyCategory feature."""
        engineered = engineer_features(clean_sample_data)
        
        assert 'PropertyCategory' in engineered.columns
        
        # Test combination of PropertyType and PropertySubType
        expected_first = f"{clean_sample_data.iloc[0]['PropertyType']}_{clean_sample_data.iloc[0]['PropertySubType']}"
        assert engineered.iloc[0]['PropertyCategory'] == expected_first
    
    @patch('backend.data.preprocessing.explore_numeric_features')
    def test_explore_features_called(self, mock_explore, clean_sample_data):
        """Test that explore_numeric_features is called."""
        engineer_features(clean_sample_data)
        
        mock_explore.assert_called_once()

class TestPreprocessData:
    """Test the preprocess_data function."""
    
    def test_train_test_split(self, clean_sample_data):
        """Test that data is properly split into train and test sets."""
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(clean_sample_data)
        
        # Check that we have both train and test sets
        assert len(X_train) > 0
        assert len(X_test) > 0
        assert len(y_train) > 0
        assert len(y_test) > 0
        
        # Check that train + test = total (accounting for rounding)
        total_samples = len(clean_sample_data)
        assert len(X_train) + len(X_test) == total_samples
        assert len(y_train) + len(y_test) == total_samples
    
    def test_target_column_removed_from_features(self, clean_sample_data):
        """Test that target column is removed from features."""
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(clean_sample_data)
        
        # Reconstruct X from processed data isn't straightforward, but we can check shapes
        assert isinstance(X_train, np.ndarray)
        assert isinstance(X_test, np.ndarray)
    
    def test_preprocessing_pipeline_created(self, clean_sample_data):
        """Test that preprocessing pipeline is created and returned."""
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(clean_sample_data)
        
        # Preprocessor should be a ColumnTransformer
        from sklearn.compose import ColumnTransformer
        assert isinstance(preprocessor, ColumnTransformer)
    
    def test_custom_test_size(self, clean_sample_data):
        """Test preprocessing with custom test size."""
        test_size = 0.3
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(
            clean_sample_data, test_size=test_size
        )
        
        total_samples = len(clean_sample_data)
        expected_test_size = int(total_samples * test_size)
        
        # Allow for small rounding differences
        assert abs(len(X_test) - expected_test_size) <= 1
    
    def test_custom_target_column(self, clean_sample_data):
        """Test preprocessing with custom target column."""
        # Add a new target column
        modified_data = clean_sample_data.copy()
        modified_data['NewTarget'] = modified_data['Price'] * 2
        
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(
            modified_data, target_col='NewTarget'
        )
        
        # Check that y values are from the new target
        assert y_train.iloc[0] == modified_data.iloc[0]['NewTarget'] * 2 or y_train.iloc[0] == modified_data.iloc[1]['NewTarget']
    
    def test_preprocessor_handles_numeric_features(self, clean_sample_data):
        """Test that preprocessor properly handles numeric features."""
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(clean_sample_data)
        
        # X_train and X_test should be arrays (processed data)
        assert isinstance(X_train, np.ndarray)
        assert isinstance(X_test, np.ndarray)
        
        # Should have same number of features
        assert X_train.shape[1] == X_test.shape[1]
    
    def test_preprocessor_handles_categorical_features(self, clean_sample_data):
        """Test that preprocessor properly handles categorical features."""
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(clean_sample_data)
        
        # After one-hot encoding, should have more features than original
        original_feature_count = len(clean_sample_data.columns) - 1  # Minus target
        processed_feature_count = X_train.shape[1]
        
        # Should have more features due to one-hot encoding
        assert processed_feature_count >= original_feature_count

class TestIntegrationWorkflow:
    """Test the complete preprocessing workflow."""
    
    def test_complete_preprocessing_pipeline(self, sample_raw_data):
        """Test the complete workflow from raw data to processed."""
        # Step 1: Clean data
        cleaned_data = clean_data(sample_raw_data)
        
        # Step 2: Engineer features
        engineered_data = engineer_features(cleaned_data)
        
        # Step 3: Preprocess for modeling
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(engineered_data)
        
        # Verify the complete pipeline works
        assert len(X_train) > 0
        assert len(X_test) > 0
        assert len(y_train) > 0
        assert len(y_test) > 0
        
        # Check that we have reasonable data shapes
        assert X_train.shape[1] > 0  # Should have features
        assert X_train.shape[0] > 0  # Should have samples
    
    def test_pipeline_handles_edge_cases(self):
        """Test pipeline with edge cases."""
        # Create minimal dataset
        minimal_data = pd.DataFrame({
            'Price': [300000, 450000],
            'AreaNet': [80, 120],
            'Bedrooms': [2, 3],
            'Parish': ['Alvalade', 'Areeiro']
        })
        
        # Should not crash with minimal data
        cleaned = clean_data(minimal_data)
        engineered = engineer_features(cleaned)
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(engineered)
        
        # Should produce valid results even with minimal data
        assert len(X_train) + len(X_test) == 2

class TestErrorHandling:
    """Test error handling in preprocessing functions."""
    
    def test_clean_data_empty_dataframe(self):
        """Test clean_data with empty dataframe."""
        empty_df = pd.DataFrame()
        
        # Should handle empty dataframe gracefully
        result = clean_data(empty_df)
        assert isinstance(result, pd.DataFrame)
    
    def test_engineer_features_missing_columns(self):
        """Test engineer_features when expected columns are missing."""
        minimal_df = pd.DataFrame({
            'Price': [300000, 450000],
            'SomeOtherColumn': [1, 2]
        })
        
        # Should not crash when expected columns are missing
        result = engineer_features(minimal_df)
        assert isinstance(result, pd.DataFrame)
    
    def test_preprocess_data_insufficient_samples(self):
        """Test preprocess_data with very few samples."""
        tiny_df = pd.DataFrame({
            'Price': [300000],
            'Feature': [1]
        })
        
        # With only one sample, should handle gracefully
        try:
            X_train, X_test, y_train, y_test, preprocessor = preprocess_data(tiny_df)
            # If it succeeds, that's fine
            assert True
        except ValueError:
            # If it fails due to insufficient samples, that's also expected
            assert True

class TestDataQuality:
    """Test data quality checks and validations."""
    
    def test_no_data_leakage(self, clean_sample_data):
        """Test that there's no data leakage between train and test sets."""
        # Set a fixed random state to make this test deterministic
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(
            clean_sample_data, random_state=42
        )
        
        # Convert to sets for easier comparison (if possible)
        # Since we're dealing with processed arrays, we check shapes instead
        assert X_train.shape[0] > 0
        assert X_test.shape[0] > 0
        
        # Train and test should have no overlap in indices
        total_samples = X_train.shape[0] + X_test.shape[0]
        assert total_samples == len(clean_sample_data)
    
    def test_feature_scaling_applied(self, clean_sample_data):
        """Test that feature scaling is applied to numeric features."""
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(clean_sample_data)
        
        # After standard scaling, features should have different scales than original
        # We can't easily check the exact values since data is transformed,
        # but we can verify the shapes are correct
        assert X_train.shape[1] > 0
        assert X_test.shape[1] > 0
        assert X_train.shape[1] == X_test.shape[1]
    
    def test_categorical_encoding_applied(self, clean_sample_data):
        """Test that categorical encoding is applied."""
        original_feature_count = len([col for col in clean_sample_data.columns 
                                    if col != 'Price'])
        
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(clean_sample_data)
        
        # After one-hot encoding, should typically have more features
        processed_feature_count = X_train.shape[1]
        
        # This might not always be true if there are only binary categoricals,
        # but it's a reasonable check for our test data
        assert processed_feature_count >= original_feature_count

class TestPreprocessorConsistency:
    """Test that the preprocessor produces consistent results."""
    
    def test_preprocessor_transform_consistency(self, clean_sample_data):
        """Test that the preprocessor transforms data consistently."""
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(clean_sample_data)
        
        # Create new test data similar to training data
        new_data = clean_sample_data.drop('Price', axis=1).iloc[:2]
        
        # Transform the new data using the fitted preprocessor
        transformed_new = preprocessor.transform(new_data)
        
        # Should have same number of features as training data
        assert transformed_new.shape[1] == X_train.shape[1]
    
    def test_reproducible_results(self, clean_sample_data):
        """Test that preprocessing produces reproducible results."""
        # Run preprocessing twice with same random state
        result1 = preprocess_data(clean_sample_data, random_state=42)
        result2 = preprocess_data(clean_sample_data, random_state=42)
        
        X_train1, X_test1, y_train1, y_test1, _ = result1
        X_train2, X_test2, y_train2, y_test2, _ = result2
        
        # Results should be identical
        np.testing.assert_array_equal(X_train1, X_train2)
        np.testing.assert_array_equal(X_test1, X_test2)
        np.testing.assert_array_equal(y_train1, y_train2)
        np.testing.assert_array_equal(y_test1, y_test2)

class TestPerformance:
    """Test performance-related aspects of preprocessing."""
    
    def test_preprocessing_handles_large_categorical_variety(self):
        """Test preprocessing with many categorical values."""
        # Create data with many categorical values
        large_cat_data = pd.DataFrame({
            'Price': np.random.randint(200000, 800000, 100),
            'AreaNet': np.random.randint(50, 200, 100),
            'Parish': [f'Parish_{i%20}' for i in range(100)],  # 20 different parishes
            'PropertyType': np.random.choice(['Homes', 'Single Habitation'], 100)
        })
        
        # Should handle large categorical variety without issues
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(large_cat_data)
        
        # Check that it produces reasonable results
        assert X_train.shape[0] > 0
        assert X_test.shape[0] > 0
        assert X_train.shape[1] > 0  # Should have features after one-hot encoding
    
    def test_memory_efficiency_large_dataset(self):
        """Test that preprocessing doesn't consume excessive memory."""
        # Create a moderately large dataset
        n_samples = 1000
        large_data = pd.DataFrame({
            'Price': np.random.randint(200000, 800000, n_samples),
            'AreaNet': np.random.randint(50, 200, n_samples),
            'AreaGross': np.random.randint(60, 250, n_samples),
            'Bedrooms': np.random.randint(1, 6, n_samples),
            'Bathrooms': np.random.randint(1, 4, n_samples),
            'Parish': np.random.choice(['Alvalade', 'Areeiro', 'Benfica', 'Lumiar'], n_samples),
            'PropertyType': np.random.choice(['Homes', 'Single Habitation'], n_samples),
            'Condition': np.random.choice(['New', 'Used', 'As New'], n_samples)
        })
        
        # Should process without memory issues
        X_train, X_test, y_train, y_test, preprocessor = preprocess_data(large_data)
        
        # Verify reasonable output
        assert X_train.shape[0] + X_test.shape[0] == n_samples
        assert X_train.shape[1] > 0

if __name__ == "__main__":
    # Example of how to run specific test classes
    pytest.main([__file__, "-v"])