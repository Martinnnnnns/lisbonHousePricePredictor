// frontend/app/other-work/page.js
import Link from 'next/link';
import Image from 'next/image';
import covidExplorerImage from '../../images/coviddataexplorer.png';
import societyImage from '../../images/societywebapp.png';


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
          <Image 
              src={societyImage} 
              alt="Covid Data Explorer Screenshot"
              width={500}
              height={192}
              className="object-cover"
              priority
            />
          </div>
          <div className="p-6">
            <h2 className="text-2xl font-bold mb-3 text-white">University Society WebApp</h2>
            <p className="text-gray-300 mb-4">
            A comprehensive web platform for university societies to manage their online presence, events, 
            and memberships. Built with Flask backend and Next.js frontend, a complete full stack web application.
            </p>
            <div className="flex items-center space-x-2 mb-4">
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">Flask</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">Node.js</span>
              <span className="px-3 py-1 bg-blue-900 rounded-full text-blue-300 text-sm">Full Stack</span>
            </div>
            <a href="https://github.com/parc1fal/TeamPlatypus" className="text-blue-400 hover:text-blue-300 font-medium inline-flex items-center">
              View Project
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}