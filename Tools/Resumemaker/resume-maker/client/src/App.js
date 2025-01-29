import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ResumeForm from './components/ResumeForm';
import ResumePreview from './components/ResumePreview';
import ReviewSystem from './components/ReviewSystem';

function App() {
  const [resumeData, setResumeData] = useState({});

  return (
    <Router>
      <Routes>
        <Route path="/" element={
          <div className="app-container">
            <ResumeForm onUpdate={setResumeData} />
            <ResumePreview data={resumeData} />
            <ReviewSystem />
          </div>
        }/>
      </Routes>
    </Router>
  );
}
const [darkMode, setDarkMode] = useState(false);
<div className={darkMode ? 'dark-theme' : 'light-theme'}>
  <button onClick={() => setDarkMode(!darkMode)}>
    Toggle Theme
  </button>
</div>
export default App;