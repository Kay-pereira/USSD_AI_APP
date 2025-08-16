import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './css/Home.css';

const Reports = () => {
  const [reports, setReports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchReports = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/reports/');
        setReports(response.data);
      } catch (err) {
        console.error(err);
        setError('Failed to fetch delivery reports.');
      } finally {
        setLoading(false);
      }
    };

    fetchReports();
  }, []);

  return (
    <div className="container">
      <h1 className="title">Delivery Reports</h1>
      {loading && <p className="status">Loading reports...</p>}
      {error && <p className="status">{error}</p>}
      {!loading && !error && (
        <table className="reports-table">
          <thead>
            <tr>
              <th>Phone Number</th>
              <th>Message</th>
              <th>Status</th>
              <th>Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {reports.map((report) => (
              <tr key={report.id}>
                <td>{report.phone_number}</td>
                <td>{report.message}</td>
                <td>{report.status}</td>
                <td>{new Date(report.timestamp).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Reports;
