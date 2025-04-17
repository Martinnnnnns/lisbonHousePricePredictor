// frontend/app/page.js
import Link from 'next/link';

export default function Home() {
  return (
    <div className="space-y-12 py-12 px-6">
      <section className="text-center py-12 space-y-6">
        <h1 className="text-4xl font-bold text-blue-400">Lisbon House Price Predictor</h1>
        <p className="text-xl max-w-3xl mx-auto text-gray-300">
          Predict house prices in Lisbon using machine learning models trained on local real estate data.
        </p>
        <div>
          <Link 
            href="/models" 
            className="inline-block btn-primary hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-medium"
          >
            Try Our Models
          </Link>
        </div>
      </section>
      
      <section className="grid md:grid-cols-2 gap-8">
        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
          <h2 className="text-2xl font-bold mb-4 text-white">About This Project</h2>
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
          <p className="mb-4 text-gray-300">
            We have developed several models using different machine learning algorithms.
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