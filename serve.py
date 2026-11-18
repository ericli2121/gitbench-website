#!/usr/bin/env python3
"""Simple HTTP server for local development"""
import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"🚀 Serving Gitbench website at {url}")
        print(f"📂 Directory: {Path(__file__).parent}")
        print(f"\nPress Ctrl+C to stop")

        # Open browser
        webbrowser.open(url)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")
