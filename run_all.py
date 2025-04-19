#!/usr/bin/env python
"""
Lisbon House Price Prediction - Simple Pipeline Runner
"""
import sys
import os

# Get the absolute path to the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

# Add the project root to the Python path
sys.path.append(project_root)

# Create the necessary directories if they don't exist
os.makedirs('./backend/models/saved_models', exist_ok=True)
os.makedirs('./backend/models/logs', exist_ok=True)
os.makedirs('./backend/models/visuals', exist_ok=True)

print("Starting Lisbon House Price Prediction Pipeline...")

# Import the model_logging module first
sys.path.insert(0, os.path.join(project_root, 'backend', 'models'))
from backend.models.model_logging import log_model_operation

# Step 1: Train models
print("\n--- Step 1: Training Models ---")
from backend.models.model_training import main as train_models
train_models()

# Step 2: Test predictions
print("\n--- Step 2: Testing Predictions ---")
from backend.models.model_prediction import main as test_predictions
test_predictions()

# Step 3: Evaluate models
print("\n--- Step 3: Evaluating Models ---")
from backend.models.model_evaluation import main as evaluate_models
evaluate_models()

print("\nPipeline execution complete!")