# Student Performance Analytics 🚀



A full-stack web application to analyze and visualize student performance using modern web technologies and **Power BI integration**.

---

## 🚀 Tech Stack

- **Frontend**: React.js + Tailwind CSS
- **Backend**: Node.js + Express
- **Database**: MongoDB / MySQL (customizable)
- **Visualization**:
  - In-app charts using Chart.js (optional)
  - 🔥 Power BI / Tableau Embedded Dashboards

---

## 📌 Features

- 👥 Student login/signup
- 📈 Performance graphs (marks, attendance, subject-wise analysis)
- 💡 Real-time analytics dashboard
- ⬇️ **Export data as CSV** (for Power BI/Tableau)
- 🔗 **Embedded Power BI Dashboard** in web app

---

## 📁 Folder Structure

Student_Performance_Analytics/
├── client/ # React frontend
│ ├── src/
│ │ ├── components/
│ │ │ ├── PowerBIEmbed.jsx
│ │ │ └── ExportButton.jsx
│ │ └── App.jsx
│ └── package.json
├── server/ # Node.js backend
│ ├── routes/
│ │ └── exportData.js # CSV download route
│ └── index.js
└── README.md

yaml
Copy
Edit

---

## 📤 Export Data for Power BI

User can export student performance data as a `.csv` file with one click:

➡️ **URL**:  
```bash
GET /api/export-csv
📥 CSV Format Example:


name,roll,math,science
Aman,101,85,92
Ravi,102,78,80
Simran,103,90,95
📊 Embed Power BI Dashboard
Power BI visuals are embedded directly inside the React dashboard.

🔧 How to Add Your Power BI Report
Create visuals in Power BI Desktop

Publish to Power BI Service

Go to File > Embed > Website or Portal

Copy the embed link

Replace the iframe in PowerBIEmbed.jsx:



<iframe
  width="100%"
  height="600"
  src="https://app.powerbi.com/view?r=YOUR_REPORT_LINK"
  frameBorder="0"
  allowFullScreen
></iframe>
🧠 Future Enhancements
🧑‍🏫 Admin dashboard for teachers

🧠 AI-based student performance prediction

📲 Mobile-friendly responsive design

🔐 Role-based dashboards (student/teacher/admin)

🙌 Author
Aman Kaushal
🎓 B.Tech CSE (AI) | Galgotias University
🔗 GitHub - @aman23-cmd




