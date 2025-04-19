# Lisbon House Price Predictor

A full-stack web application for predicting real estate prices in Lisbon, Portugal. The application uses a machine learning model trained on local housing data to estimate property values based on features like location, size, and amenities.

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

## Model Information

The prediction model is built using scikit-learn's linear regression algorithm. It analyzes the relationship between property features and prices, allowing it to predict the value of new properties based on their characteristics.

Key features that influence property prices in Lisbon:
- Location (Parish)
- Property size (Area)
- Number of bedrooms and bathrooms
- Property condition
- Property type

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Dataset sourced from Lisbon real estate listings
- Built with Flask and React
- Machine learning model powered by scikit-learn
