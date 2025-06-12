#!/usr/bin/env python3
import json, http.server, socketserver

PORT = 8000

class Handler(http.server.BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send_response(200); self.end_headers();
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(payload)
        elif self.path == "/status":
            self._send_json({"status": "OK"})
        elif self.path == "/info":
            self._send_json({"version": "1.0", "description": "A simple API built with http.server"})
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\\nShutting down…")
            httpd.server_close()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\\nShutting down…")
            httpd.server_close()
