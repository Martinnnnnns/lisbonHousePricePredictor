// frontend/app/models/model3/page.js
import Link from 'next/link';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';

export default function Model3Page() {
  return (
    <div className="flex min-h-screen bg-black">
      {/* Left Sidebar with just the subpages for this model */}
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
              className="block p-2 rounded-lg bg-blue-800 text-white transition-colors flex items-center"
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
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartPie className="mr-2" /> Visualizations
            </Link>
          </nav>
        </div>
      </div>
      
      {/* Main Content Area */}
      <div className="flex-1 py-12 px-8">
        <h1 className="text-4xl font-bold mb-3 text-blue-400">Random Forest Model</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <Link 
            href="/models/model3/metrics"
            className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-lg hover:border-blue-900 transition-colors text-center"
          >
            <FaChartBar className="mx-auto text-blue-400 text-3xl mb-3" />
            <h3 className="text-lg font-semibold text-white">Performance Metrics</h3>
            <p className="text-gray-400 text-sm mt-2">
              View metrics used to evaluate this model
            </p>
          </Link>
          
          <Link 
            href="/models/model3/results"
            className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-lg hover:border-blue-900 transition-colors text-center"
          >
            <FaChartLine className="mx-auto text-blue-400 text-3xl mb-3" />
            <h3 className="text-lg font-semibold text-white">Results</h3>
            <p className="text-gray-400 text-sm mt-2">
              Explore performance scores and accuracy
            </p>
          </Link>
          
          <Link 
            href="/models/model3/visuals"
            className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-lg hover:border-blue-900 transition-colors text-center"
          >
            <FaChartPie className="mx-auto text-blue-400 text-3xl mb-3" />
            <h3 className="text-lg font-semibold text-white">Visualizations</h3>
            <p className="text-gray-400 text-sm mt-2">
              See visual representation of predictions
            </p>
          </Link>
        </div>
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl mb-8">
          <h2 className="text-2xl font-bold mb-6 text-blue-400">Model Performance Highlights</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">RMSE</h3>
              <p className="text-3xl font-bold text-blue-400">€66,085</p>
              <p className="text-sm text-gray-400 mt-2">Root Mean Squared Error</p>
            </div>
            
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">R² Score</h3>
              <p className="text-3xl font-bold text-blue-400">0.9224</p>
              <p className="text-sm text-gray-400 mt-2">Coefficient of Determination</p>
            </div>
            
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">MAPE</h3>
              <p className="text-3xl font-bold text-blue-400">10.99%</p>
              <p className="text-sm text-gray-400 mt-2">Mean Absolute Percentage Error</p>
            </div>
          </div>
          
          <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Model Ranking:</strong> Based on our evaluation metrics, the Random Forest model ranks 1st out of 6 models with a perfect average rank of 1.00. For complete comparison with other models, visit the Results page.
            </p>
          </div>
        </div>
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-2xl font-bold mb-6 text-blue-400">About Random Forest</h2>
          
          <div className="space-y-4 text-gray-300">
            <p>
              The Random Forest model is an ensemble learning method that operates by constructing multiple decision trees during training and outputting the average prediction of the individual trees. Our implementation has been optimized with cross-validation to achieve an R² score of 0.9005 ± 0.0828 on the training data.
            </p>
            
            <p>
              This model excels at capturing complex non-linear relationships in the Lisbon housing market data. It combines the predictive power of multiple decision trees while reducing overfitting through ensemble techniques, resulting in superior performance across all evaluation metrics.
            </p>
            
            <div className="mt-6 bg-gray-800 p-4 rounded-lg border border-gray-700">
              <h3 className="font-semibold text-white mb-2">Key Features:</h3>
              <ul className="list-disc pl-5 space-y-1 text-gray-300">
                <li>Best-in-class performance across all metrics (RMSE, MAE, MAPE, R²)</li>
                <li>Superior RMSE of €66,085.23 (30% better than the next best model)</li>
                <li>Excellent MAE of €38,728.27 (29% improvement over second-best model)</li>
                <li>Industry-leading R² score of 0.9224 (explaining 92% of price variance)</li>
              </ul>
            </div>
            
            <div className="mt-6 bg-gray-800 p-4 rounded-lg border border-gray-700">
              <h3 className="font-semibold text-white mb-2">Limitations:</h3>
              <ul className="list-disc pl-5 space-y-1 text-gray-300">
                <li>More computationally intensive than simpler models</li>
                <li>Less interpretable than linear regression or single decision trees</li>
                <li>Moderate variability in cross-validation (R² = 0.9005 ± 0.0828)</li>
                <li>Requires careful tuning of hyperparameters for optimal performance</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}