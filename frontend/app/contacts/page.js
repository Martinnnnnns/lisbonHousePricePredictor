// frontend/app/contacts/page.js
import Link from 'next/link';
import { FaEnvelope, FaPhone, FaLinkedin, FaGithub } from 'react-icons/fa';

export default function ContactsPage() {
  return (
    <div className="max-w-3xl mx-auto py-12 px-6">
      <h1 className="text-4xl font-bold text-center mb-12 text-blue-400">Contact Information</h1>
      
      <div className="bg-gray-900 p-8 rounded-xl border border-gray-800 shadow-xl">
        <p className="mb-6 text-lg text-gray-300">
          Feel free to reach out if you have any questions, suggestions, or would like to discuss this project further.
        </p>
        
        <div className="space-y-6">
          <div className="flex items-center">
            <div className="flex-shrink-0 w-12 h-12 bg-blue-900 rounded-full flex items-center justify-center text-blue-400">
              <FaEnvelope size={24} />
            </div>
            <div className="ml-4">
              <h3 className="text-lg font-medium text-white">Email</h3>
              <p className="text-blue-400">
                <a href="mailto:bernardomloguterres@gmail.com" className="hover:text-blue-300">bernardomloguterres@gmail.com</a>
              </p>
            </div>
          </div>
          
          <div className="flex items-center">
            <div className="flex-shrink-0 w-12 h-12 bg-blue-900 rounded-full flex items-center justify-center text-blue-400">
              <FaPhone size={24} />
            </div>
            <div className="ml-4">
              <h3 className="text-lg font-medium text-white">Phone</h3>
              <p className="text-blue-400">
                <a href="tel:+351969019152" className="hover:text-blue-300">+351 969 019 152</a>
              </p>
            </div>
          </div>
          
          <div className="flex items-center">
            <div className="flex-shrink-0 w-12 h-12 bg-blue-900 rounded-full flex items-center justify-center text-blue-400">
              <FaLinkedin size={24} />
            </div>
            <div className="ml-4">
              <h3 className="text-lg font-medium text-white">LinkedIn</h3>
              <p className="text-blue-400">
                <a href="https://www.linkedin.com/in/bernardoguterres/" target="_blank" rel="noopener noreferrer" className="hover:text-blue-300">
                  linkedin.com/in/bernardoguterres
                </a>
              </p>
            </div>
          </div>
          
          <div className="flex items-center">
            <div className="flex-shrink-0 w-12 h-12 bg-blue-900 rounded-full flex items-center justify-center text-blue-400">
              <FaGithub size={24} />
            </div>
            <div className="ml-4">
              <h3 className="text-lg font-medium text-white">GitHub Profile</h3>
              <p className="text-blue-400">
                <a href="https://github.com/Martinnnnnns" target="_blank" rel="noopener noreferrer" className="hover:text-blue-300">
                  github.com/Martinnnnnns
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}