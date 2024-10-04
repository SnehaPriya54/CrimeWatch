
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "./Login.css";
import "./IMG.jpg";


const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');  // Initialize as an empty string
  const [password, setPassword] = useState('');  // Initialize as an empty string
  const [error, setError] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();

    // Retrieve users from localStorage
    const existingUsers = JSON.parse(localStorage.getItem('users')) || [];

    // Check if the user exists
    const user = existingUsers.find(
      (user) => user.username === username && user.password === password
    );

    if (user) {
      // Redirect to the appropriate dashboard based on the user's role
      if (user.role === 'police') {
        navigate('/police-dashboard');
      } else if (user.role === 'client') {
        navigate('/client-dashboard');
      }
    } else {
      // If no user is found, display an error message
      setError('Account does not exist or incorrect credentials. Please sign up.');
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleLogin} key={Math.random()} >
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            autoComplete="new-username"  // Prevents autofill
            name="new-username"  // Unique name for the input
          />
        </div>
        <br></br>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            autoComplete="off"  // Prevents autofill
            name="password"  // Unique name for the input
          />
        </div>
        <br></br>
        <button type="submit">Login</button>
        
      </form>
      <p className='noaccount'>
        Don't have an account? <a href="/signup">Sign up here</a>
      </p>

      {/* Display error message if account does not exist */}
      {error && (
        <div style={{ color: 'red', marginTop: '10px' }}>
          {error}
        </div>
      )}

      
    </div>
  );
};

export default Login;
