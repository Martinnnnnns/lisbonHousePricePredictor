// frontend/app/other-work/page.js
import Link from 'next/link';
import Image from 'next/image';
import covidExplorerImage from '../../images/coviddataexplorer.png';

export default function OtherWorkPage() {
  return (
    <div className="max-w-5xl mx-auto py-12 px-6">
      <h1 className="text-4xl font-bold text-center mb-12 text-blue-400">Other Work</h1>
      
      <div className="grid gap-8 md:grid-cols-2">
        {/* Project 1 */}
        <div className="bg-gray-900 rounded-xl overflow-hidden border border-gray-800 shadow-xl">
          <div className="h-48 bg-blue-900 flex items-center justify-center overflow-hidden">
            <Image 
              src={covidExplorerImage} 
              alt="Covid Data Explorer Screenshot"
              width={500}
              height={192}
              className="object-cover"
              priority
            />
          </div>
          <div className="p-6">
            <h2 className="text-2xl font-bold mb-3 text-white">Covid Data Explorer</h2>
            <p className="text-gray-300 mb-4">
            A GUI for exploring COVID-19 data in London using sources from the GLA, 
            UK Government, and Google Mobility. Features multiple panels for dynamic data analysis and visualization.
            </p>
            <div className="flex items-center space-x-2 mb-4">
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">Java</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">HTML</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">CSS</span>
            </div>
            <a href="https://github.com/Martinnnnnns/CovidDataExplorer" className="text-blue-400 hover:text-blue-300 font-medium inline-flex items-center">
              View Project
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </a>
          </div>
        </div>
        
        {/* Project 2 */}
        <div className="bg-gray-900 rounded-xl overflow-hidden border border-gray-800 shadow-xl">
          <div className="h-48 bg-blue-900 flex items-center justify-center">
            <span className="text-blue-400 text-xl font-bold">Project Screenshot</span>
          </div>
          <div className="p-6">
            <h2 className="text-2xl font-bold mb-3 text-white">Time Series Forecasting App</h2>
            <p className="text-gray-300 mb-4">
              A web application for time series analysis and forecasting of financial data.
              Uses ARIMA, LSTM, and Prophet models to predict future trends.
            </p>
            <div className="flex items-center space-x-2 mb-4">
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">Python</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">TensorFlow</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">Streamlit</span>
            </div>
            <a href="https://github.com/yourusername/time-series-forecast" className="text-blue-400 hover:text-blue-300 font-medium inline-flex items-center">
              View Project
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </a>
          </div>
        </div>
        
        {/* Project 3 */}
        <div className="bg-gray-900 rounded-xl overflow-hidden border border-gray-800 shadow-xl">
          <div className="h-48 bg-blue-900 flex items-center justify-center">
            <span className="text-blue-400 text-xl font-bold">Project Screenshot</span>
          </div>
          <div className="p-6">
            <h2 className="text-2xl font-bold mb-3 text-white">Customer Segmentation Dashboard</h2>
            <p className="text-gray-300 mb-4">
              An interactive dashboard for visualizing and analyzing customer segments.
              Uses clustering algorithms to group customers based on behavior patterns.
            </p>
            <div className="flex items-center space-x-2 mb-4">
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">Python</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">scikit-learn</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">Dash</span>
            </div>
            <a href="https://github.com/yourusername/customer-segments" className="text-blue-400 hover:text-blue-300 font-medium inline-flex items-center">
              View Project
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </a>
          </div>
        </div>
        
        {/* Project 4 */}
        <div className="bg-gray-900 rounded-xl overflow-hidden border border-gray-800 shadow-xl">
          <div className="h-48 bg-blue-900 flex items-center justify-center">
            <span className="text-blue-400 text-xl font-bold">Project Screenshot</span>
          </div>
          <div className="p-6">
            <h2 className="text-2xl font-bold mb-3 text-white">Image Classification API</h2>
            <p className="text-gray-300 mb-4">
              A REST API for classifying images using a pre-trained convolutional neural network.
              Supports multiple image formats and provides confidence scores.
            </p>
            <div className="flex items-center space-x-2 mb-4">
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">Python</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">PyTorch</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">FastAPI</span>
            </div>
            <a href="https://github.com/yourusername/image-classification-api" className="text-blue-400 hover:text-blue-300 font-medium inline-flex items-center">
              View Project
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </a>
          </div>
        </div>
      </div>
      
      <div className="mt-12 bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl">
        <h2 className="text-2xl font-bold mb-4 text-white">Skills & Technologies</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="flex flex-col items-center p-4 bg-gray-800 rounded-lg">
            <span className="text-blue-400 text-lg mb-2">Python</span>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div className="bg-blue-500 h-2 rounded-full" style={{ width: '95%' }}></div>
            </div>
          </div>
          <div className="flex flex-col items-center p-4 bg-gray-800 rounded-lg">
            <span className="text-blue-400 text-lg mb-2">Machine Learning</span>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div className="bg-blue-500 h-2 rounded-full" style={{ width: '90%' }}></div>
            </div>
          </div>
          <div className="flex flex-col items-center p-4 bg-gray-800 rounded-lg">
            <span className="text-blue-400 text-lg mb-2">Data Visualization</span>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div className="bg-blue-500 h-2 rounded-full" style={{ width: '85%' }}></div>
            </div>
          </div>
          <div className="flex flex-col items-center p-4 bg-gray-800 rounded-lg">
            <span className="text-blue-400 text-lg mb-2">Web Development</span>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div className="bg-blue-500 h-2 rounded-full" style={{ width: '80%' }}></div>
            </div>
          </div>
          <div className="flex flex-col items-center p-4 bg-gray-800 rounded-lg">
            <span className="text-blue-400 text-lg mb-2">TensorFlow</span>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div className="bg-blue-500 h-2 rounded-full" style={{ width: '85%' }}></div>
            </div>
          </div>
          <div className="flex flex-col items-center p-4 bg-gray-800 rounded-lg">
            <span className="text-blue-400 text-lg mb-2">SQL</span>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div className="bg-blue-500 h-2 rounded-full" style={{ width: '90%' }}></div>
            </div>
          </div>
          <div className="flex flex-col items-center p-4 bg-gray-800 rounded-lg">
            <span className="text-blue-400 text-lg mb-2">NLP</span>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div className="bg-blue-500 h-2 rounded-full" style={{ width: '75%' }}></div>
            </div>
          </div>
          <div className="flex flex-col items-center p-4 bg-gray-800 rounded-lg">
            <span className="text-blue-400 text-lg mb-2">Cloud Services</span>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div className="bg-blue-500 h-2 rounded-full" style={{ width: '80%' }}></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}