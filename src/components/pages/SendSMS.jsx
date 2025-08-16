import React, { useState } from 'react';
import axios from 'axios';
import './css/Home.css';

const SendSMS = () => {
  const [phoneNumber, setPhoneNumber] = useState('');
  const [message, setMessage] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/sendsms/', {
        phone_number: phoneNumber,
        message: message
      });
      setStatus('Message sent successfully!');
      setPhoneNumber('');
      setMessage('');
    } catch (error) {
      console.error(error);
      setStatus('Failed to send message.');
    }
  };

  return (
    <div className="container">
      <h1 className="title">Send SMS</h1>
      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label>Phone Number:</label>
          <input
            type="text"
            value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)}
            placeholder="+233xxxxxxxxx"
            required
            className="input"
          />
        </div>
        <div className="form-group">
          <label>Message:</label>
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your message here..."
            required
            className="textarea"
          />
        </div>
        <button type="submit" className="btn">Send</button>
      </form>
      {status && <p className="status">{status}</p>}
    </div>
  );
};

export default SendSMS;
