import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, Navigate } from 'react-router-dom';
import Login from './components/Auth/Login';
import Signup from './components/Auth/SignUp';
import PoliceDashboard from './components/Dashboard/PoliceDashboard';
import ClientDashboard from './components/Dashboard/ClientDashboard';
import './App.css';

const LandingPage = () => {
  return (
    <div>
      
    </div>
  );
};

const App = () => {
  return (
    <Router>
      <div>
        {/* Navigation Bar */}
        <nav style={{ backgroundColor: "#0056b3", color: 'white', padding: '10px' }}>
          <ul style={{ display: 'flex', listStyleType: 'none', gap: '20px', margin: 0 }}>
            <li><Link to="/" style={{ color: 'white', textDecoration: 'none' }}>Home</Link></li>
            <li><Link to="/login" style={{ color: 'white', textDecoration: 'none' }}>Login</Link></li>
            <li><Link to="/signup" style={{ color: 'white', textDecoration: 'none' }}>Sign Up</Link></li>
          </ul>
        </nav>

        {/* Routes */}
        <Routes>
          {/* Landing page is shown when the website is accessed */}
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/police-dashboard" element={<PoliceDashboard />} />
          <Route path="/client-dashboard" element={<ClientDashboard />} />
          
          {/* Catch-all route to redirect to landing page if no match */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
