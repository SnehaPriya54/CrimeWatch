import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart, CategoryScale, LinearScale, BarElement } from 'chart.js';
import { useNavigate } from 'react-router-dom';

// Register the scales and the bar element
Chart.register(CategoryScale, LinearScale, BarElement);

const PoliceDashboard = () => {
  const navigate = useNavigate(); // Hook for navigation

  const data = {
    labels: ['Crime 1', 'Crime 2', 'Crime 3'],
    datasets: [
      {
        label: 'Crimes Reported',
        data: [5, 10, 15],
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  const options = {
    scales: {
      x: {
        type: 'category', // Use category scale for x-axis
      },
      y: {
        type: 'linear', // Use linear scale for y-axis
        beginAtZero: true, // Start y-axis at zero
      },
    },
  };

  const handleLogout = () => {
    // Clear user data if necessary (optional)
    // localStorage.removeItem('user'); // Uncomment if you are storing user data in localStorage

    // Redirect to login page
    navigate('/login');
  };

  return (
    <div>
      <h2>Police Dashboard</h2>
      <Bar data={data} options={options} />
      <button onClick={handleLogout} style={{ marginTop: '20px',width:'20%' }}>
        Logout
      </button>
    </div>
  );
};

export default PoliceDashboard;
