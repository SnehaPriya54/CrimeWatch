import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Signup = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState(''); // Initialize as an empty string
  const [password, setPassword] = useState(''); // Initialize as an empty string
  const [role, setRole] = useState(''); // New state for user role
  const [error, setError] = useState('');

  const handleSignup = (e) => {
    e.preventDefault();

    // Retrieve existing users from localStorage
    const existingUsers = JSON.parse(localStorage.getItem('users')) || [];

    // Check if the username already exists
    const userExists = existingUsers.find((user) => user.username === username);

    if (userExists) {
      // If user exists, display an error message
      setError('Username already exists. Please choose a different one.');
    } else {
      // If user doesn't exist, create a new user object
      const newUser = { username, password, role };

      // Save the new user in localStorage
      existingUsers.push(newUser);
      localStorage.setItem('users', JSON.stringify(existingUsers));

      // Redirect to the login page after successful signup
      navigate('/login');
    }
  };

  return (
    <div>
      <h2>Sign Up</h2>
      <form onSubmit={handleSignup} key={Math.random()}>
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
            autoComplete="new-password"  // Prevents autofill
            name="new-password"  // Unique name for the input
          />
        </div>
        <br></br>
        <div>
          <label>Role:</label>
          <select value={role} onChange={(e) => setRole(e.target.value)} className=''required>
            <option value="">Select Role</option>
            <option value="police">Police</option>
            <option value="client">Client</option>
          </select>
        </div>
        <br></br>
        <button type="submit">Sign Up</button>
        
      </form>
      <p>
        Already have an account? <a href="/login">Login here</a>
      </p>

      {/* Display error message if username already exists */}
      {error && (
        <div style={{ color: 'red', marginTop: '10px' }}>
          {error}
        </div>
      )}

     
    </div>
  );
};

export default Signup;
