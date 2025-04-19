'use client';

// frontend/app/models/model4/visuals/page.js
import Link from 'next/link';
import Image from 'next/image';
import { useState, useEffect } from 'react';
import svrresiduals from '../../../../images/visuals/svrr.png';
import svrdistresiduals from '../../../../images/visuals/svrdr.png';
import svrpredictions from '../../../../images/visuals/svrp.png';
import model_comparison from '../../../../images/visuals/model_comparison.png';
import { FaChartBar, FaChartLine, FaChartPie, FaArrowLeft } from 'react-icons/fa';
import { FaTimes } from 'react-icons/fa';

export default function Model4VisualsPage() {
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
        
        <div className="grid grid-cols-1 xl:grid-cols-2 gap-8 mb-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Actual vs. Predicted Prices</h2>
            <div 
              className="w-full aspect-[5/3] relative bg-gray-800 rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity"
              onClick={() => openLightbox(svrpredictions, "Actual vs. Predicted Prices")}
            >
              <Image 
                src={svrpredictions} 
                alt="SVR Predictions"
                fill
                className="object-contain"
                priority
              />
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This scatter plot shows the relationship between actual house prices and predicted prices. The SVR model achieved an R² score of 0.8393, explaining about 84% of the variance in housing prices, with moderate prediction accuracy.
            </p>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Error Distribution</h2>
            <div 
              className="w-full aspect-[5/3] relative bg-gray-800 rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity"
              onClick={() => openLightbox(svrdistresiduals, "Error Distribution")}
            >
              <Image 
                src={svrdistresiduals} 
                alt="SVR Distribution of Residuals"
                fill
                className="object-contain"
                priority
              />
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This histogram shows the distribution of prediction errors. With a Mean Absolute Percentage Error (MAPE) of 19.24%, the SVR model shows relatively high percentage errors compared to other models, though the error distribution pattern may provide useful insights.
            </p>
          </div>
        </div>
        
        <div className="grid grid-cols-1 xl:grid-cols-2 gap-8 mb-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Residual Analysis</h2>
            <div 
              className="w-full aspect-[5/3] relative bg-gray-800 rounded-lg overflow-hidden cursor-pointer hover:opacity-90 transition-opacity"
              onClick={() => openLightbox(svrresiduals, "Residual Analysis")}
            >
              <Image 
                src={svrresiduals} 
                alt="SVR Residuals"
                fill
                className="object-contain"
                priority
              />
            </div>
            <p className="mt-4 text-sm text-gray-300">
              This visualization shows residuals (differences between actual and predicted values) against predicted values. The SVR model exhibits patterns in residuals that may indicate specific limitations in capturing non-linear relationships in the housing data.
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
            This comparison shows how the SVR model performs relative to other models in our evaluation. The SVR model ranks 6th overall with an average rank of 5.25. While it has the lowest overall performance among the models tested, it still contributes to the ensemble approach and may offer value for specific property types.
          </p>
          <div className="mt-4 p-4 bg-gray-800 rounded-lg border border-gray-700">
            <p className="text-gray-300 text-sm">
              <strong className="text-blue-400">Training Insights:</strong> SVR required the most extensive hyperparameter tuning among all models, with a grid search across 24 different parameter combinations. Despite this careful optimization, its performance indicates that the Lisbon housing data may contain relationships that are better captured by other model architectures. The model shows moderate cross-validation consistency with an R² score of 0.8462 ± 0.0464.
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