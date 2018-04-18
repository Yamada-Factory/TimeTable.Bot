#!/usr/local/bin/python3
import line_api
import setting
from time_table import *
from string_changer import *
from module import *
from datetime import *


def task_inform():
    try:
        now = datetime.now()

        #text = 'もうこんな時間かぁ'
        #time = ('ただいまの時刻は{}時{}分').format(now.hour, now.minute)

        comment = '課題List {}時通知'.format(now.hour)
        date = '2018/{}/{}'.format(now.month, now.day)
        line_api.push_message(setting.ID, [comment, task_list_string(get_task_list(date))])
        #line_api.push_message(setting.ID,[text, time])
        return True
    except:
        return False
