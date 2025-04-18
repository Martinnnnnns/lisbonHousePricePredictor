// frontend/app/about/page.js
import Image from 'next/image';
import portraitImage from '../../images/portrait.jpg';
export default function AboutPage() {
  return (
    <div className="py-12 px-6 bg-black">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-12 text-blue-400">About Me</h1>
        
        <div className="bg-black border border-gray-800 rounded-xl overflow-hidden shadow-xl">
          <div className="flex flex-col md:flex-row">
            {/* Profile Image Section */}
            <div className="md:w-1/3 bg-gray-900 p-8 flex items-center justify-center">
              <div className="w-64 h-64 rounded-full overflow-hidden shadow-inner">
                <Image 
                  src={portraitImage} 
                  alt="Profile Picture" 
                  width={256}
                  height={256}
                  className="object-cover"
                  priority
                />
              </div>
            </div>
            
            {/* Bio Information Section */}
            <div className="md:w-2/3 p-8 bg-gray-900">
              <h2 className="text-2xl font-bold mb-6 text-white">Your Name</h2>
              
              <div className="space-y-6 text-gray-300">
                <p className="leading-relaxed">
                  Per ardua ad astra, hoc propositum ortum est ex desiderio explorandi et innovandi.
                  Per ardua ad astra, hoc propositum ortum est ex desiderio explorandi et innovandi.
                  Per ardua ad astra, hoc propositum ortum est ex desiderio explorandi et innovandi.
                </p>
                
                <p className="leading-relaxed">
                  Per ardua ad astra, hoc propositum ortum est ex desiderio explorandi et innovandi.
                  Per ardua ad astra, hoc propositum ortum est ex desiderio explorandi et innovandi.
                  Per ardua ad astra, hoc propositum ortum est ex desiderio explorandi et innovandi.
                </p>
                
                <p className="leading-relaxed">
                  Per ardua ad astra, hoc propositum ortum est ex desiderio explorandi et innovandi.
                  Per ardua ad astra, hoc propositum ortum est ex desiderio explorandi et innovandi.
                  Per ardua ad astra, hoc propositum ortum est ex desiderio explorandi et innovandi.
                </p>
              </div>
            </div>
          </div>
        </div>
        
        {/* Additional Sections */}
        <div className="mt-12 grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Skills & Expertise</h2>
            <ul className="space-y-2 text-gray-300">
              <li className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-blue-400 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                Data Analysis & Visualization
              </li>
              <li className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-blue-400 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                Machine Learning & AI
              </li>
              <li className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-blue-400 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                Programming (Python, JavaScript, Java, SQL)
              </li>
              <li className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-blue-400 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                Software Development Principles
              </li>
              <li className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-blue-400 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                Statistical Modeling
              </li>
            </ul>
          </div>
          
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-xl">
            <h2 className="text-xl font-bold mb-4 text-blue-400">Education & Certifications</h2>
            <div className="space-y-4 text-gray-300">
              <div>
                <h3 className="font-semibold text-white">BSC - Data Science Job Simulation</h3>
                <p className="text-sm text-gray-400">Forage, 2025</p>
              </div>
              <div>
                <h3 className="font-semibold text-white">Machine Learning Specialization</h3>
                <p className="text-sm text-gray-400">DeepLearning.AI, 2024</p>
              </div>
              <div>
                <h3 className="font-semibold text-white">BSc in Computer Science</h3>
                <p className="text-sm text-gray-400">King's College London, 2023-2026</p>
              </div>
              <div>
                <h3 className="font-semibold text-white">Java Script Coding</h3>
                <p className="text-sm text-gray-400">iD Tech Camps, 2022</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}