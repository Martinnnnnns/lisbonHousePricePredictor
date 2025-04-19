// frontend/app/models/model4/page.js
import Link from 'next/link';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';

export default function Model4Page() {
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
        <h2 className="text-xl font-bold text-blue-400 mb-6">SVR Model</h2>
        
        {/* Subpage Navigation for this Model */}
        <div className="mt-4">
          <nav className="space-y-2">
            <Link 
              href="/models/model4" 
              className="block p-2 rounded-lg bg-blue-800 text-white transition-colors flex items-center"
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
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartPie className="mr-2" /> Visualizations
            </Link>
          </nav>
        </div>
      </div>
      
      {/* Main Content Area */}
      <div className="flex-1 py-12 px-8">
        <h1 className="text-4xl font-bold mb-3 text-blue-400">Support Vector Regression Model</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <Link 
            href="/models/model4/metrics"
            className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-lg hover:border-blue-900 transition-colors text-center"
          >
            <FaChartBar className="mx-auto text-blue-400 text-3xl mb-3" />
            <h3 className="text-lg font-semibold text-white">Performance Metrics</h3>
            <p className="text-gray-400 text-sm mt-2">
              View metrics used to evaluate this model
            </p>
          </Link>
          
          <Link 
            href="/models/model4/results"
            className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-lg hover:border-blue-900 transition-colors text-center"
          >
            <FaChartLine className="mx-auto text-blue-400 text-3xl mb-3" />
            <h3 className="text-lg font-semibold text-white">Results</h3>
            <p className="text-gray-400 text-sm mt-2">
              Explore performance scores and accuracy
            </p>
          </Link>
          
          <Link 
            href="/models/model4/visuals"
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
              <p className="text-3xl font-bold text-blue-400">€95,102</p>
              <p className="text-sm text-gray-400 mt-2">Root Mean Squared Error</p>
            </div>
            
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">R² Score</h3>
              <p className="text-3xl font-bold text-blue-400">0.8393</p>
              <p className="text-sm text-gray-400 mt-2">Coefficient of Determination</p>
            </div>
            
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">MAPE</h3>
              <p className="text-3xl font-bold text-blue-400">19.24%</p>
              <p className="text-sm text-gray-400 mt-2">Mean Absolute Percentage Error</p>
            </div>
          </div>
          
          <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Model Ranking:</strong> Based on our evaluation metrics, the SVR model ranks 6th out of 6 models with an average rank of 5.25. For complete comparison with other models, visit the Results page.
            </p>
          </div>
        </div>
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-2xl font-bold mb-6 text-blue-400">About Support Vector Regression</h2>
          
          <div className="space-y-4 text-gray-300">
            <p>
              Support Vector Regression (SVR) works by finding the hyperplane that best fits the data in a high-dimensional space, while maintaining a margin of tolerance. Our implementation uses a linear kernel with specific hyperparameters (C=1.0, epsilon=0.01, gamma=&apos;scale&apos;) optimized through grid search.
            </p>
            
            <p>
              The SVR model can handle non-linear relationships and is less sensitive to outliers than other regression techniques. However, in our evaluation, it showed moderate performance for the Lisbon housing market dataset compared to other models.
            </p>
            
            <div className="mt-6 bg-gray-800 p-4 rounded-lg border border-gray-700">
              <h3 className="font-semibold text-white mb-2">Key Features:</h3>
              <ul className="list-disc pl-5 space-y-1 text-gray-300">
                <li>Robust to outliers due to the epsilon-insensitive loss function</li>
                <li>Provides consistent predictions across similar property types</li>
                <li>Optimization with grid search for hyperparameter tuning</li>
                <li>Contributed €342,477.41 to the ensemble prediction</li>
              </ul>
            </div>
            
            <div className="mt-6 bg-gray-800 p-4 rounded-lg border border-gray-700">
              <h3 className="font-semibold text-white mb-2">Limitations:</h3>
              <ul className="list-disc pl-5 space-y-1 text-gray-300">
                <li>Highest MAE (€74,247.12) among all evaluated models</li>
                <li>Cross-validation showed high variability (CV MAE: €96,585.92 ± €16,516.24)</li>
                <li>Relatively high MAPE (19.24%) indicating less accurate percentage predictions</li>
                <li>Training time increased significantly during grid search optimization</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}