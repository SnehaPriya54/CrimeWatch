import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, Navigate } from 'react-router-dom';
import Login from './components/Auth/Login';
import Signup from './components/Auth/SignUp';
import PoliceDashboard from './components/Dashboard/PoliceDashboard';
import ClientDashboard from './components/Dashboard/ClientDashboard';

const LandingPage = () => {
  return (
    <div>
      <h1>Welcome to the Crime Management System</h1>
      <p>Please login or signup to access the dashboard.</p>
    </div>
  );
};

const App = () => {
  return (
    <Router>
      <div>
        {/* Navigation Bar */}
        <nav>
          <ul style={{ display: 'flex', listStyleType: 'none', gap: '20px' }}>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/signup">Sign Up</Link></li>
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
