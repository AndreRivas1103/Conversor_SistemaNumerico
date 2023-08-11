from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from converter import decimal_to_other_bases, other_bases_to_decimal

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 - Not Found")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)

        number = parsed_data["number"][0]
        input_base = parsed_data["input_base"][0]
        output_base = parsed_data["output_base"][0]

        if input_base == "dec":
            converted_number = decimal_to_other_bases(number)
            result = converted_number[{'hex': 0, 'bin': 1, 'oct': 2}[output_base]]
        else:
            decimal_number = other_bases_to_decimal(number, input_base)
            if output_base == "dec":
                result = str(decimal_number)
            else:
                converted_number = decimal_to_other_bases(decimal_number)
                result = converted_number[{'hex': 0, 'bin': 1, 'oct': 2}[output_base]]

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(result.encode())

def run_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Servidor iniciado en http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
