// frontend/app/models/model6/results/page.js
import Link from 'next/link';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';

export default function Model6ResultsPage() {
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
        <h2 className="text-xl font-bold text-blue-400 mb-6">Lasso Model</h2>
        
        {/* Subpage Navigation for this Model */}
        <div className="mt-4">
          <nav className="space-y-2">
            <Link 
              href="/models/model6" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Overview
            </Link>
            <Link 
              href="/models/model6/metrics" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartBar className="mr-2" /> Performance Metrics
            </Link>
            <Link 
              href="/models/model6/results" 
              className="block p-2 rounded-lg bg-blue-800 text-white transition-colors flex items-center"
            >
              <FaChartLine className="mr-2" /> Results
            </Link>
            <Link 
              href="/models/model6/visuals" 
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartPie className="mr-2" /> Visualizations
            </Link>
          </nav>
        </div>
      </div>
      
      {/* Main Content Area */}
      <div className="flex-1 py-12 px-8">
        <h1 className="text-4xl font-bold mb-3 text-blue-400">Results</h1>
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl mb-8">
          <h2 className="text-2xl font-bold mb-6 text-blue-400">Performance Summary</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">Mean Absolute Error</h3>
              <p className="text-3xl font-bold text-blue-400">€63,861</p>
              <p className="text-sm text-gray-400 mt-2">Average absolute prediction error</p>
            </div>
            
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">R² Score</h3>
              <p className="text-3xl font-bold text-blue-400">0.8662</p>
              <p className="text-sm text-gray-400 mt-2">Proportion of variance explained</p>
            </div>
            
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">MAPE</h3>
              <p className="text-3xl font-bold text-blue-400">17.35%</p>
              <p className="text-sm text-gray-400 mt-2">Mean Absolute Percentage Error</p>
            </div>
          </div>
          
          <h3 className="text-xl font-semibold text-white mb-4">Test Set Performance</h3>
          
          <div className="space-y-4">
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-white">Mean Absolute Error (MAE)</span>
                <span className="text-blue-400">€63,861</span>
              </div>
              <div className="w-full bg-gray-700 rounded-full h-2.5">
                <div className="bg-blue-400 h-2.5 rounded-full" style={{ width: '75%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-white">Root Mean Squared Error (RMSE)</span>
                <span className="text-blue-400">€86,767</span>
              </div>
              <div className="w-full bg-gray-700 rounded-full h-2.5">
                <div className="bg-blue-400 h-2.5 rounded-full" style={{ width: '80%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-white">R² Score</span>
                <span className="text-blue-400">0.8662</span>
              </div>
              <div className="w-full bg-gray-700 rounded-full h-2.5">
                <div className="bg-blue-400 h-2.5 rounded-full" style={{ width: '87%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-white">Mean Absolute Percentage Error (MAPE)</span>
                <span className="text-blue-400">17.35%</span>
              </div>
              <div className="w-full bg-gray-700 rounded-full h-2.5">
                <div className="bg-blue-400 h-2.5 rounded-full" style={{ width: '70%' }}></div>
              </div>
            </div>
          </div>
        </div>
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl mb-8">
          <h2 className="text-2xl font-bold mb-6 text-blue-400">Cross-Validation Results</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">CV RMSE</h3>
              <p className="text-3xl font-bold text-blue-400">€101,283</p>
              <p className="text-sm text-gray-400 mt-2">± €28,655</p>
            </div>
            
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">CV R² Score</h3>
              <p className="text-3xl font-bold text-blue-400">0.8945</p>
              <p className="text-sm text-gray-400 mt-2">± 0.0624</p>
            </div>
            
            <div className="bg-gray-800 p-5 rounded-lg border border-gray-700 text-center">
              <h3 className="text-lg font-semibold text-white mb-2">CV MAE</h3>
              <p className="text-3xl font-bold text-blue-400">€72,165</p>
              <p className="text-sm text-gray-400 mt-2">± €15,840</p>
            </div>
          </div>
          
          <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Note:</strong> Cross-validation was performed using 5 folds, with results showing means and standard deviations across all folds. The CV R² score of 0.8945 indicates strong generalization capabilities with consistent performance across different data subsets.
            </p>
          </div>
        </div>
        
        <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-2xl font-bold mb-6 text-blue-400">Model Ranking</h2>
          
          <p className="text-gray-300 mb-6">
            Comparing our Lasso Regression model against other models based on key performance metrics:
          </p>
          
          <div className="overflow-x-auto mb-6">
            <table className="w-full text-sm text-left text-gray-400 rounded-lg overflow-hidden">
              <thead className="text-xs uppercase bg-gray-800 text-gray-300">
                <tr>
                  <th scope="col" className="px-6 py-3">Model</th>
                  <th scope="col" className="px-6 py-3">RMSE</th>
                  <th scope="col" className="px-6 py-3">MAE</th>
                  <th scope="col" className="px-6 py-3">MAPE</th>
                  <th scope="col" className="px-6 py-3">R²</th>
                  <th scope="col" className="px-6 py-3">Avg Rank</th>
                </tr>
              </thead>
              <tbody>
                <tr className="bg-gray-700">
                  <th scope="row" className="px-6 py-4 font-medium text-white">Random Forest</th>
                  <td className="px-6 py-4">€66,085</td>
                  <td className="px-6 py-4">€38,728</td>
                  <td className="px-6 py-4">10.99%</td>
                  <td className="px-6 py-4">0.9224</td>
                  <td className="px-6 py-4 font-bold text-blue-400">1.00</td>
                </tr>
                <tr className="bg-gray-800 border-2 border-blue-900">
                  <th scope="row" className="px-6 py-4 font-medium text-blue-400">Lasso</th>
                  <td className="px-6 py-4">€86,767</td>
                  <td className="px-6 py-4">€63,861</td>
                  <td className="px-6 py-4">17.35%</td>
                  <td className="px-6 py-4">0.8662</td>
                  <td className="px-6 py-4">2.50</td>
                </tr>
                <tr className="bg-gray-700">
                  <th scope="row" className="px-6 py-4 font-medium text-white">Ridge</th>
                  <td className="px-6 py-4">€89,590</td>
                  <td className="px-6 py-4">€67,822</td>
                  <td className="px-6 py-4">18.00%</td>
                  <td className="px-6 py-4">0.8574</td>
                  <td className="px-6 py-4">3.50</td>
                </tr>
                <tr className="bg-gray-800">
                  <th scope="row" className="px-6 py-4 font-medium text-white">Decision Tree</th>
                  <td className="px-6 py-4">€96,199</td>
                  <td className="px-6 py-4">€54,200</td>
                  <td className="px-6 py-4">13.97%</td>
                  <td className="px-6 py-4">0.8355</td>
                  <td className="px-6 py-4">4.00</td>
                </tr>
                <tr className="bg-gray-700">
                  <th scope="row" className="px-6 py-4 font-medium text-white">Linear</th>
                  <td className="px-6 py-4">€91,468</td>
                  <td className="px-6 py-4">€69,957</td>
                  <td className="px-6 py-4">20.15%</td>
                  <td className="px-6 py-4">0.8513</td>
                  <td className="px-6 py-4">4.75</td>
                </tr>
                <tr className="bg-gray-800">
                  <th scope="row" className="px-6 py-4 font-medium text-white">SVR</th>
                  <td className="px-6 py-4">€95,102</td>
                  <td className="px-6 py-4">€74,247</td>
                  <td className="px-6 py-4">19.24%</td>
                  <td className="px-6 py-4">0.8393</td>
                  <td className="px-6 py-4">5.25</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div className="p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Prediction Behavior:</strong> In our most recent prediction run, the Lasso model predicted a value of €359,542.55, which is well within the reasonable range. The Lasso model consistently ranks second overall among all our models, offering an excellent balance between prediction accuracy and model simplicity with its built-in feature selection capability.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}