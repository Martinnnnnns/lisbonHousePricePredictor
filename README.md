# Lisbon House Price Predictor

A full-stack web application for predicting real estate prices in Lisbon, Portugal. The application uses a machine learning model trained on local housing data to estimate property values based on features like location, size, and amenities.

![Lisbon](https://images.unsplash.com/photo-1569701813229-33284b643e3c?q=80&w=1170)

## Features

- **Machine Learning-Powered Predictions**: Linear regression model trained on Lisbon housing data
- **Interactive Property Input**: User-friendly form to input property details
- **Data Visualizations**: Explore trends and patterns in the Lisbon real estate market
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

### Backend
- **Flask**: Python web framework for the API
- **scikit-learn**: Machine learning library for the prediction model
- **Pandas & NumPy**: Data processing and numerical computation
- **Matplotlib**: Data visualization

### Frontend
- **React**: JavaScript library for building the user interface
- **Axios**: Promise-based HTTP client for API requests
- **Chart.js/Recharts**: Visualization libraries for interactive charts
- **React Bootstrap**: UI component library

## Project Structure

```
lisbon_price_predictor/
├── backend/
│   ├── app.py                    # Main Flask application
│   ├── data/                     # Data directory
│   │   ├── lisbonhouses.csv      # Property dataset
│   │   └── processed/            # Processed datasets
│   ├── models/                   # Saved ML models
│   │   └── price_model.pkl       # Trained model
│   ├── utils/                    # Helper functions
│   │   ├── preprocess.py         # Data preprocessing
│   │   └── predict.py            # Prediction logic
│   └── routes/                   # API routes
│       ├── prediction_routes.py  # Prediction endpoints
│       └── data_routes.py        # Data endpoints for frontend
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── PredictionForm.js   # Property input form
│   │   │   ├── Results.js          # Prediction results
│   │   │   ├── DataTable.js        # Display property data
│   │   │   └── Charts.js           # Data visualizations
│   │   ├── pages/
│   │   │   ├── Home.js             # Landing page
│   │   │   ├── Predict.js          # Prediction page
│   │   │   └── DataExplorer.js     # Data exploration page
│   │   ├── services/
│   │   │   └── api.js              # API calls to backend
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── requirements.txt              # Project dependencies
├── LICENSE                       # MIT License
└── README.md                     # This file
```

## Dataset

The application uses a dataset (`lisbonhouses.csv`) with the following information about Lisbon properties:

- Property condition (Used, New, As New, For Refurbishment)
- Property types and subtypes
- Number of bedrooms and bathrooms
- Net and gross areas
- Parking availability
- Geographic coordinates
- Parish/neighborhood
- Price per square meter
- Total price

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- pip
- npm

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lisbon_price_predictor.git
   cd lisbon_price_predictor
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```bash
   cd backend
   python app.py
   ```
   The backend will be available at http://localhost:5000

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```
   The frontend will be available at http://localhost:3000

## Usage

1. Navigate to the Predict page
2. Fill in the property details:
   - Condition
   - Property type
   - Location (Parish)
   - Area
   - Number of bedrooms and bathrooms
   - Other relevant features
3. Click "Predict Price" to get an estimated property value
4. View the prediction result and confidence interval

## API Endpoints

- `POST /api/predict`: Submit property details and receive a price prediction
- `GET /api/properties`: Retrieve the property dataset
- `GET /api/property-stats`: Get statistical information about the properties
- `GET /api/parishes`: Get a list of parishes/neighborhoods

## Model Information

The prediction model is built using scikit-learn's linear regression algorithm. It analyzes the relationship between property features and prices, allowing it to predict the value of new properties based on their characteristics.

Key features that influence property prices in Lisbon:
- Location (Parish)
- Property size (Area)
- Number of bedrooms and bathrooms
- Property condition
- Property type

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Dataset sourced from Lisbon real estate listings
- Built with Flask and React
- Machine learning model powered by scikit-learn