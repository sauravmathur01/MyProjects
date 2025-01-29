import axios from 'axios';

export const saveResume = (data) => axios.post('http://localhost:5000/api/save-resume', data);
export const fetchReviews = () => axios.get('http://localhost:5000/api/reviews');
export const submitReview = (review) => axios.post('http://localhost:5000/api/submit-review', review);