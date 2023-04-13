const csv = require('csv-parser');
const fs = require('fs');

fs.createReadStream('DenverShotLocs.csv')
  .pipe(csv())
  .on('data', (row) => {
    console.log(row);
  })
  .on('end', () => {
    console.log('CSV file successfully parsed.');
  });

  fs.readFile('DenverShotLocs.json', 'utf8', (err, data) => {
    if (err) throw err;
    const shotLocs = JSON.parse(data);
    console.log(shotLocs);
  });