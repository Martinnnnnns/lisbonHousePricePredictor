// frontend/app/models/model1/visuals/page.js
import Link from 'next/link';
import Image from 'next/image';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';

export default function Model1VisualsPage() {
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
        <h2 className="text-xl font-bold text-blue-400 mb-6">Linear Model</h2>
        
        {/* Subpage Navigation for this Model */}
        <div className="mt-4">
          <nav className="space-y-2">
            <Link 
              href="/models/model1" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Overview
            </Link>
            <Link 
              href="/models/model1/metrics" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Performance Metrics
            </Link>
            <Link 
              href="/models/model1/results" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartLine className="mr-2" /> Results
            </Link>
            <Link 
              href="/models/model1/visuals" 
              className="block p-2 rounded-lg bg-blue-800 text-white transition-colors flex items-center"
            >
              <FaChartPie className="mr-2" /> Visualizations
            </Link>
          </nav>
        </div>
      </div>
      
      {/* Main Content Area */}
      <div className="flex-1 py-12 px-8">
        <h1 className="text-4xl font-bold mb-3 text-blue-400">Visualizations</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Actual vs. Predicted Prices</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Scatter Plot Visualization]</p>
                  <p className="text-gray-300 text-sm">Linear Model (R² = 0.8513)</p>
                  <p className="text-gray-400 text-xs mt-2">RMSE: €91,468.46</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This scatter plot shows the relationship between actual house prices and predicted prices. In our evaluation, the Linear model achieved an R² score of 0.8513, indicating it explains about 85% of the variance in housing prices.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Error Distribution</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Histogram Visualization]</p>
                  <p className="text-gray-300 text-sm">Error Distribution</p>
                  <p className="text-gray-400 text-xs mt-2">Mean Error: €20,153.91</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This histogram shows the distribution of prediction errors. The model has a Mean Absolute Percentage Error (MAPE) of 20.15%, which is higher than some of our other models, indicating areas for potential improvement.
            </p>
          </div>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Cross-Validation Performance</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Box Plot Visualization]</p>
                  <p className="text-gray-300 text-sm">5-Fold Cross-Validation</p>
                  <p className="text-gray-400 text-xs mt-2">CV R² Score: 0.9057 ± 0.0538</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization shows the performance across 5 cross-validation folds. The Linear model shows good consistency in performance, with a cross-validated R² score of 0.9057 ± 0.0538, indicating reliable predictive power.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Residual Analysis</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Residual Plot Visualization]</p>
                  <p className="text-gray-300 text-sm">Residuals vs. Predicted Values</p>
                  <p className="text-gray-400 text-xs mt-2">MAE: €69,956.68</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This plot shows residuals (differences between actual and predicted values) against predicted values. The linear model has a Mean Absolute Error of €69,956.68, which ranks 5th among our 6 models.
            </p>
          </div>
        </div>
        
        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-xl font-bold mb-4 text-blue-400">Model Comparison</h2>
          <div className="aspect-video relative bg-gray-800 rounded-lg overflow-hidden">
            <div className="flex items-center justify-center h-full">
              <div className="text-center p-6">
                <p className="text-gray-400 mb-4">[Bar Chart Visualization]</p>
                <p className="text-gray-300 text-sm">Performance Metrics Across All Models</p>
                <p className="text-gray-400 text-xs mt-2">Linear Model Average Rank: 4.75 of 6</p>
              </div>
            </div>
          </div>
          <p className="mt-4 text-sm text-gray-300">
            This comparison shows how the Linear model performs relative to other models in our evaluation. The Linear model ranks 4th overall with an average rank of 4.75. While it provides good interpretability, other models like Random Forest (rank 1.00) and Lasso (rank 2.50) offer better prediction accuracy.
          </p>
          <div className="mt-4 p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Important Note:</strong> In our most recent prediction run, the Linear model predicted a value of €101,684,946.24, which was significantly higher than other models and excluded from the ensemble average. This outlier prediction suggests the Linear model may be more susceptible to extreme values in certain feature combinations.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}