// frontend/app/models/model4/visuals/page.js
import Link from 'next/link';
import Image from 'next/image';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';

export default function Model4VisualsPage() {
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
        <h2 className="text-xl font-bold text-blue-400 mb-6">SVR Model</h2>
        
        {/* Subpage Navigation for this Model */}
        <div className="mt-4">
          <nav className="space-y-2">
            <Link 
              href="/models/model4" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Overview
            </Link>
            <Link 
              href="/models/model4/metrics" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Performance Metrics
            </Link>
            <Link 
              href="/models/model4/results" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartLine className="mr-2" /> Results
            </Link>
            <Link 
              href="/models/model4/visuals" 
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
                  <p className="text-gray-300 text-sm">SVR Model (R² = 0.8393)</p>
                  <p className="text-gray-400 text-xs mt-2">RMSE: €95,101.69</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This scatter plot shows the relationship between actual house prices and predicted prices. The SVR model achieved an R² score of 0.8393, explaining about 84% of the variance in housing prices, with moderate prediction accuracy.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Error Distribution</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Histogram Visualization]</p>
                  <p className="text-gray-300 text-sm">Error Distribution</p>
                  <p className="text-gray-400 text-xs mt-2">Mean Error: €19,240.80</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This histogram shows the distribution of prediction errors. With a Mean Absolute Percentage Error (MAPE) of 19.24%, the SVR model shows relatively high percentage errors compared to other models, though the error distribution pattern may provide useful insights.
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
                  <p className="text-gray-400 text-xs mt-2">CV R² Score: 0.8462 ± 0.0464</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization shows the performance across 5 cross-validation folds. The SVR model shows moderate consistency in performance with an R² score of 0.8462 ± 0.0464, but has the highest cross-validation RMSE (€131,123.66 ± €21,209.45) among all models.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Hyperparameter Tuning</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Heatmap Visualization]</p>
                  <p className="text-gray-300 text-sm">Grid Search Results</p>
                  <p className="text-gray-400 text-xs mt-2">Best Parameters: C=1.0, epsilon=0.01</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization shows the performance of different hyperparameter combinations during grid search. After testing 24 combinations, the optimal parameters were identified as C=1.0, epsilon=0.01, gamma='scale', and kernel='linear', offering the best balance of model flexibility and generalization.
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
                <p className="text-gray-400 text-xs mt-2">SVR Model Average Rank: 5.25 of 6</p>
              </div>
            </div>
          </div>
          <p className="mt-4 text-sm text-gray-300">
            This comparison shows how the SVR model performs relative to other models in our evaluation. The SVR model ranks 6th overall with an average rank of 5.25. While it has the lowest overall performance among the models tested, it still contributes to the ensemble approach and may offer value for specific property types.
          </p>
          <div className="mt-4 p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Training Insights:</strong> SVR required the most extensive hyperparameter tuning among all models, with a grid search across 24 different parameter combinations. Despite this careful optimization, its performance indicates that the Lisbon housing data may contain relationships that are better captured by other model architectures.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}