import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'UP UP and AWAY!! SUPER WASHED Aint He??!! Stay low and keep firing! The air up there is a tad bit different. LIVE.LAUGH.LOVE#striveforgreatness #thekidfromakron#jamesgang #bronknows %s' % (self.path)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
