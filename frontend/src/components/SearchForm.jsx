import React, { useState } from 'react';
import axios from 'axios';

const SearchForm = () => {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/query', { query });
      setAnswer(res.data.answer); // ✅ fixed here
    } catch (error) {
      console.error(error);
      setAnswer("Something went wrong. Please try again.");
    }
    setLoading(false);
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className="space-y-4">
        <textarea
          className="w-full border p-2 rounded"
          rows="4"
          placeholder="Enter scholarship query..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          required
        ></textarea>
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          {loading ? 'Searching...' : 'Search'}
        </button>
      </form>

      {answer && (
        <div className="mt-6 p-4 bg-green-100 border-l-4 border-green-500 text-green-800">
          <h2 className="font-semibold">Response:</h2>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
};

export default SearchForm;
