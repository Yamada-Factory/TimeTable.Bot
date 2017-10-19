#!/usr/bin/env python3
import http.server
import re
import ssl
import urllib.parse
import line_api
import setting
import json
import time_table


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
        # print(data)
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
                    line_api.reply_message(reply_token, time_table.time_table_string(time_table.get_task(time_table.get_date(words[1]))))
                elif words[0] == 'イベント' or words[0] == 'event':
                    line_api.reply_message(reply_token, time_table.event_string(time_table.get_event(time_table.get_date(words[1]))))
                elif words[0] == '課題リスト' or words[0] == 'task_list':
                    line_api.reply_message(reply_token, time_table.task_list_string(time_table.get_task_list(time_table.get_date(words[1]))))
                elif words[0] == 'イベントリスト' or words[0] == 'event_list':
                    line_api.reply_message(reply_token, time_table.event_list_string(time_table.get_event_list(time_table.get_date(words[1]))))
                elif words[0] == '時間割' or words[0] == 'table':
                    line_api.reply_message(reply_token, time_table.time_table_string(time_table.get_time_table(time_table.get_date(words[1]))))

            except IndexError:
                line_api.reply_message(reply_token, '不正な入力です')


if __name__ == '__main__':
    server_address = (setting.SERVER_ADDRESS, setting.SERVER_PORT)
    # handler_class = http.server.SimpleHTTPRequestHandler  # ハンドラを設定
    simple_server = http.server.HTTPServer(server_address, Handler)
    simple_server.socket = ssl.wrap_socket(simple_server.socket, certfile=setting.CERT_FILE,
                                           keyfile=setting.KEY_FILE, server_side=True)
    simple_server.serve_forever()
