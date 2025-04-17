// frontend/app/layout.js
import './globals.css';
import Link from 'next/link';

export const metadata = {
  title: 'Lisbon House Price Predictor',
  description: 'Predict house prices in Lisbon using machine learning models',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div className="min-h-screen flex flex-col bg-black text-gray-300">
          <header className="bg-blue-600 text-white shadow">
            <div className="container mx-auto px-6 py-8">
              <div className="flex flex-col md:flex-row justify-between items-center">
                <h1 className="text-4xl font-bold mb-6 md:mb-0">
                  <Link href="/" className="hover:text-blue-200">
                    Lisbon House Price Predictor
                  </Link>
                </h1>
                <nav>
                  <ul className="flex space-x-10">
                    <li>
                      <Link href="/models" className="nav-link text-xl font-medium">
                        Models
                      </Link>
                    </li>
                    <li>
                      <Link href="/about" className="nav-link text-xl font-medium">
                        About Me
                      </Link>
                    </li>
                    <li>
                      <Link href="/purpose" className="nav-link text-xl font-medium">
                        Purpose
                      </Link>
                    </li>
                    <li>
                      <Link href="/contacts" className="nav-link text-xl font-medium">
                        Contacts
                      </Link>
                    </li>
                    <li>
                      <Link href="/other-work" className="nav-link text-xl font-medium">
                        Other Work
                      </Link>
                    </li>
                  </ul>
                </nav>
              </div>
            </div>
          </header>
          <main className="flex-grow container mx-auto">
            {children}
          </main>
          <footer className="bg-gray-900 py-6 border-t border-gray-800">
            <div className="container mx-auto px-4 text-center text-gray-400">
              <p>© {new Date().getFullYear()} Lisbon House Price Predictor</p>
            </div>
          </footer>
        </div>
      </body>
    </html>
  );
}