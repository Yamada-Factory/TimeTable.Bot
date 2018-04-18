#!/usr/local/bin/python3
import line_api
import setting as set
from time_table import *
from string_changer import *
from module import *
from datetime import *

def konazikan():
    try:
        now = datetime.now()

        text = 'もうこんな時間かぁ'
        # time = ('ただいまの時刻は{}時{}分').format(now.hour, now.minute)
        line_api.push_message(set.ID,[text])
        return True
    except:
        return False
