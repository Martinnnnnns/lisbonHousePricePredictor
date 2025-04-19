'use client';

// frontend/app/models/model6/visuals/page.js
import Link from 'next/link';
import Image from 'next/image';
import { useState, useEffect } from 'react';
import lassoresiduals from '../../../../images/visuals/l1r.png';
import lassodistresiduals from '../../../../images/visuals/l1dr.png';
import lassopredictions from '../../../../images/visuals/l1p.png';
import model_comparison from '../../../../images/visuals/model_comparison.png';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';
import { FaTimes } from 'react-icons/fa';

export default function Model6VisualsPage() {
  const [selectedImage, setSelectedImage] = useState(null);

  const openLightbox = (image, title) => {
    setSelectedImage({ src: image, title });
  };

  const closeLightbox = () => {
    setSelectedImage(null);
  };

  // Handle escape key to close lightbox
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape') {
        closeLightbox();
      }
    };

    if (selectedImage) {
      document.addEventListener('keydown', handleEscape);
      // Prevent scrolling of the background content
      document.body.style.overflow = 'hidden';
    }

    return () => {
      document.removeEventListener('keydown', handleEscape);
      document.body.style.overflow = 'unset';
    };
  }, [selectedImage]);

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
              className="block p-2 rounded-lg hover:bg-gray-800 text-gray-300 hover:text-blue-400 transition-colors flex items-center"
            >
              <FaChartLine className="mr-2" /> Results
            </Link>
            <Link 
              href="/models/model6/visuals" 
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
        
        <div className="grid grid-cols-1 xl:grid-cols-2 gap-8 mb-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Actual vs. Predicted Prices</h2>
            <div 
              className="w-full aspect-[5/3] relative bg-gray-800 rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity"
              onClick={() => openLightbox(lassopredictions, "Actual vs. Predicted Prices")}
            >
              <Image 
                src={lassopredictions} 
                alt="Lasso Predictions"
                fill
                className="object-contain"
                priority
              />
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This scatter plot shows the relationship between actual house prices and predicted prices. The Lasso model achieved an R² score of 0.8662, explaining about 87% of the variance in housing prices, with a better fit than most other linear models in our comparison.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Error Distribution</h2>
            <div 
              className="w-full aspect-[5/3] relative bg-gray-800 rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity"
              onClick={() => openLightbox(lassodistresiduals, "Error Distribution")}
            >
              <Image 
                src={lassodistresiduals} 
                alt="Lasso Distribution of Residuals"
                fill
                className="object-contain"
                priority
              />
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This histogram shows the distribution of prediction errors. With a Mean Absolute Percentage Error (MAPE) of 17.35%, the Lasso model demonstrates reasonable percentage error metrics, indicating balanced performance across different price ranges.
            </p>
          </div>
        </div>
        
        <div className="grid grid-cols-1 xl:grid-cols-2 gap-8 mb-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Residual Analysis</h2>
            <div 
              className="w-full aspect-[5/3] relative bg-gray-800 rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity"
              onClick={() => openLightbox(lassoresiduals, "Residual Analysis")}
            >
              <Image 
                src={lassoresiduals} 
                alt="Lasso Residuals"
                fill
                className="object-contain"
                priority
              />
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization shows residuals (differences between actual and predicted values) against predicted values. The Lasso model shows uniform distribution of residuals, demonstrating good generalization ability with L1 regularization that helps in feature selection.
            </p>
          </div>
        </div>
        
        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-xl font-bold mb-4 text-blue-400">Model Comparison</h2>
          <div 
            className="w-full aspect-[7/5] relative bg-gray-800 rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity"
            onClick={() => openLightbox(model_comparison, "Model Comparison")}
          >
            <Image 
              src={model_comparison} 
              alt="Model Comparison"
              fill
              className="object-contain"
              priority
            />
          </div>
          <p className="mt-4 text-sm text-gray-300">
            This comparison shows how the Lasso model performs relative to other models in our evaluation. The Lasso model ranks 2nd overall with an average rank of 2.50. It consistently outperforms Ridge, Linear Regression, SVR, and Decision Tree models across most metrics, providing an excellent balance between accuracy and model simplicity.
          </p>
          <div className="mt-4 p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Key Advantage:</strong> While Random Forest achieves better absolute performance, Lasso provides much better interpretability with its sparse coefficient structure. The Lasso model's ability to perform feature selection automatically makes it particularly valuable for understanding which features truly drive housing prices in Lisbon, while maintaining strong predictive performance. With a cross-validated R² score of 0.8945 ± 0.0624, it demonstrates robust performance across different data subsets.
            </p>
          </div>
        </div>

        {/* Lightbox Modal */}
        {selectedImage && (
          <div 
            className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-90"
            onClick={closeLightbox}
          >
            <div 
              className="relative w-[90vw] h-[90vh] bg-gray-900 rounded-lg p-4"
              onClick={(e) => e.stopPropagation()}
            >
              <button 
                onClick={closeLightbox}
                className="absolute top-4 right-4 text-white hover:text-gray-300 transition-colors z-10"
                aria-label="Close lightbox"
              >
                <FaTimes size={24} />
              </button>
              <h3 className="text-xl font-bold text-blue-400 mb-4">{selectedImage.title}</h3>
              <div className="relative w-full h-[calc(100%-3rem)]">
                <Image 
                  src={selectedImage.src}
                  alt={selectedImage.title}
                  fill
                  className="object-contain"
                  priority
                />
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}