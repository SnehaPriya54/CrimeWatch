import React, { useEffect } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const CrimeMap = () => {
  useEffect(() => {
    const map = L.map('map').setView([51.505, -0.09], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors',
    }).addTo(map);

    // Example marker for crime data
    L.marker([51.5, -0.09]).addTo(map)
      .bindPopup('Crime Location')
      .openPopup();
  }, []);

  return <div id="map" style={{ height: '500px' }}></div>;
};

export default CrimeMap;
