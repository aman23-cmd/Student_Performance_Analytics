const express = require('express');
const router = express.Router();
const fs = require('fs');
const { Parser } = require('json2csv');

// Sample student data - normally fetch from DB
const studentData = [
  { name: 'Aman', roll: '101', math: 85, science: 92 },
  { name: 'Ravi', roll: '102', math: 78, science: 80 },
  { name: 'Simran', roll: '103', math: 90, science: 95 },
];

router.get('/export-csv', (req, res) => {
  try {
    const fields = ['name', 'roll', 'math', 'science'];
    const json2csvParser = new Parser({ fields });
    const csv = json2csvParser.parse(studentData);

    res.setHeader('Content-Disposition', 'attachment; filename=student_data.csv');
    res.set('Content-Type', 'text/csv');
    res.status(200).send(csv);
  } catch (err) {
    console.error(err);
    res.status(500).send('Error generating CSV');
  }
});

module.exports = router;
