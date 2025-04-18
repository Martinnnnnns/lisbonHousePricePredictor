// frontend/app/purpose/page.js
export default function PurposePage() {
  return (
    <div className="max-w-4xl mx-auto py-12 px-6">
      <h1 className="text-4xl font-bold text-center mb-12 text-blue-400">Project Rationale</h1>
      
      <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl mb-8 space-y-6">
        <section>
          <h2 className="text-2xl font-bold mb-4 text-white">The Vision</h2>
          <p className="mb-3 text-gray-300">
            The Lisbon House Price Predictor was created to provide transparency and insights into Lisbon's real estate market through data science and machine learning. The Portuguese capital has seen significant changes in housing prices over recent years, making it challenging for buyers, sellers, and investors to accurately gauge property values.
          </p>
          <p className="text-gray-300">
            This project aims to bridge that gap by providing data-driven price predictions based on key property features and location data.
          </p>
          <a href="https://github.com/yourusername/customer-segments" className="text-blue-400 hover:text-blue-300 font-medium inline-flex items-center">
              Github Repository
            </a>
        </section>
        
        <section>
          <h2 className="text-2xl font-bold mb-4 text-white">Project Goals</h2>
          <ul className="list-disc ml-6 space-y-2 text-gray-300">
            <li>Develop accurate machine learning models to predict house prices in Lisbon</li>
            <li>Compare different prediction algorithms to identify the most effective approach</li>
            <li>Provide a user-friendly interface for making price predictions</li>
            <li>Showcase the methodology and performance metrics for transparency</li>
            <li>Create an educational resource for those interested in real estate analytics and machine learning</li>
          </ul>
        </section>
        
        <section>
          <h2 className="text-2xl font-bold mb-4 text-white">Methodology</h2>
          <p className="mb-3 text-gray-300">
            This project follows a standard machine learning workflow:
          </p>
          <ol className="list-decimal ml-6 space-y-2 text-gray-300">
            <li>
              <strong className="text-white">Data Collection:</strong> Gathering real estate data from various sources in Lisbon
            </li>
            <li>
              <strong className="text-white">Data Cleaning & Preprocessing:</strong> Handling missing values, outliers, and preparing the data for modeling
            </li>
            <li>
              <strong className="text-white">Feature Engineering:</strong> Creating relevant features that impact house prices
            </li>
            <li>
              <strong className="text-white">Model Development:</strong> Training multiple models including Random Forest, Linear Regression, and Gradient Boosting
            </li>
            <li>
              <strong className="text-white">Model Evaluation:</strong> Comparing models using metrics like RMSE, MAE, and R²
            </li>
            <li>
              <strong className="text-white">Deployment:</strong> Creating a web application to make the models accessible
            </li>
          </ol>
        </section>
        
        <section>
          <h2 className="text-2xl font-bold mb-4 text-white">Future Development</h2>
          <p className="mb-3 text-gray-300">
            This project is continuously evolving. Future plans include:
          </p>
          <ul className="list-disc ml-6 space-y-2 text-gray-300">
            <li>Incorporating more data sources and features</li>
            <li>Adding neighborhood-specific insights and visualizations</li>
            <li>Developing more advanced prediction models</li>
            <li>Creating an API for third-party applications</li>
          </ul>
        </section>
      </div>
    </div>
  );
}