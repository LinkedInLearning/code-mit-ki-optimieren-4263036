const http = require('http');
const fs = require('fs');
const url = require('url');
const path = require('path');
let queryAntwort = "";
const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  let filePath = '.' + parsedUrl.pathname;
  if (filePath === './') {
    filePath = './index.html'; // Standardseite
  }
  const extname = path.extname(filePath);
  let contentType = 'text/html';
  switch (extname) {
    case '.txt': contentType = 'text/plain'; break;
    case '.html': contentType = 'text/html'; break;
    default: contentType = 'text/plain';
  }
  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code === 'ENOENT') { // Datei nicht gefunden
         res.writeHead(404);
         res.end('Datei nicht gefunden');
      } else {
        res.writeHead(500); // Anderer Fehler
        res.end(`Interner Serverfehler: ${err.code}`);
      }
    } else { // Datei gefunden, sende Inhalt oder Reaktion auf Query
      console.log(queryAntwort); // Query
      res.writeHead(200, { 'Content-Type': contentType });
      // Wenn kein Query vorhanden
      if(queryAntwort.length < 5)
        res.end(content, 'utf-8'); // Sende Datei
      else // Sende Query-Daten 
        res.end(queryAntwort, 'utf-8');
    
    }
  });
});
server.on('error', (err) => {
  console.error('Serverfehler:', err);
});
// Daten über GET oder POST entgegennehmen
server.on('request', (req, res) => {
  if (req.method === 'GET') {
    console.log('GET-Anfrage empfangen');
    const queryData = url.parse(req.url, true).query;
    console.log('Daten:', queryData);
    queryAntwort = JSON.stringify(queryData);
  } else if (req.method === 'POST') {
    console.log('POST-Anfrage empfangen');
    let body = '';
    req.on('data', (chunk) => {
    body += chunk.toString();
    });
    req.on('end', () => {
    console.log('Daten:', body);
    queryAntwort = body;
    // Hier auf die POST-Daten reagieren und entsprechend queryAntworten
 //   res.writeHead(200, { 'Content-Type': 'application/json' });
 //   res.end(JSON.stringify({ message: 'POST-Erfolg' }));
    });
  }
});
// Server starten
const PORT = process.env.PORT || 3210;
server.listen(PORT, () => {
  console.log(`Server läuft auf Port ${PORT}`);
});
