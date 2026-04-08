import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({".html": "text/html"})

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
