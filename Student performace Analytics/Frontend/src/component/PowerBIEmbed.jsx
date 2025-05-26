import React from 'react';

const PowerBIEmbed = () => {
  return (
    <div className="my-6">
      <h2 className="text-xl font-bold mb-2">📊 Power BI Dashboard</h2>
      <iframe
        width="100%"
        height="600"
        src="https://app.powerbi.com/view?r=YOUR_REPORT_LINK"
        frameBorder="0"
        allowFullScreen
        title="Power BI Dashboard"
      ></iframe>
    </div>
  );
};

export default PowerBIEmbed;
