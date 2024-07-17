import http.server
import socketserver
import urllib.parse
import os

queryAntwort = ""

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global queryAntwort
        parsed_url = urllib.parse.urlparse(self.path)
        query_data = urllib.parse.parse_qs(parsed_url.query)
        queryAntwort = str(query_data)

        if parsed_url.path == '/':
            self.path = '/index.html'
        
        try:
            super().do_GET()
        except Exception as e:
            self.send_error(500, f"Interner Serverfehler: {str(e)}")
        
    def do_POST(self):
        global queryAntwort
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        queryAntwort = post_data.decode('utf-8')
        print('Daten:', queryAntwort)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"message": "POST-Erfolg"}')
        
    def end_headers(self):
        global queryAntwort
        self.send_header('Content-Type', self.guess_type(self.path))
        super().end_headers()

    def send_head(self):
        global queryAntwort
        parsed_url = urllib.parse.urlparse(self.path)
        file_path = '.' + parsed_url.path
        
        if os.path.exists(file_path):
            if len(queryAntwort) < 5:
                return super().send_head()
            else:
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                return io.BytesIO(queryAntwort.encode('utf-8'))
        else:
            self.send_error(404, 'Datei nicht gefunden')

PORT = 3210
Handler = CustomHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server läuft auf Port {PORT}")
    httpd.serve_forever()
