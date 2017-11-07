import re
import line_api
from string_changer import *
from time_table import *


def processing_input(events):
    for event in events:
        reply_token = event['replyToken']
        if event['type'] != 'message':
            return
        if event['message']['type'] != 'text':
            return
        text = event['message']['text']
        words = re.split('[ 　\n]', text)

        command_pattern = {'登録': '登録', 'register': '登録',
                           '削除': '削除', 'delete': '削除',
                           '更新': '更新', 'update': '更新'
                           }
        date_pattern = ['\d{4,4}/\d{1,2}/\d{1,2}', '昨日', '明日', '明後日', '明々後日', '来週']
        tag_pattern = {'時間割': '時間割',
                       'time_table': '時間割',
                       '課題': '課題',
                       'task': '課題',
                       'イベント': 'イベント',
                       'event': 'イベント',
                       '課題リスト': '課題リスト',
                       'task_list': '課題リスト',
                       'イベントリスト': 'イベントリスト',
                       'event_list': 'イベントリスト',
                       '時間割変更': '時間割変更',
                       'time_table_change': '時間割変更',
                       '起動停止ランダム': '起動停止ランダム'
                       }

        flag = '表示'
        for p in command_pattern.keys():
            if p in words:
                flag = command_pattern[p]
                words.remove(p)
                break
        date = '今日'
        for d in date_pattern:
            for e in words:
                if re.match(d, e):
                    date = e
                    words.remove(e)
                    break
            else:
                continue
            break
        tag = ''
        for p in tag_pattern:
            if p in words:
                tag = tag_pattern[p]
                words.remove(p)
                break
        id_option = False
        if 'id' in words:
            id_option = True
            words.remove('id')

        if tag == '':
            return
        try:
            if flag == '表示':
                if tag == '時間割':
                    line_api.reply_message(reply_token, time_table_string(get_time_table(date)))
                elif tag == '課題':
                    line_api.reply_message(reply_token, task_string(get_task(date)))
                elif tag == 'イベント':
                    line_api.reply_message(reply_token, event_string(get_event(date)))
                elif tag == '課題リスト':
                    if id_option:
                        line_api.reply_message(reply_token, task_list_string_id(get_task_list(date)))
                    else:
                        line_api.reply_message(reply_token, task_list_string(get_task_list(date)))
                elif tag == 'イベントリスト':
                    if id_option:
                        line_api.reply_message(reply_token, event_list_string_id(get_event_list(date)))
                    else:
                        line_api.reply_message(reply_token, event_list_string(get_event_list(date)))
                elif tag == '時間割変更':
                    if id_option:
                        line_api.reply_message(reply_token, time_table_change_list_string_id(get_time_table_change_list(date)))
                    else:
                        line_api.reply_message(reply_token, time_table_change_list_string(get_time_table_change_list(date)))
                elif tag == '起動停止ランダム':
                    line_api.reply_message(reply_token, '機動停止ガンダム')
            elif flag == '登録':
                if tag == '時間割' or tag == '時間割変更':
                    if add_time_table_change(date, words[0], words[1]):
                        line_api.reply_message(reply_token, 'success')
                    else:
                        line_api.reply_message(reply_token, 'failure')
                elif tag == '課題':
                    if add_task(date, words[0], words[1]):
                        line_api.reply_message(reply_token, 'success')
                    else:
                        line_api.reply_message(reply_token, 'failure')
                elif tag == 'イベント':
                    if add_event(date, words[0]):
                        line_api.reply_message(reply_token, 'success')
                    else:
                        line_api.reply_message(reply_token, 'failure')
            elif flag == '削除':
                if tag == '時間割' or tag == '時間割変更':
                    if id_option:
                        if delete_time_table_change_id(words[0]):
                            line_api.reply_message(reply_token, 'success')
                        else:
                            line_api.reply_message(reply_token, 'failure')
                    else:
                        if delete_time_table_change(date, words[0], words[1]):
                            line_api.reply_message(reply_token, 'success')
                        else:
                            line_api.reply_message(reply_token, 'failure')
                elif tag == '課題':
                    if id_option:
                        if delete_task_id(words[0]):
                            line_api.reply_message(reply_token, 'success')
                        else:
                            line_api.reply_message(reply_token, 'failure')
                    else:
                        if delete_task(date, words[0], words[1]):
                            line_api.reply_message(reply_token, 'success')
                        else:
                            line_api.reply_message(reply_token, 'failure')
                elif tag == 'イベント':
                    if id_option:
                        if delete_event_id(words[0]):
                            line_api.reply_message(reply_token, 'success')
                        else:
                            line_api.reply_message(reply_token, 'failure')
                    else:
                        if delete_event(date, words[0]):
                            line_api.reply_message(reply_token, 'success')
                        else:
                            line_api.reply_message(reply_token, 'failure')
            elif flag == '更新':
                if tag == '時間割' or tag == '時間割変更':
                    if update_time_table_change(words[0], date, words[1], words[2]):
                        line_api.reply_message(reply_token, 'success')
                    else:
                        line_api.reply_message(reply_token, 'failure')
                elif tag == '課題':
                    if update_task(words[0], date, words[1], words[2]):
                        line_api.reply_message(reply_token, 'success')
                    else:
                        line_api.reply_message(reply_token, 'failure')
                elif tag == 'イベント':
                    if update_event(words[0], date, words[1]):
                        line_api.reply_message(reply_token, 'success')
                    else:
                        line_api.reply_message(reply_token, 'failure')
        except Exception:
            line_api.reply_message(reply_token, '不正な入力です')
