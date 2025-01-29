const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

// Mock database
let resumes = [];
let reviews = [];

// Save Resume Endpoint
app.post('/api/save-resume', (req, res) => {
  resumes.push(req.body);
  res.status(201).send('Resume saved');
});

// Review System Endpoint
app.post('/api/submit-review', (req, res) => {
  reviews.push(req.body);
  res.status(201).send('Review submitted');
});

app.get('/api/reviews', (req, res) => {
  res.json(reviews);
});

app.listen(5000, () => console.log('Server running on port 5000'));