#!/usr/bin/env python3
import http.server
import re
import ssl
import urllib.parse
import line_api
import setting
import json


class Handler(http.server.CGIHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        headers = self.headers
        signature = headers.get('X-Line-Signature')

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len).decode('utf-8')

        if not line_api.signature_check(post_body, signature):
            return

        data = urllib.parse.unquote(post_body)
        data = data.replace('events=', '').replace('+', '').replace("'", '"')
        print(data)
        events = json.loads(data)

        for event in events:
            reply_token = event['replyToken']
            type = event['type']
            if type == 'message':
                type = event['message']['type']
                if type == 'text':
                    text = event['message']['text']
                    words = re.split('[,、.。 ]', text)
                    if len(words) == 0:
                        return

                    if words[0] == '登録' or words == 'register':
                        if words[1] == '課題' or words[1] == 'task':
                            time_table.update_task(words[2], words[3], words[4])
                        elif words[1] == 'イベント' or words[1] == 'event':
                            time_table.update_event(words[2], words[3])
                        elif words[1] == '振替' or words[1] == 'trans':
                            time_table.update_trans(words[2], words[3])
                        elif words[1] == '変更' or words[1] == 'change':
                            time_table.update_time_table_change(words[2], words[3], words[4])
                    elif words[0] == '課題' or words[0] == 'task':
                        line_api.reply_message(reply_token, time_table.get_task(words[1]))
                    elif words[0] == 'イベント' or words[0] == 'event':
                        line_api.reply_message(reply_token, time_table.get_event(words[1]))
                    elif words[0] == '課題リスト' or words[0] == 'task_list':
                        line_api.reply_message(reply_token, time_table.get_task_list(words[1]))
                    elif words[0] == 'イベントリスト' or words[0] == 'event_list':
                        line_api.reply_message(reply_token, time_table.get_event_list(words[1]))
                    else:
                        time_table = time_table.get_time_table(words[0])
                        task = time_table.get_task(words[0])
                        event = time_table.get_event(words[0])


if __name__ == '__main__':
    server_address = (setting.SERVER_ADDRESS, setting.SERVER_PORT)
    # handler_class = http.server.SimpleHTTPRequestHandler  # ハンドラを設定
    simple_server = http.server.HTTPServer(server_address, Handler)
    simple_server.socket = ssl.wrap_socket(simple_server.socket, certfile=setting.CERT_FILE,
                                           keyfile=setting.KEY_FILE, server_side=True)
    simple_server.serve_forever()
