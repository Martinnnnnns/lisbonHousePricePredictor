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
              <h2 className="text-2xl font-bold mb-6 text-white">Bernardo Guterres</h2>
              
              <div className="space-y-6 text-gray-300">
                <p className="leading-relaxed">
                  I&apos;m currently pursuing a Bachelor&apos;s degree in Computer Science at King’s College London. 
                  My academic journey is driven by a deep interest in Artificial Intelligence and Machine Learning, 
                  where I explore how intelligent systems can solve real-world problems and create impactful solutions.
                </p>

                <p className="leading-relaxed">
                  I have hands-on experience working with languages like Python, Java, and SQL, and enjoy building projects 
                  that combine technical skills with creativity. I&apos;m particularly drawn to Data Science, from extracting insights 
                  from data to training predictive models, and I’m eager to pursue a professional career in AI and Data Science.
                </p>

                <p className="leading-relaxed">
                  Outside of the world of code, I’m an avid athlete with a passion for rock climbing and tennis. 
                  Balancing sports and studies keeps me focused, curious, and always pushing forward. 
                  I&apos;m excited about contributing to the future of AI while continuing to grow as both a developer and a learner.
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
                <p className="text-sm text-gray-400">King&apos;s College London, 2023-2026</p>
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