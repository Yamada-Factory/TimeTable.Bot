import line_api
import json
import setting
import signal
import processing_input
from bottle import *


class SSLWebServer(ServerAdapter):
    def run(self, handler):
        from gevent.pywsgi import WSGIServer
        srv = WSGIServer((self.host, self.port), handler,
                         certfile=setting.CERT_FILE,
                         keyfile=setting.KEY_FILE,
                         ca_certs=setting.CA_FILE)
        srv.serve_forever()


@post('/TimeTable.Bot')
def line_post():
    signature = request.get_header('X-Line-Signature')
    body = request.body.read().decode('utf-8')
    if not line_api.signature_check(body, signature):
        return

    events = json.loads(body)['events']
    processing_input.processing_input(events)

    body = json.dumps({})
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r


def handler(signal, frame):
        line_api.push_message(setting.ID, ['停止'])
        sys.exit(0)


signal.signal(signal.SIGINT, handler)
line_api.push_message(setting.ID, ['起動'])
run(host='0.0.0.0', port=443, server=SSLWebServer)
