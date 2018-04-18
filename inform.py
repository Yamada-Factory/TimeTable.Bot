#!/usr/local/bin/python3
import line_api
import setting
from time_table import *
from string_changer import *
from module import *

def infromToday():
    try:
        date = tomorrow_Day()
        table = time_table_string(get_time_table(get_date(date)))
        task = task_string(get_task(get_date(date)))
        event = event_string(get_event(get_date(date)))

        #text = 'もうこんな時間かぁ'
        line_api.push_message(setting.ID, [table, task, event])
        #line_api.push_message(setting.ID,[text])
        return True
    except:
        return False
