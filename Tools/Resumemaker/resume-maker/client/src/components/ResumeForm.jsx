import React, { useState } from 'react';

export default function ResumeForm({ onUpdate }) {
  const [formData, setFormData] = useState({
    personalInfo: { name: '', email: '', phone: '' },
    education: [],
    experience: [],
    skills: []
  });

  const handleInputChange = (section, field, value) => {
    setFormData(prev => ({
      ...prev,
      [section]: { ...prev[section], [field]: value }
    }));
    onUpdate(formData); // Pass data to parent
  };

  return (
    <div className="form-container">
      <h2>Personal Information</h2>
      <input
        type="text"
        placeholder="Full Name"
        onChange={(e) => handleInputChange('personalInfo', 'name', e.target.value)}
      />
      <input
        type="email"
        placeholder="Email"
        onChange={(e) => handleInputChange('personalInfo', 'email', e.target.value)}
      />
      <input
        type="tel"
        placeholder="Phone"
        onChange={(e) => handleInputChange('personalInfo', 'phone', e.target.value)}
      />
      {/* Add more fields for education, experience, and skills */}
    </div>
  );
}