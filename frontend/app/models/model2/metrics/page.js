// frontend/app/models/model2/metrics/page.js
import Link from 'next/link';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';

export default function Model2MetricsPage() {
  return (
    <div className="flex min-h-screen bg-black">
      {/* Left Sidebar - Only Model Detail Navigation */}
      <div className="w-64 bg-gray-900 border-r border-gray-800 p-6">
        <Link 
            href="/models" 
            className="inline-flex items-center text-blue-400 hover:text-blue-300 mb-6"
          >
            <FaArrowLeft className="mr-2" /> All Models
        </Link>
        <h2 className="text-xl font-bold text-blue-400 mb-6">Decision Tree Model</h2>
        <nav className="space-y-2">
          <Link 
            href="/models/model2" 
            className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
          >
            <FaChartBar className="mr-2" /> Overview
          </Link>
          <Link 
            href="/models/model2/metrics" 
            className="block p-2 rounded-lg bg-blue-800 text-white transition-colors flex items-center"
          >
            <FaChartBar className="mr-2" /> Performance Metrics
          </Link>
          <Link 
            href="/models/model2/results" 
            className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
          >
            <FaChartLine className="mr-2" /> Results
          </Link>
          <Link 
            href="/models/model2/visuals" 
            className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
          >
            <FaChartPie className="mr-2" /> Visualizations
          </Link>
        </nav>
      </div>
      
      {/* Main Content Area */}
      <div className="flex-1 py-12 px-8">
        <h1 className="text-4xl font-bold mb-3 text-blue-400">Performance Metrics</h1>
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl mb-8">
          <h2 className="text-2xl font-bold mb-6 text-blue-400">Evaluation Metrics</h2>
          
          <p className="text-gray-300 mb-6">
            The following metrics have been used to evaluate our Decision Tree model's performance in predicting Lisbon house prices:
          </p>
          
          <div className="space-y-6">
            <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
              <h3 className="text-lg font-semibold text-white mb-2">Root Mean Squared Error (RMSE): €96,198.62</h3>
              <p className="text-gray-300 mb-2">
                Square root of the average of squared differences between predicted and actual values. Gives higher weight to larger errors.
              </p>
              <p className="text-sm text-gray-400">
                Formula: RMSE = √[(1/n) * Σ(y<sub>i</sub> - ŷ<sub>i</sub>)²]
              </p>
            </div>
            
            <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
              <h3 className="text-lg font-semibold text-white mb-2">Mean Absolute Error (MAE): €54,200.06</h3>
              <p className="text-gray-300 mb-2">
                Average of the absolute differences between predicted and actual values. Less sensitive to outliers than RMSE.
              </p>
              <p className="text-sm text-gray-400">
                Formula: MAE = (1/n) * Σ|y<sub>i</sub> - ŷ<sub>i</sub>|
              </p>
            </div>
            
            <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
              <h3 className="text-lg font-semibold text-white mb-2">Mean Absolute Percentage Error (MAPE): 13.97%</h3>
              <p className="text-gray-300 mb-2">
                Average of absolute percentage errors, providing an intuitive understanding of error magnitude in percentage terms.
              </p>
              <p className="text-sm text-gray-400">
                Formula: MAPE = (100%/n) * Σ|y<sub>i</sub> - ŷ<sub>i</sub>| / y<sub>i</sub>
              </p>
            </div>
            
            <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
              <h3 className="text-lg font-semibold text-white mb-2">R² Score (Coefficient of Determination): 0.8355</h3>
              <p className="text-gray-300 mb-2">
                Represents the proportion of variance in the target variable that is predictable from the input features.
              </p>
              <p className="text-sm text-gray-400">
                Range: 0 to 1, where 1 indicates perfect prediction and 0 indicates a model that predicts the mean of the data
              </p>
            </div>
          </div>
        </div>
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl mb-8">
          <h2 className="text-2xl font-bold mb-6 text-blue-400">Cross-Validation Results</h2>
          
          <p className="text-gray-300 mb-6">
            The model was evaluated using 5-fold cross-validation to ensure robust performance assessment:
          </p>
          
          <div className="space-y-6">
            <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
              <h3 className="text-lg font-semibold text-white mb-2">Cross-validated R² Score: 0.8341 ± 0.1276</h3>
              <p className="text-gray-300 mb-2">
                The model explains approximately 83.4% of the variance in housing prices across the validation folds, with relatively high inconsistency.
              </p>
            </div>
            
            <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
              <h3 className="text-lg font-semibold text-white mb-2">Cross-validated RMSE: €126,645.73 ± €44,803.59</h3>
              <p className="text-gray-300 mb-2">
                The average root mean squared error across all validation folds, with a high standard deviation indicating significant variability in performance.
              </p>
            </div>
            
            <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
              <h3 className="text-lg font-semibold text-white mb-2">Cross-validated MAE: €73,477.87 ± €20,539.73</h3>
              <p className="text-gray-300 mb-2">
                The average mean absolute error across all validation folds, showing considerable variability in prediction accuracy.
              </p>
            </div>
          </div>
        </div>
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-2xl font-bold mb-6 text-blue-400">Cross-Validation Methodology</h2>
          
          <p className="text-gray-300 mb-6">
            To ensure robust evaluation and avoid overfitting, our Decision Tree model was evaluated using k-fold cross-validation with the following approach:
          </p>
          
          <div className="space-y-4">
            <div className="flex items-start">
              <div className="flex-shrink-0 w-8 h-8 bg-blue-900 rounded-full flex items-center justify-center text-blue-400 mr-4 mt-1">
                1
              </div>
              <div>
                <h4 className="text-white font-medium">Data Splitting</h4>
                <p className="text-gray-300">The dataset of 246 rows was randomly split into training (196 samples) and testing (50 samples) sets</p>
              </div>
            </div>
            
            <div className="flex items-start">
              <div className="flex-shrink-0 w-8 h-8 bg-blue-900 rounded-full flex items-center justify-center text-blue-400 mr-4 mt-1">
                2
              </div>
              <div>
                <h4 className="text-white font-medium">K-Fold Cross-Validation</h4>
                <p className="text-gray-300">The training set was further divided into 5 equal folds for cross-validation</p>
              </div>
            </div>
            
            <div className="flex items-start">
              <div className="flex-shrink-0 w-8 h-8 bg-blue-900 rounded-full flex items-center justify-center text-blue-400 mr-4 mt-1">
                3
              </div>
              <div>
                <h4 className="text-white font-medium">Hyperparameter Tuning</h4>
                <p className="text-gray-300">Grid search was used to find optimal hyperparameters: max_depth=None, min_samples_split=5</p>
              </div>
            </div>
            
            <div className="flex items-start">
              <div className="flex-shrink-0 w-8 h-8 bg-blue-900 rounded-full flex items-center justify-center text-blue-400 mr-4 mt-1">
                4
              </div>
              <div>
                <h4 className="text-white font-medium">Model Training & Evaluation</h4>
                <p className="text-gray-300">For each iteration, the model was trained on 4 folds and evaluated on the remaining fold</p>
              </div>
            </div>
            
            <div className="flex items-start">
              <div className="flex-shrink-0 w-8 h-8 bg-blue-900 rounded-full flex items-center justify-center text-blue-400 mr-4 mt-1">
                5
              </div>
              <div>
                <h4 className="text-white font-medium">Metric Calculation</h4>
                <p className="text-gray-300">Performance metrics were calculated for each fold and aggregated to produce mean and standard deviation values</p>
              </div>
            </div>
            
            <div className="flex items-start">
              <div className="flex-shrink-0 w-8 h-8 bg-blue-900 rounded-full flex items-center justify-center text-blue-400 mr-4 mt-1">
                6
              </div>
              <div>
                <h4 className="text-white font-medium">Final Evaluation</h4>
                <p className="text-gray-300">The fully trained model was evaluated on the reserved test set to obtain the final performance metrics</p>
              </div>
            </div>
          </div>
          
          <div className="mt-6 p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Note:</strong> The high standard deviation in cross-validated metrics (R² = 0.8341 ± 0.1276) suggests that the Decision Tree model's performance varies significantly depending on the specific data it encounters. This indicates potential issues with model stability.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}