import React from 'react';

const ExportButton = () => {
  const handleExport = () => {
    window.open('http://localhost:5000/api/export-csv', '_blank');
  };

  return (
    <button
      onClick={handleExport}
      className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
    >
      Download CSV for Power BI
    </button>
  );
};

export default ExportButton;
