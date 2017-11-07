import line_api
import json
import setting
import sys
import signal
import processing_input
from bottle import *
from module import *
from string_changer import *

# SSLサーバ設定
class SSLWebServer(ServerAdapter):
    def run(self, handler):
        from gevent.pywsgi import WSGIServer
        srv = WSGIServer((self.host, self.port), handler,
                         certfile=setting.CERT_FILE,
                         keyfile=setting.KEY_FILE,
                         ca_certs=setting.CA_FILE)
        srv.serve_forever()

# WebController
# 翌日の時間割及び課題の表示
@get('/')
def top():
    date = tomorrow_Day() #5時間割後の日付取得
    time = get_time_table(date) # 時間割取得
    event = event_string(get_event(date)) # イベント取得
    task = today_task(date)

    if( len(time) == 0):
        return template('top', time='', task = '', today = date, message = 'はお休みです．', event = event)
    else:
        return template('top', time = time, task = task, today = date, message = ' ', event = event)

# 課題管理
# 課題一覧表示
@get('/task')
def task_views():
    task = all_task()
    length = len(task)
    return template('main_task', message = '', task = task, length = length)

# 課題追加
@get('/task/add')
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
            return template('main_task', message='追加しました!', task=all_task(), length=len(all_task()))
        else:
            return template('main_task_add', message='失敗しました!')
        return redirect('/task', message='')


# 授業管理
# 時間割表示(mobile非対応)
@get('/時間割')
def time_table_view():
    return template('main_timetable', message='')

# 時間割変更
@get('/時間割/変更')
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
@get('/event')
def event_views():
    event = referenceEvent()
    length = len(event)
    return template('main_event', message = '', event = event, length = length)

# イベント追加
@get('/event/add')
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
            return template('main_event', message='追加しました!', event = referenceEvent(), length = len(referenceEvent()) )
        else:
            return template('main_event_add', message='失敗しました!')
        return redirect('/event', message='')


# error
# @error(404)
# def error404(error):
#     return template('error')


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


@post('/TimeTable.Bot')
def line_post():
    signature = request.get_header('X-Line-Signature')
    body = request.body.read().decode('utf-8')
    if not line_api.signature_check(body, signature):
        return

    events = json.loads(body)['events']
    processing_input.processing_input(events)
#    print('end')
    body = json.dumps({})
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

def handler(signal, frame):
        line_api.push_message(setting.ID, ['停止'])
        sys.exit(0)
signal.signal(signal.SIGINT, handler)
line_api.push_message(setting.ID, ['起動'])

# build in server
run(host='0.0.0.0', port=4460, server=SSLWebServer, debug=True, reloader=True)
