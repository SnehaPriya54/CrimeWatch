import React, { useState } from 'react';

const DataEntryForm = () => {
  const [formData, setFormData] = useState({ crimeType: '', description: '' });

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    // Replace with API submission logic
  };

  return (
    <div>
      <h2>Data Entry Form</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Crime Type:
          <input type="text" value={formData.crimeType} onChange={(e) => setFormData({ ...formData, crimeType: e.target.value })} />
        </label>
        <label>
          Description:
          <input type="text" value={formData.description} onChange={(e) => setFormData({ ...formData, description: e.target.value })} />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default DataEntryForm;
