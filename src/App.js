import React from 'react';
import { BrowserRouter as Router, Route, Routes,Navigate } from 'react-router-dom';
import Login from './components/Auth/Login';
import Signup from './components/Auth/SignUp';
import PoliceDashboard from './components/Dashboard/PoliceDashboard';
import ClientDashboard from './components/Dashboard/ClientDashboard';

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/police-dashboard" element={<PoliceDashboard />} />
          <Route path="/client-dashboard" element={<ClientDashboard />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
