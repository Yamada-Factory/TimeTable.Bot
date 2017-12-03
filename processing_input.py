import re
import line_api
import setting
from string_changer import *
from time_table import *
import os


def processing_input(events):
    line_logger = logging.Logger('line_event')
    try:
        f = logging.FileHandler('./log/line-'+datetime.datetime.today().strftime('%Y-%m')+'.log')
        f.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
        line_logger.addHandler(f)
    except FileNotFoundError:
        os.mkdir('log')
        f = logging.FileHandler('./log/line-' + datetime.datetime.today().strftime('%Y-%m') + '.log')
        f.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
        line_logger.addHandler(f)
    
    command_logger = logging.Logger('command')
    f = logging.FileHandler('./log/command-'+datetime.datetime.today().strftime('%Y-%m')+'.log')
    f.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
    command_logger.addHandler(f)
    for event in events:
        type_ = event['type']

        command_data = list()

        source_type = event['source']['type']
        command_data.append(source_type)
        user_id = event['source'].get('userId', '-')
        command_data.append(user_id)
        group_id = '-'
        if source_type != 'user':
            group_id = event['source'].get(source_type+'Id', '-')
        command_data.append(group_id)

        if type_ != 'message':
            line_logger.log(30, ' '.join(command_data))
            return

        message_type = event['message']['type']
        message_id = event['message']['id']
        command_data.append(message_type)
        command_data.append(message_id)
        if message_type == 'text':
            command_data.append(event['message']['text'])
        elif message_type == 'file':
            command_data.append(event['message']['fileName'])
            # command_data.append(event['message']['fileSize'])
        elif message_type == 'location':
            command_data.append(event['message']['title'])
            command_data.append(event['message']['address'])
            command_data.append(event['message']['latitude'])
            command_data.append(event['message']['longitude'])
        elif message_type == 'sticker':
            command_data.append(event['message']['packageId'])
            command_data.append(event['message']['stickerId'])

        command_data = map(str, command_data)
        line_logger.log(30, ' '.join(command_data))

        if message_type != 'text':
            return

        reply_token = event['replyToken']
        text = event['message']['text']
        words = re.split('[ 　\n]', text)

        command_pattern = {'登録': '登録', 'register': '登録',
                           '削除': '削除', 'delete': '削除',
                           '更新': '更新', 'update': '更新',
                           'show': '表示'
                           }
        date_pattern = ['\d{4,4}/\d{1,2}/\d{1,2}','今日', '昨日', '明日', '明後日', '明々後日', '来週']
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
                       '起動停止ランダム': '起動停止ランダム',
                       '卍': '卍'
                       }

        flag = '表示'
        for p in command_pattern.keys():
            if p in words:
                flag = command_pattern[p]
                words.remove(p)
                break
        date = '今日'
        date_flag = False
        for d in date_pattern:
            for e in words:
                if re.match(d, e):
                    date = e
                    words.remove(e)
                    date_flag = True
                    break
            else:
                continue
            break
        tag = '-'
        for p in tag_pattern:
            if p in words:
                tag = tag_pattern[p]
                words.remove(p)
                break
        id_option = False
        if 'id' in words:
            id_option = True
            words.remove('id')

        if tag == '-':
            if date_flag:
                table = time_table_string(get_time_table(get_date(date)))
                task = task_string(get_task(get_date(date)))
                event = event_string(get_event(get_date(date)))
                
                command_logger.log(30, '{} {} {} success'.format(flag, tag, date))
                line_api.push_message(setting.ID, [table, task, event])
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
                elif tag == '卍':
                    line_api.reply_message(reply_token, 'ふとし')
                else:
                    raise Exception
                command_logger.log(30, '{} {} {} {} {} success'.format(user_id, group_id, flag, tag, date))
            elif flag == '登録':
                is_success = False
                value = list()
                if tag == '時間割' or tag == '時間割変更':
                    is_success = add_time_table_change(date, words[0], words[1])
                    value.extend(words[:2])
                elif tag == '課題':
                    is_success = add_task(date, words[0], words[1])
                    value.extend(words[:2])
                elif tag == 'イベント':
                    is_success = add_event(date, words[0])
                    value.extend(words[:1])
                if is_success:
                    line_api.reply_message(reply_token, 'success')
                    command_logger.log(30, '{} {} {} {} {} {} success'.format(user_id, group_id, flag, tag, date,
                                                                              ' '.join(value)))
                else:
                    line_api.reply_message(reply_token, 'failure')
                    command_logger.log(30, '{} {} {} {} {} {} failure'.format(user_id, group_id, flag, tag, date,
                                                                              ' '.join(value)))
            elif flag == '削除':
                is_success = False
                value = list()
                if tag == '時間割' or tag == '時間割変更':
                    if id_option:
                        is_success = delete_time_table_change_id(words[0])
                        value.extend(words[0:1])
                    else:
                        is_success = delete_time_table_change(date, words[0], words[1])
                        value.append(date)
                        value.extend(words[0:2])
                elif tag == '課題':
                    if id_option:
                        is_success = delete_task_id(words[0])
                        value.extend(words[0:1])
                    else:
                        is_success = delete_task(date, words[0], words[1])
                        value.append(date)
                        value.extend(words[0:2])
                elif tag == 'イベント':
                    if id_option:
                        is_success = delete_event_id(words[0])
                        value.extend(words[0:1])
                    else:
                        is_success = delete_event(date, words[0])
                        value.append(date)
                        value.extend(words[0:2])
                if is_success:
                    line_api.reply_message(reply_token, 'success')
                    command_logger.log(30, '{} {} {} {} {} success'.format(user_id, group_id, flag, tag,
                                                                              ' '.join(value)))
                else:
                    line_api.reply_message(reply_token, 'failure')
                    command_logger.log(30, '{} {} {} {} {} failure'.format(user_id, group_id, flag, tag,
                                                                           ' '.join(value)))
            elif flag == '更新':
                is_success = False
                value = list()
                if tag == '時間割' or tag == '時間割変更':
                    is_success = update_time_table_change(words[0], date, words[1], words[2])
                    value.extend(words[1:3])
                elif tag == '課題':
                    is_success = update_task(words[0], date, words[1], words[2])
                    value.extend(words[1:3])
                elif tag == 'イベント':
                    is_success = update_event(words[0], date, words[1])
                    value.extend(words[1:2])
                if is_success:
                    line_api.reply_message(reply_token, 'success')
                    command_logger.log(30, '{} {} {} {} {} {} success'.format(user_id, group_id, flag, tag, date,
                                                                              ' '.join(value)))
                else:
                    line_api.reply_message(reply_token, 'failure')
                    command_logger.log(30, '{} {} {} {} {} {} failure'.format(user_id, group_id, flag, tag, date,
                                                                              ' '.join(value)))
        except Exception:
            line_api.reply_message(reply_token, '不正な入力です')
