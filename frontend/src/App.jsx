import React from 'react';
import SearchForm from './components/SearchForm';

const App = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-xl mx-auto bg-white p-6 rounded-xl shadow-md">
        <h1 className="text-2xl font-bold mb-4 text-center">Scholarship Finder</h1>
        <SearchForm />
      </div>
    </div>
  );
};

export default App;