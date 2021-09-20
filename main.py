from http.server import HTTPServer, CGIHTTPRequestHandler


class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi"]


# run this script and then visit: http://localhost:8080?mac_address=DEADBEEF
PORT = 8080
http = HTTPServer(("", PORT), Handler)
print(f"Server at port: {PORT}")
http.serve_forever()