
"""
API routes package for Lisbon House Price Prediction API.
Contains blueprint definitions for all API endpoints.
"""

# Import all blueprints
from .prediction_routes import prediction_bp
from .data_routes import data_bp

# List of all blueprints to be registered with the Flask app
blueprints = [
    prediction_bp,
    data_bp,
]

# For backward compatibility and explicit imports
__all__ = [
    'prediction_bp',
    'data_bp',
    'blueprints', 
]