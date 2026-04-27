import axios from 'axios';

// Connects to your Node.js Backend
export const backendAPI = axios.create({
    baseURL: import.meta.env.VITE_BACKEND_URL || 'http://localhost:5000/api', 
    withCredentials: true
});

// Interceptor for checking token in localStorage is no longer needed since we use cookies
backendAPI.interceptors.request.use((config) => {
    return config;
});

// Connects directly to your Python AI Service
export const aiAPI = axios.create({
    baseURL: import.meta.env.VITE_AI_URL || 'http://localhost:8000',
});