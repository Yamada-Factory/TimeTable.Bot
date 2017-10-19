# -*- coding: utf-8 -*-

from bottle import *
from module import *
from time_table import *
import urllib


#from bottle import route, run, template, request

# 翌日の時間割及び課題の表示
@route('/')
def top():
    date = tomorrow_Day()
    time = get_time_table(date)
    if( len(get_time_table(date)) == 0):
        return template('top', time='', task = '', today = date, message = 'はお休みです．')
    else:
        return template('top', time = time, task = referenceTask(date), today = date, message = ' ')

# 課題管理
@route('/task')
def task_views():
    return template('main_task', message='')

# 課題追加
@route('/task/add')
def task_add_views():
    return template('main_task_add', message='')

@post('/task/add')
def task_add():
    subject = request.forms.subject
    contents = request.forms.comment
    dead_line_year = int( request.forms.get("year") )
    dead_line_month = int( request.forms.get("month") )
    dead_line_day = int( request.forms.get("day") )

    # 入力値判定
    if (subject == ''):
        return template('main_task_add', message='不正な値です!!')
    elif (contents == ''):
        return template('main_task_add', message='不正な値です!!')
    elif ( checkDate(dead_line_year, dead_line_month, dead_line_day) != True ):
        return template('main_task_add', message='不正な値です!!')
    else:
        day = toStringDate(dead_line_year, dead_line_month, dead_line_day)
        if (add_task(day, subject, contents) == True):
            return template('main_task', message='追加しました!')
        else:
            return template('main_task_add', message='失敗しました!')
        return redirect('/task', message='')


# 授業管理
# 時間割表示(mobile非対応)
@route('/時間割')
def time_table_view():
    return template('main_timetable', message='')

# 時間割変更
@route('/時間割/変更')
def time_table_change_view():
    return template('main_timetable_change', message='')

@post('/時間割/変更')
def time_table_change():
    subject = request.forms.subject
    time = request.forms.get("time")
    dead_line_year = int( request.forms.get("year") )
    dead_line_month = int( request.forms.get("month") )
    dead_line_day = int( request.forms.get("day") )

    # 入力値判定
    if (subject == ''):
        return template('main_timetable_change', message='不正な値です!!')
    elif ( checkDate(dead_line_year, dead_line_month, dead_line_day) != True ):
        return template('main_timetable_change', message='不正な値です!!')
    else:
        day = toStringDate(dead_line_year, dead_line_month, dead_line_day)
        if (add_time_table_change(day, time, subject) == True):
            return template('main_timetable', message='追加しました!')
        else:
            return template('main_timetable_change', message='失敗しました!')
        return redirect('/時間割', message='')

# イベント管理
# イベント一覧表示
@route('/event')
def event_views():
    get_event_list(toDay())
    return template('main_event', message = '')

# イベント追加
@route('/event/add')
def event_add_views():
    return template('main_event_add', message = '')

@post('/event/add')
def event_add():
    contents = request.forms.comment
    dead_line_year = int( request.forms.get("year") )
    dead_line_month = int( request.forms.get("month") )
    dead_line_day = int( request.forms.get("day") )

    # 入力値判定
    if (contents == ''):
        return template('main_event_add', message='不正な値です!!')
    elif ( checkDate(dead_line_year, dead_line_month, dead_line_day) != True ):
        return template('main_event_add', message='不正な値です!!')
    else:
        day = toStringDate(dead_line_year, dead_line_month, dead_line_day)
        if (add_event(day, contents) == True):
            return template('main_event', message='追加しました!')
        else:
            return template('main_event_add', message='失敗しました!')
        return redirect('/event', message='')


# error
@error(404)
def error404(error):
    return template('error')


# これより下は基本的に触らなくて良い
# PATH設定
@route('/css/<filename>')
def route_css(filename):
    return static_file(filename, root='css/', mimetype='text/css')

@route('/js/<filename>')
def route_js(filename):
    return static_file(filename, root='js/', mimetype='text/javascript')

@route('/fonts/<filename>')
def route_fonts(filename):
    return static_file(filename, root='fonts')

@route('/images/<filename>')
def route_js(filename):
    return static_file(filename, root='views/images/')

@route('/db/<filename>')
def route_fonts(filename):
    return static_file(filename, root='db/')

# build in server
run(host='localhost', post=8080, debug=True)
