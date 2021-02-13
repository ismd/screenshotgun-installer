#!/usr/bin/env python
import argparse
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import hmac
import json
import os
import pathlib
import subprocess

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            if self.path == '/_/update':
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)

                if not verify_signature(self.headers, body):
                    raise ValueError('Invalid X-Hub-Signature-256')

                data = json.loads(body)
                if data['action'] == 'published':
                    path = "%s/update.py %s/%s" % \
                        (pathlib.Path(__file__).absolute(), \
                         data['repository']['releases_url'], \
                         data['release']['release_id'])

                    print("Running in background", path)
                    subprocess.Popen(path)

                self.send_response(200)
                self.end_headers()
            else:
                self.send_error(404)
        except Exception as err:
            self.send_error(404)
            print(err)

    def do_GET(self):
        self.send_error(404)

def verify_signature(headers, body):
    signature = hmac.new(
        os.environ['SECRET_TOKEN'].encode(),
        body,
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(signature, headers['X-Hub-Signature-256'].split('=')[1])

def run(listen, port):
    server = HTTPServer((listen, port), Server)
    print('Server started http://%s:%s' % (listen, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Server stopped.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Screenshotgun installer updater')

    parser.add_argument(
        '-l',
        '--listen',
        default='localhost',
        help='Specify the IP address on which the server listens',
    )

    parser.add_argument(
        '-p',
        '--port',
        type=int,
        default=8000,
        help='Specify the port on which the server listens',
    )

    args = parser.parse_args()
    run(args.listen, args.port)
