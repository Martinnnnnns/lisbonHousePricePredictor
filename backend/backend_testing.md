# Backend Testing Guide

Simple guide for running tests on the Lisbon House Price Predictor backend.

## Running Tests

### 1. Install Test Dependencies
```bash
pip install pytest-flask pytest-mock pytest-cov pytest-xdist
```

### 2. Run All Tests
```bash
pytest tests/ -v
```

### 3. Run with Coverage
```bash
pytest tests/ --cov=routes --cov=models --cov=utils --cov-report=html
```

## Test Files Structure

```
tests/
├── conftest.py              # Shared test setup and fixtures
├── test_data_routes.py      # API endpoints for data (/api/data/*)
├── test_prediction_routes.py # API endpoints for predictions (/api/predictions/*)
├── test_model_prediction.py # Model loading and prediction logic
├── test_preprocessing.py    # Data cleaning and feature engineering
└── test_data_utils.py       # Utility functions
```

## pytest.ini Configuration

The `pytest.ini` file controls how tests run:

- **Finds tests**: Automatically discovers `test_*.py` files
- **Output format**: Shows verbose results with colors and timing
- **Test markers**: Organize tests into categories
- **Coverage tracking**: Measures which code is tested
- **Logging**: Captures output during test execution

## Test Categories (Markers)

Run specific types of tests:

```bash
pytest tests/ -m unit        # Fast isolated tests
pytest tests/ -m api         # API endpoint tests  
pytest tests/ -m integration # Tests that use multiple components
pytest tests/ -m "not slow"  # Skip time-consuming tests
```

## conftest.py Fixtures

Provides shared test data across all test files:

- **`sample_house_data`** - Example house for predictions
- **`sample_dataframe`** - Example dataset for data processing
- **`mock_model`** - Fake ML model for testing
- **`client`** - Flask test client for API calls
- **`temp_csv_file`** - Temporary files for safe testing

## Useful Test Commands

```bash
# Run specific test file
pytest tests/test_data_routes.py -v

# Run specific test function
pytest tests/test_data_routes.py::TestModelList::test_get_model_list_success -v

# Run tests in parallel (faster)
pytest tests/ -n auto

# Show detailed output
pytest tests/ -v -s

# Stop on first failure
pytest tests/ -x

# Run only failed tests from last run
pytest tests/ --lf

# Generate HTML coverage report
pytest tests/ --cov=routes --cov=models --cov=utils --cov-report=html
# Then open: htmlcov/index.html
```

## What Each Test File Tests

| File | Tests |
|------|-------|
| `test_data_routes.py` | `/model-list`, `/parish-list`, `/data-summary` endpoints |
| `test_prediction_routes.py` | `/predict`, `/batch-predict`, `/model-info` endpoints |
| `test_model_prediction.py` | Model loading, preprocessing, price prediction logic |
| `test_preprocessing.py` | Data cleaning, outlier removal, feature engineering |
| `test_data_utils.py` | File loading/saving, missing value checks, data exploration |

## Common Issues

**Import errors?**
```bash
cd backend
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
pytest tests/ -v
```

**Missing files?**
```bash
touch tests/__init__.py
touch routes/__init__.py
touch models/__init__.py
touch utils/__init__.py
```

**Tests work without real models** - they use mock data when actual model files don't exist.

## Quick Test Check

```bash
# Verify everything works
pytest tests/ --tb=short -q
```

If you see `X passed`, you're good to go! 🎉