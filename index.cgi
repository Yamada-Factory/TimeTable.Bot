#!/usr/local/bin/python3

from bottle import *
from module import *
from string_changer import *
import line_api
import json
import setting
import sys
import signal
import processing_input
import inform, task, neta

my_api_key = 'xxx-xxx'

# SSLサーバ設定
# 使う場合
class SSLWebServer(ServerAdapter):
    def run(self, handler):
        from gevent.pywsgi import WSGIServer
        srv = WSGIServer((self.host, self.port), handler,
                         certfile=setting.CERT_FILE,
                         keyfile=setting.KEY_FILE,
                         ca_certs=setting.CA_FILE)
        srv.serve_forever()

#########################################
#                                       #
#             Webコントローラ             #
#                                       #
#########################################

# トップページ
@get('/')
def top():
    return '''<h1>Hello</h1>'''

# 独自API
# 時間割通知
@get('/api/inform')
def get_api_inform():
    id = request.query['id']
    if id == my_api_key:
        result = inform.infromToday()
    else:
        result = False
    return '''inform : {}'''.format(result)

# 課題リスト
@get('/api/task')
def get_api_task():
    id = request.query['id']
    if id == my_api_key:
        result = task.task_inform()
    else:
        result = False
    return '''task : {}'''.format(result)

# もう5時かAPI
@get('/api/mougozi')
def get_api_kona():
    id = request.query['id']
    if id == my_api_key:
        result = neta.konazikan()
    else:
        result = False
    return '''こんな時間 : {}'''.format(result)


# LINE API
@post('/TimeTable.Bot')
def line_post():
    signature = request.get_header('X-Line-Signature')
    body = request.body.read().decode('utf-8')
    if not line_api.signature_check(body, signature):
        return

    events = json.loads(body)['events']
    processing_input.processing_input(events)
#    print('end')
    body = json.dumps({})
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

def handler(signal, frame):
        # line_api.push_message(setting.ID, ['停止'])
        sys.exit(0)
signal.signal(signal.SIGINT, handler)
# line_api.push_message(setting.ID, ['起動'])

# build in server
if __name__=='__main__':
    # cgi serverで使うなら
    # xrea serverとかだとこっち
    run(host=setting.ADDRESS_URL, port=setting.ADDRESS_PORT, server='cgi', debug=True, reloader=True)

    # SSL証明書を必要とするときはこっち
    run(host=setting.ADDRESS_URL, port=setting.ADDRESS_PORT, server=SSLWebServer, debug=True, reloader=True)
    
