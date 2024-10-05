// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, Navigate } from 'react-router-dom';
import Login from './components/Auth/Login';

import PoliceDashboard from './components/Dashboard/PoliceDashboard';
import ClientDashboard from './components/Dashboard/ClientDashboard';
import './App.css';
import videoSrc from './cloud.mp4'; 
import AboutUs from './components/AboutUs';  // Import About Us
import Footer from './components/Footer';    // Import Footer

const LandingPage = () => {
  return (
    <div>
      <br></br><br></br>
      <video autoPlay muted loop id="video">
        <source src={videoSrc} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      
     
    
    </div>
  );
};

const App = () => {
  return (
    <Router>
    
      <div className="app-container">  {/* Flexbox wrapper */}
        {/* Navigation Bar */}
        <nav style={{ backgroundColor: "#0056b3", color: 'white', padding: '10px' }}>
  <ul style={{ display: 'flex', listStyleType: 'none', gap: '20px', margin: 0, padding: 0, alignItems: 'center', width: '100%' }}>
    <li><Link to="/" style={{ color: 'white', textDecoration: 'none' }}>Home</Link></li>
    <li><Link to="/login" style={{ color: 'white', textDecoration: 'none' }}>Login</Link></li>
    <li><Link to="/aboutus" style={{ color: 'white', textDecoration: 'none' }}>About Us</Link></li>
    <li style={{ flexGrow: 1 }}></li> {/* This will push the h1 to the extreme right */}
    <li><h1 style={{ color: "white", margin: 0 }}>CRIME WATCH</h1></li>
  </ul>
</nav>

        {/* Main content area */}
        <div className="content-wrapper">  {/* Content wrapper */}
          <Routes>
            {/* Landing page is shown when the website is accessed */}
            <Route path="/" element={<LandingPage />} />
            <Route path="/login" element={<Login />} />
            <Route path="/aboutus" element={<AboutUs />} />
            <Route path="/police-dashboard" element={<PoliceDashboard />} />
            <Route path="/client-dashboard" element={<ClientDashboard />} />
            
            {/* Catch-all route to redirect to landing page if no match */}
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </div>

        {/* Footer */}
        <Footer />
      </div>
    </Router>
  );
};

export default App;
