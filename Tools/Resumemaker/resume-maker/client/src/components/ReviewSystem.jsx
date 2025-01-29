import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function ReviewSystem() {
  const [reviews, setReviews] = useState([]);
  const [newReview, setNewReview] = useState({ rating: 5, comment: '' });

  useEffect(() => {
    axios.get('/api/reviews').then(res => setReviews(res.data));
  }, []);

  const submitReview = () => {
    axios.post('/api/submit-review', newReview)
      .then(() => {
        setReviews([...reviews, newReview]);
        setNewReview({ rating: 5, comment: '' });
      });
  };

  return (
    <div className="review-section">
      <h3>User Reviews</h3>
      <div className="star-rating">
        {[...Array(5)].map((_, i) => (
          <button key={i} onClick={() => setNewReview({...newReview, rating: i+1})}>
            ⭐
          </button>
        ))}
      </div>
      <textarea
        value={newReview.comment}
        onChange={(e) => setNewReview({...newReview, comment: e.target.value})}
      />
      <button onClick={submitReview}>Submit Review</button>
    </div>
  );
}