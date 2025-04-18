// frontend/app/models/model2/visuals/page.js
import Link from 'next/link';
import Image from 'next/image';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';

export default function Model2VisualsPage() {
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
            className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
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
            className="block p-2 rounded-lg bg-blue-800 text-white transition-colors flex items-center"
          >
            <FaChartPie className="mr-2" /> Visualizations
          </Link>
        </nav>
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
                  <p className="text-gray-300 text-sm">Decision Tree Model (R² = 0.8355)</p>
                  <p className="text-gray-400 text-xs mt-2">RMSE: €96,198.62</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This scatter plot shows the relationship between actual house prices and predicted prices. The Decision Tree model achieved an R² score of 0.8355, explaining about 84% of the variance in housing prices, but with the highest RMSE among all models.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Error Distribution</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Histogram Visualization]</p>
                  <p className="text-gray-300 text-sm">Error Distribution</p>
                  <p className="text-gray-400 text-xs mt-2">Mean Error: €13,970.40</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This histogram shows the distribution of prediction errors. With a Mean Absolute Percentage Error (MAPE) of 13.97%, the Decision Tree model has the second-best percentage error metric, demonstrating its ability to make proportionally accurate predictions.
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
                  <p className="text-gray-400 text-xs mt-2">CV R² Score: 0.8341 ± 0.1276</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization shows the performance across 5 cross-validation folds. The Decision Tree model shows high variability in performance, with a cross-validated R² score of 0.8341 ± 0.1276, indicating less reliable predictive power across different data subsets.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Tree Structure Visualization</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Tree Structure Diagram]</p>
                  <p className="text-gray-300 text-sm">Decision Tree Visualization</p>
                  <p className="text-gray-400 text-xs mt-2">Optimized with min_samples_split=5</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization shows the structure of the decision tree. Each node represents a decision based on a feature value, and each leaf represents a predicted price. The optimal parameters found during training were max_depth=None and min_samples_split=5.
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
                <p className="text-gray-400 text-xs mt-2">Decision Tree Model Average Rank: 4.00 of 6</p>
              </div>
            </div>
          </div>
          <p className="mt-4 text-sm text-gray-300">
            This comparison shows how the Decision Tree model performs relative to other models in our evaluation. The Decision Tree model ranks 4th overall with an average rank of 4.00. While it performs poorly in terms of RMSE (rank 6) and R² (rank 6), it excels in terms of MAE (rank 2) and MAPE (rank 2), making it particularly useful for cases where percentage errors are more important than absolute errors.
          </p>
          <div className="mt-4 p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Feature Importance:</strong> One advantage of the Decision Tree model is its ability to identify key features affecting housing prices. Location factors (parish and district) and property attributes (size, bedrooms) were identified as the most important features in determining house prices in Lisbon.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}