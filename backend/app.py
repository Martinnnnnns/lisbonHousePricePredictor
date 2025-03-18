from flask import Flask, jsonify, request
import os
import sys

def create_app(test_config=None):
    """
    Factory function to create and configure the Flask application.
    
    Args:
        test_config: Configuration for testing (optional)
        
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    
    # Load config based on environment
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
            MODEL_PATH=os.path.join(app.instance_path, 'models'),
            DEBUG=os.environ.get('FLASK_DEBUG', True)
        )
    else:
        app.config.from_mapping(test_config)
    
    # Ensure instance folders exist
    try:
        os.makedirs(app.instance_path, exist_ok=True)
        os.makedirs(app.config['MODEL_PATH'], exist_ok=True)
    except OSError:
        pass
    
    # Add CORS support
    try:
        from flask_cors import CORS
        CORS(app)
    except ImportError:
        print("Flask-CORS not installed. Cross-origin requests may be blocked.")
    
    # Register all blueprints from the routes package
    try:
        from routes import blueprints
        
        # Register blueprints with URL prefixes
        for blueprint in blueprints:
            # Get the blueprint name to determine its prefix
            if blueprint.name == 'prediction':
                prefix = '/api/predictions'
            elif blueprint.name == 'data':
                prefix = '/api/data'
            else:
                prefix = f'/api/{blueprint.name}'
                
            app.register_blueprint(blueprint, url_prefix=prefix)
    except ImportError as e:
        print(f"Error importing routes: {e}")
    
    @app.route('/')
    def home():
        """API home endpoint with documentation."""
        return jsonify({
            'status': 'online',
            'message': 'Lisbon House Price Prediction API',
            'endpoints': {
                'predictions': [
                    '/api/predictions/predict',
                    '/api/predictions/batch-predict',
                    '/api/predictions/model-info'
                ],
                'data': [
                    '/api/data/model-list',
                    '/api/data/model-features/<model_name>',
                    '/api/data/data-summary',
                    '/api/data/parish-list',
                    '/api/data/model-performance'
                ]
            },
            'version': '1.0.0'
        })
    
    @app.route('/healthcheck')
    def healthcheck():
        """Simple health check endpoint."""
        return jsonify({
            'status': 'healthy',
            'service': 'lisbon-house-price-api'
        })
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 'Not found',
            'message': 'The requested resource was not found on the server.',
            'path': request.path
        }), 404
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'error': 'Internal server error',
            'message': 'An unexpected error occurred on the server.'
        }), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host=os.environ.get('FLASK_HOST', '0.0.0.0'),
        port=int(os.environ.get('FLASK_PORT', 5001)),
        debug=app.config['DEBUG']
    )