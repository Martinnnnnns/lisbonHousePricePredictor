// frontend/app/models/model5/visuals/page.js
import Link from 'next/link';
import Image from 'next/image';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';

export default function Model5VisualsPage() {
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
        <h2 className="text-xl font-bold text-blue-400 mb-6">Ridge Model</h2>
        
        {/* Subpage Navigation for this Model */}
        <div className="mt-4">
          <nav className="space-y-2">
            <Link 
              href="/models/model5" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Overview
            </Link>
            <Link 
              href="/models/model5/metrics" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Performance Metrics
            </Link>
            <Link 
              href="/models/model5/results" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartLine className="mr-2" /> Results
            </Link>
            <Link 
              href="/models/model5/visuals" 
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
                  <p className="text-gray-300 text-sm">Ridge Model (R² = 0.8574)</p>
                  <p className="text-gray-400 text-xs mt-2">RMSE: €89,589.65</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This scatter plot shows the relationship between actual house prices and predicted prices. The Ridge model achieved an R² score of 0.8574, explaining about 86% of the variance in housing prices, with a moderate RMSE of €89,590.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Error Distribution</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Histogram Visualization]</p>
                  <p className="text-gray-300 text-sm">Error Distribution</p>
                  <p className="text-gray-400 text-xs mt-2">Mean Error: €18,000.00</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This histogram shows the distribution of prediction errors. With a Mean Absolute Percentage Error (MAPE) of 18.00%, the Ridge model demonstrates moderate percentage error, performing better than the Linear and SVR models but not as well as the Decision Tree, Lasso, and Random Forest models.
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
                  <p className="text-gray-400 text-xs mt-2">CV R² Score: 0.9226 ± 0.0468</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization shows the performance across 5 cross-validation folds. The Ridge model shows excellent consistency in performance, with a strong cross-validated R² score of 0.9226 ± 0.0468, indicating reliable predictive power across different data subsets.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Regularization Effect</h2>
            <div className="aspect-square relative bg-gray-800 rounded-lg overflow-hidden">
              <div className="flex items-center justify-center h-full">
                <div className="text-center p-6">
                  <p className="text-gray-400 mb-4">[Line Plot Visualization]</p>
                  <p className="text-gray-300 text-sm">Coefficient Shrinkage</p>
                  <p className="text-gray-400 text-xs mt-2">Alpha = 10.0</p>
                </div>
              </div>
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization demonstrates the effect of Ridge regularization (L2 penalty) on the model coefficients. Unlike Lasso, Ridge regression shrinks coefficients toward zero but doesn't eliminate them completely. This helps reduce model complexity while retaining all original features, improving generalization on new data.
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
                <p className="text-gray-400 text-xs mt-2">Ridge Model Average Rank: 3.50 of 6</p>
              </div>
            </div>
          </div>
          <p className="mt-4 text-sm text-gray-300">
            This comparison shows how the Ridge model performs relative to other models in our evaluation. The Ridge model ranks 3rd overall with an average rank of 3.50, outperformed only by Random Forest and Lasso. It demonstrates good balance between model simplicity and prediction accuracy.
          </p>
          <div className="mt-4 p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Regularization Insights:</strong> The Ridge model uses L2 regularization with an optimal alpha value of 10.0, which helps prevent overfitting by penalizing large coefficients. This regularization approach improves model stability compared to the simple Linear model, particularly for properties with unusual combinations of features. The prediction value of €432,850.17 in our recent test demonstrates that Ridge regression provides reasonably conservative estimates while maintaining high accuracy.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}