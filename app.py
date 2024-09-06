# app.py
import os
import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, World!\n")

	connection = None

	try:
        	connection = psycopg2.connect(
          	host="127.0.0.1",
            	port=5432,
            	dbname=os.getenv('DB_NAME', 'postgres'),
            	user=os.getenv('DB_USER', 'postgres'),
            	password=os.getenv('DB_PASSWORD', 'your-password')
        	)
        	self.wfile.write(b"Connected to the database successfully!\n")

    	except Exception as e:
        	error_message = f"Error connecting to the database: {e}"
            	self.wfile.write(error_message.encode('utf-8'))

	finally:
		if connection:
			connection.close()

def run(server_class=HTTPServer, handler_class=HelloWorldHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd server on port 8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
