// frontend/app/models/model3/visuals/page.js
import Link from 'next/link';
import Image from 'next/image';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';

export default function Model3VisualsPage() {
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
        <h2 className="text-xl font-bold text-blue-400 mb-6">Random Forest Model</h2>
        
        {/* Subpage Navigation for this Model */}
        <div className="mt-4">
          <nav className="space-y-2">
            <Link 
              href="/models/model3" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Overview
            </Link>
            <Link 
              href="/models/model3/metrics" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Performance Metrics
            </Link>
            <Link 
              href="/models/model3/results" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartLine className="mr-2" /> Results
            </Link>
            <Link 
              href="/models/model3/visuals" 
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
                  <p className="text-gray-300 text-sm">Random Forest Model (R² = 0.9224)</p>
                  <p className="text-gray-400 text-xs mt-2">RMSE: €66,085.23</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This scatter plot shows the relationship between actual house prices and predicted prices. The Random Forest model achieved an R² score of 0.9224, explaining about 92% of the variance in housing prices, the highest among all models.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Error Distribution</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Histogram Visualization]</p>
                  <p className="text-gray-300 text-sm">Error Distribution</p>
                  <p className="text-gray-400 text-xs mt-2">Mean Error: €10,990.00</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This histogram shows the distribution of prediction errors. With a Mean Absolute Percentage Error (MAPE) of 10.99%, the Random Forest model has the best percentage error metric, demonstrating its superior accuracy in proportional terms.
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
                  <p className="text-gray-400 text-xs mt-2">CV R² Score: 0.9005 ± 0.0828</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization shows the performance across 5 cross-validation folds. The Random Forest model shows good consistency with a cross-validated R² score of 0.9005 ± 0.0828, and performs even better on the test set (R² = 0.9224).
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Feature Importance</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Bar Chart Visualization]</p>
                  <p className="text-gray-300 text-sm">Feature Importance Ranking</p>
                  <p className="text-gray-400 text-xs mt-2">Top Feature: Property Size (0.42)</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This chart shows the importance of each feature in the Random Forest model. Property size, location (parish), and number of bedrooms were identified as the most influential features in determining house prices in Lisbon.
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
                <p className="text-gray-400 text-xs mt-2">Random Forest Model Average Rank: 1.00 of 6</p>
              </div>
            </div>
          </div>
          <p className="mt-4 text-sm text-gray-300">
            This comparison shows how the Random Forest model performs relative to other models in our evaluation. The Random Forest model ranks 1st overall with an average rank of 1.00, performing best across all metrics (RMSE, MAE, MAPE, and R²). Its ensemble approach helps overcome the limitations of single decision trees.
          </p>
          <div className="mt-4 p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Predictive Advantage:</strong> The Random Forest model consistently provides the most accurate predictions across all evaluation metrics. Its ensemble of 50 decision trees mitigates overfitting while capturing complex relationships in the data. For production deployment, this model is recommended as the primary predictor for Lisbon housing prices.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}