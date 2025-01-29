import React from 'react';
import html2pdf from 'html2pdf.js';

export default function ResumePreview({ data }) {
  const exportPDF = () => {
    const element = document.getElementById('resume-content');
    html2pdf().from(element).save();
  };

  return (
    <div className="preview-pane">
      <div id="resume-content">
        <h1>{data.personalInfo.name}</h1>
        <p>{data.personalInfo.email} | {data.personalInfo.phone}</p>
        <h2>Education</h2>
        <ul>
          {data.education.map((edu, index) => (
            <li key={index}>{edu.degree} at {edu.institution}</li>
          ))}
        </ul>
        <h2>Experience</h2>
        <ul>
          {data.experience.map((exp, index) => (
            <li key={index}>{exp.title} at {exp.company}</li>
          ))}
        </ul>
      </div>
      <button onClick={exportPDF}>Download PDF</button>
    </div>
  );
}