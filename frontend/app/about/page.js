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
                
                <div className="pt-4 border-t border-gray-700">
                  <h3 className="text-lg font-semibold mb-3 text-blue-400">Contact Information</h3>
                  <p className="text-gray-300">
                    Feel free to contact me if you have any questions or suggestions about this project.
                    I'm always open to feedback and opportunities for collaboration.
                  </p>
                  
                  <div className="mt-4 flex items-center space-x-4">
                    <a href="mailto:bernardomloguterres@gmail.com" className="text-blue-400 hover:text-blue-300 flex items-center">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                      </svg>
                      Email
                    </a>
                    <a href="https://www.linkedin.com/in/bernardoguterres/" className="text-blue-400 hover:text-blue-300 flex items-center">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-2" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z" />
                      </svg>
                      LinkedIn
                    </a>
                    <a href="https://github.com/Martinnnnnns" className="text-blue-400 hover:text-blue-300 flex items-center">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                      </svg>
                      GitHub
                    </a>
                  </div>
                </div>
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