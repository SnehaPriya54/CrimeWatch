import React from 'react';
import { useNavigate } from 'react-router-dom';

const ClientDashboard = () => {
  const navigate = useNavigate(); // Hook for navigation

  const handleLogout = () => {
    // Clear user data if necessary (optional)
    // localStorage.removeItem('user'); // Uncomment if you are storing user data in localStorage

    // Redirect to login page
    navigate('/login');
  };

  return (
    <div>
      <h2>Client Dashboard</h2>
      <p>Welcome, client! View relevant data here.</p>
      <button onClick={handleLogout} style={{ marginTop: '20px' }}>
        Logout
      </button>
    </div>
  );
};

export default ClientDashboard;
