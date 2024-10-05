// Footer.js
import React from 'react';

const Footer = () => {
  return (
    <footer style={styles.footer}>
      <div style={styles.container}>
        <p style={styles.text}>© 2024 Our Company. All rights reserved.</p>
        <ul style={styles.links}>
          <li><a href="/privacy" style={styles.link}>Privacy Policy</a></li>
          <li><a href="/terms" style={styles.link}>Terms of Service</a></li>
          <li><a href="/contact" style={styles.link}>Contact Us</a></li>
        </ul>
      </div>
    </footer>
  );
};

const styles = {
  footer: {
    backgroundColor: '#222',
    color: '#fff',
    padding: '20px 0',
    textAlign: 'center',
  },
  container: {
    maxWidth: '1200px',
    margin: '0 auto',
  },
  text: {
    marginBottom: '10px',
    fontSize: '14px',
  },
  links: {
    listStyleType: 'none',
    padding: 0,
    display: 'flex',
    justifyContent: 'center',
    gap: '20px',
  },
  link: {
    color: '#fff',
    textDecoration: 'none',
    fontSize: '14px',
  }
};

export default Footer;
