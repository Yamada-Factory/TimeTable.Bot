import urllib.parse
import urllib.parse
import time_table
import line_api
import urllib.parse
import json
from bottle import *


class SSLWebServer(ServerAdapter):
        def run(self, handler):
                from gevent.pywsgi import WSGIServer
                srv = WSGIServer((self.host, self.port), handler,
                certfile='/etc/pki/tls/certs/trompot/ssl.cert',
                keyfile='/etc/pki/tls/certs/trompot/ssl.key',
                ca_certs='/etc/pki/tls/certs/trompot/ca.cert')
                srv.serve_forever()


@post('/TimeTable.Bot')
def line_post():
    print('post')
    signature = request.get_header('X-Line-Signature')
    body = request.body
    print(body)
    if not line_api.signature_check(body, signature):
        return

    data = urllib.parse.unquote(body)
    data = data.replace('events=', '').replace('+', '').replace("'", '"')
    print(data)

    events = json.loads(data)
    for event in events:
        reply_token = event['replyToken']
        type = event['type']
        if type != 'message':
            return
        type = event['message']['type']
        if type != 'text':
            return
        text = event['message']['text']
        words = re.split('[,、.。 ]', text)
        if len(words) <= 1:
            return
        try:
            if words[0] == '登録' or words == 'register':
                b = True
                if words[1] == '課題' or words[1] == 'task':
                    b = time_table.add_task(time_table.get_date(words[2]), words[3], words[4])
                elif words[1] == 'イベント' or words[1] == 'event':
                    b = time_table.add_event(time_table.get_date(words[2]), words[3])
                elif words[1] == '時間割' or words[1] == 'table':
                    b = time_table.add_time_table_change(time_table.get_date(words[2]), words[3], words[4])
                if b:
                    line_api.reply_message(reply_token, 'success')
                else:
                    line_api.reply_message(reply_token, 'failure')
            elif words[0] == '課題' or words[0] == 'task':
                line_api.reply_message(reply_token,
                                       time_table.time_table_string(time_table.get_task(time_table.get_date(words[1]))))
            elif words[0] == 'イベント' or words[0] == 'event':
                line_api.reply_message(reply_token,
                                       time_table.event_string(time_table.get_event(time_table.get_date(words[1]))))
            elif words[0] == '課題リスト' or words[0] == 'task_list':
                line_api.reply_message(reply_token, time_table.task_list_string(
                    time_table.get_task_list(time_table.get_date(words[1]))))
            elif words[0] == 'イベントリスト' or words[0] == 'event_list':
                line_api.reply_message(reply_token, time_table.event_list_string(
                    time_table.get_event_list(time_table.get_date(words[1]))))
            elif words[0] == '時間割' or words[0] == 'table':
                line_api.reply_message(reply_token, time_table.time_table_string(
                    time_table.get_time_table(time_table.get_date(words[1]))))

        except IndexError:
            line_api.reply_message(reply_token, '不正な入力です')

    body = json.dumps({})
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

run(host='0.0.0.0', port=443, server=SSLWebServer)
