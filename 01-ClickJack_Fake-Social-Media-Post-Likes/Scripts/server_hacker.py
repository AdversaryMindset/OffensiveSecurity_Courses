# Created by Adversary Mindset for Training Purposes Only

import http.server
import socketserver

PORT = 4444

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # You can add custom handling here if needed
        super().do_GET()

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()
