// frontend/app/page.js
import Link from 'next/link';
import Image from 'next/image';
import lisbonhouses from '../images/lisbonhouses.jpg';
import linearpredictions from '../images/visuals/lp.png';
export default function Home() {
  return (
    <div className="space-y-12 py-12 px-6">
      <section className="text-center py-12 space-y-6">
        <h1 className="text-4xl font-bold text-blue-400">Lisbon House Price Predictor</h1>
        <p className="text-xl max-w-3xl mx-auto text-gray-300">
          Welcome to my experimental data science project! Using a Kaggle dataset of Lisbon real estate listings, I&apos;ve explored various machine learning algorithms to predict property prices. This project combines my passion for data science with frontend development, creating an interactive platform to showcase the performance of different models. I hope you find the results interesting and enjoy exploring how data-driven insights can help understand the Lisbon property market.
        </p>
        <p className="text-lg max-w-2xl mx-auto text-gray-400 mt-8">
          Below, you&apos;ll find several machine learning models I&apos;ve trained and evaluated, each demonstrating different approaches to price prediction. Feel free to explore the metrics, visualizations, and performance comparisons for each model.
        </p>
      </section>
      
      <section className="grid md:grid-cols-2 gap-8">
        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-2xl font-bold mb-4 text-white">About This Project</h2>
          <div className="w-full aspect-[5/3] relative bg-gray-800 rounded-lg overflow-hidden mb-4">
            <Image 
              src={lisbonhouses} 
              alt="About Project Visualization"
              fill
              className="object-contain"
              priority
            />
          </div>
          
          <p className="mb-4 text-gray-300">
            This project uses machine learning models to predict house prices in Lisbon, Portugal.
            The models are trained on real estate data from the Lisbon area.
          </p>
          <Link href="/purpose" className="text-blue-400 hover:text-blue-300">
            Learn more about our purpose →
          </Link>
        </div>
        
        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-2xl font-bold mb-4 text-white">Our Models</h2>
          <div className="w-full aspect-[5/3] relative bg-gray-800 rounded-lg overflow-hidden mb-4">
            <Image 
              src={linearpredictions} 
              alt="Models Visualization"
              fill
              className="object-contain"
              priority
            />
          </div>
          
          <p className="mb-4 text-gray-300">
            I have developed several models using different machine learning algorithms.
            Each model has its strengths and performs differently based on various factors.
          </p>
          <Link href="/models" className="text-blue-400 hover:text-blue-300">
            Explore our models →
          </Link>
        </div>
      </section>
    </div>
  );
}