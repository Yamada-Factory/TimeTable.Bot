import re
import time_table
import line_api

def processing_input(events):
    for event in events:
        reply_token = event['replyToken']
        if event['type'] != 'message':
            return
        if event['message']['type'] != 'text':
            return
        text = event['message']['text']
        words = re.split('[ 　\n]', text)
        if len(words) <= 1:
            return
        try:
            if words[0] == '登録' or words[0] == 'register':
                b = False
                if words[1] == '課題' or words[1] == 'task':
                    b = time_table.add_task(time_table.get_date(words[2]), words[3], words[4])
                elif words[1] == 'イベント' or words[1] == 'event':
                    b = time_table.add_event(time_table.get_date(words[2]), words[3])
                elif words[1] == '時間割' or words[1] == 'table':
                    b = time_table.add_time_table_change(time_table.get_date(words[2]), words[3], words[4])
                else:
                    return
                if b:
                    line_api.reply_message(reply_token, 'success')
                else:
                    line_api.reply_message(reply_token, 'failure')
            elif words[0] == '削除' or words[0] == 'delete':
                b = False
                if words[1] == '課題' or words[1] == 'task':
                    b = time_table.delete_task(time_table.get_date(words[2]), words[3], words[4])
                elif words[1] == 'イベント' or words[1] == 'event':
                    b = time_table.delete_event(time_table.get_date(words[2]), words[3])
                elif words[1] == '時間割' or words[1] == 'table':
                    b = time_table.delete_time_table_change(time_table.get_date(words[2]), words[3], words[4])
                else:
                    return
                if b:
                    line_api.reply_message(reply_token, 'success')
                else:
                    line_api.reply_message(reply_token, 'failure')
            elif words[0] == '課題' or words[0] == 'task':
                line_api.reply_message(reply_token,
                                       time_table.task_string(time_table.get_task(time_table.get_date(words[1]))))
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