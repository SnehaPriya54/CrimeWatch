import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "./Login.css";
import videoSrc from './globe.mp4'; 

const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    const existingUsers = JSON.parse(localStorage.getItem('users')) || [];
    const user = existingUsers.find(
      (user) => user.username === username && user.password === password
    );

    if (user) {
      if (user.role === 'police') {
        navigate('/police-dashboard');
      } else if (user.role === 'client') {
        navigate('/client-dashboard');
      }
    } else {
      setError('Account does not exist or incorrect credentials. Please sign up.');
    }
  };

  return (
    <div className="login-container">
      <video autoPlay muted loop id="background-video">
        <source src={videoSrc} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      
      <div className="form">
        <h2>Login</h2>
        <form onSubmit={handleLogin}>
          <div className="input-group">
            <label>Username:</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="input-group">
            <label>Password:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <div className="input-group">
            <label>Email Id:</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <br />
          <button type="submit">Login</button>
        </form>
        <p className="noaccount">
          Don't have an account? <a href="/signup">Sign up here</a>
        </p>
        {error && <div className="error">{error}</div>}
      </div>
    </div>
  );
};

export default Login;
