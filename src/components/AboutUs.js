// AboutUs.js
import React from 'react';
import "./AboutUs.css";

const AboutUs = () => {
  return (
    <section style={styles.container}>
      <h2 style={styles.heading}>About Us</h2>
      <p style={styles.text}>
        We are a company dedicated to delivering the best solutions for our clients. Our goal is to empower people with innovative tools and services that make a positive impact on their lives. With a team of experts in technology and a focus on continuous improvement, we are constantly striving for excellence.
      </p>
    </section>
  );
};

const styles = {
  container: {
    padding: '50px',
    backgroundColor: '#f0f0f0',
    textAlign: 'center',
  },
  heading: {
    fontSize: '32px',
    fontWeight: 'bold',
    marginBottom: '20px',
  },
  text: {
    fontSize: '18px',
    color: '#333',
    maxWidth: '800px',
    margin: '0 auto',
    lineHeight: '1.6',
  },
};

export default AboutUs;
