const fs = require('fs');
const csv = require('csv-parser');
const path = require('path');

const IN  = path.join(__dirname, 'cleaned_data.csv');
const OUT = path.join(__dirname, 'quake_data.js');

let features = [];

fs.createReadStream(IN)
    .pipe(csv({ separator: ',', quote: '"' }))
    .on('data', row => {
        if (!row.longitude || !row.latitude) return;
        features.push({
            type: 'Feature',
            properties: {
                place: row.place,
                mag:   parseFloat(row.mag),
                time:  Date.parse(row.time)   // gibt ms seit 1970 zurück
            },
            geometry: {
                type: 'Point',
                coordinates: [
                    parseFloat(row.longitude),
                    parseFloat(row.latitude)
                ]
            }
        });
    })
    .on('end', () => {
        const geojson = { type: 'FeatureCollection', features };
        const outStr = `const quakeData = ${JSON.stringify(geojson)};`;
        fs.writeFileSync(OUT, outStr, 'utf-8');
        console.log(`✅ ${OUT} mit ${features.length} Features erzeugt`);
    });
