#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import datetime
from time_table import *

def checkDate(year, month, day):
    try:
        newDataStr="%04d/%02d/%02d"%(year,month,day)
        newDate=datetime.datetime.strptime(newDataStr,"%Y/%m/%d")
        return True
    except ValueError:
        return False


# 本日の時間を返す
# 整形
def toStringDate(year, month, day):
    date = '{}/{}/{}'.format(year, month, day)
    return (format_date(date))
# 日付取得
def toDay():
    today = datetime.date.today()
    return toStringDate(today.year, today.month, today.day)

# 夜の8時に翌日に更新するための時間取得
def tomorrow_Day():
    tomorrow = datetime.datetime.now() + datetime.timedelta(hours = 5)
    return toStringDate(tomorrow.year, tomorrow.month, tomorrow.day)

# dateの教科とtaskの教科を一致させる
def referenceTask(date):
    # dateの課題及び授業取得
    date_task = get_task(date)
    date_time = get_time_table(date)

    task_the_Day = []
    for i in range(len(date_time)):
        for j in range(len(date_task)):
            if(date_time[i] == date_task[j].subject):
                task_the_Day.append(date_task[j].value)
                break
            else:
                task_the_Day.append('')
    return task_the_Day

# 課題取得
def today_task(date):
    tasks = task_list_string_date(get_task(date))
    task = tasks.split("<br>")
    return task

# 課題一覧を表示させる
def all_task():
    tasks = task_list_string_date(get_task_list_one(toDay()))
    task = tasks.split("<br>")
    return task

def task_list_string_date(data):
    if len(data) == 0:
        return 'なし'
    out = ''
    for e in data:
        out += e.date+'<br>'
        out += e.subject+'<br>'
        out += e.value
        out += '<br>'
    return out

# イベント一覧を表示させる
def referenceEvent():
    events = event_list_string_date(get_event_list_one(toDay()))
    event = events.split("<br>")
    return event


# イベントリストを文字列に変換する
def event_list_string_date(data):
    if len(data) == 0:
        return 'なし'
    out = ''
    for e in data:
        out += e.date+'<br>'
        out += e.event
        out += '<br>'
    return out
