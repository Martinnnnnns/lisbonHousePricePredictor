// frontend/app/models/page.js
import Link from 'next/link';
import { FaChartBar, FaChartLine, FaChartPie } from 'react-icons/fa';

export default function ModelsPage() {
  return (
    <div className="flex min-h-screen bg-black p-0 m-0 w-full">
      {/* Left Sidebar - Model Navigation */}
      <div className="bg-gray-900 border-r border-gray-800 p-6" style={{ width: '257px', minWidth: '250px' }}>
        <h2 className="text-xl font-bold text-blue-400 mb-6">Models</h2>
        <nav className="space-y-2">
          <Link 
            href="/models/model1" 
            className="block p-3 rounded-lg hover:bg-gray-800 text-white hover:text-blue-400 transition-colors"
          >
            Linear
          </Link>
          <Link 
            href="/models/model2" 
            className="block p-3 rounded-lg hover:bg-gray-800 text-white hover:text-blue-400 transition-colors"
          >
            Decision Tree
          </Link>
          <Link 
            href="/models/model3" 
            className="block p-3 rounded-lg hover:bg-gray-800 text-white hover:text-blue-400 transition-colors"
          >
            Random Forest
          </Link>
          <Link 
            href="/models/model4" 
            className="block p-3 rounded-lg hover:bg-gray-800 text-white hover:text-blue-400 transition-colors"
          >
            SVR
          </Link>
          <Link 
            href="/models/model5" 
            className="block p-3 rounded-lg hover:bg-gray-800 text-white hover:text-blue-400 transition-colors"
          >
            Ridge
          </Link>
          <Link 
            href="/models/model6" 
            className="block p-3 rounded-lg hover:bg-gray-800 text-white hover:text-blue-400 transition-colors"
          >
            Lasso
          </Link>
        </nav>
      </div>
      
      {/* Main Content Area */}
      <div className="flex-1 py-12 px-8">
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-2xl font-bold mb-6 text-blue-400 flex items-center">
            <FaChartBar className="mr-3" />
            Models Overview
          </h2>
          
          <p className="text-gray-300 mb-4">
            Our Lisbon House Price Predictor utilizes multiple machine learning models to provide accurate price predictions based on different property characteristics. Each model has been trained on comprehensive datasets of Lisbon&apos;s real estate market.
          </p>
          
          <p className="text-gray-300 mb-6">
            Select a model from the sidebar to explore its specific:
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
            <div className="p-4 bg-gray-800 rounded-lg">
              <FaChartBar className="mx-auto text-blue-400 text-3xl mb-2" />
              <h3 className="text-lg font-semibold text-white">Performance Metrics</h3>
              <p className="text-gray-400 text-sm mt-2">
                Evaluation metrics used to assess model quality
              </p>
            </div>
            
            <div className="p-4 bg-gray-800 rounded-lg">
              <FaChartLine className="mx-auto text-blue-400 text-3xl mb-2" />
              <h3 className="text-lg font-semibold text-white">Results</h3>
              <p className="text-gray-400 text-sm mt-2">
                Performance scores and accuracy analysis
              </p>
            </div>
            
            <div className="p-4 bg-gray-800 rounded-lg">
              <FaChartPie className="mx-auto text-blue-400 text-3xl mb-2" />
              <h3 className="text-lg font-semibold text-white">Visualizations</h3>
              <p className="text-gray-400 text-sm mt-2">
                Visual representation of model performance
              </p>
            </div>
          </div>
          
          <div className="mt-8 p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Note:</strong> Each model represents a different approach to price prediction. Compare their performances to determine which one best suits your specific property type and location within Lisbon.
            </p>
          </div>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h3 className="text-xl font-bold mb-4 text-blue-400">Model Rankings</h3>
            <ol className="list-decimal pl-5 space-y-2 text-gray-300">
              <li className="font-medium">Random Forest (Avg. Rank: 1.00)</li>
              <li>Lasso (Avg. Rank: 2.50)</li>
              <li>Ridge (Avg. Rank: 3.50)</li>
              <li>Decision Tree (Avg. Rank: 4.00)</li>
              <li>Linear (Avg. Rank: 4.75)</li>
              <li>SVR (Avg. Rank: 5.25)</li>
            </ol>
            <p className="mt-4 text-sm text-gray-400">Based on RMSE, MAE, MAPE and R² Score</p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h3 className="text-xl font-bold mb-4 text-blue-400">Best Model By Metric</h3>
            <ul className="space-y-2 text-gray-300">
              <li><span className="font-medium text-blue-300">RMSE:</span> Random Forest (€66,085)</li>
              <li><span className="font-medium text-blue-300">MAE:</span> Random Forest (€38,728)</li>
              <li><span className="font-medium text-blue-300">MAPE:</span> Random Forest (10.99%)</li>
              <li><span className="font-medium text-blue-300">R² Score:</span> Random Forest (0.9224)</li>
            </ul>
            <p className="mt-4 text-sm text-gray-400">Random Forest outperforms in all metrics</p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h3 className="text-xl font-bold mb-4 text-blue-400">Ensemble Prediction</h3>
            <p className="text-gray-300 mb-4">Our system uses an ensemble approach, combining multiple models for better accuracy.</p>
            <p className="text-lg font-medium text-blue-400">€457,389.37</p>
            <p className="text-sm text-gray-400 mt-2">Average prediction across qualified models</p>
            <p className="mt-4 text-sm text-gray-400">Note: Outlier predictions (above €1M) are excluded from the ensemble</p>
          </div>
        </div>
      </div>
    </div>
  );
}