
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json


class DockerPracticeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            response = {
                "message": "Hello from my Python Docker application!",
                "status": "success"
            }
            self.send_response(200)

        elif self.path == "/health":
            response = {
                "status": "healthy"
            }
            self.send_response(200)

        else:
            response = {
                "error": "Endpoint not found"
            }
            self.send_response(404)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

port = int(os.environ.get("PORT", 8000))
server = HTTPServer(("0.0.0.0", port), DockerPracticeHandler)

print(f"Server running on port {port}")
server.serve_forever()
