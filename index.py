from bottle import *
from module import *
#from bottle import route, run, template, request

@route('/')
def top():
    return template('top')

# 課題管理
@route('/task')
def task_views():
    return template('main_task')

# 課題追加
@route('/task/add')
def task_add_views():
    return template('main_task_add', message='')

@post('/task/add')
def task_add():
    subject = request.forms.get("subject")
    contents = request.forms.get("comment")
    dead_line_year = int( request.forms.get("year") )
    dead_line_month = int( request.forms.get("month") )
    dead_line_day = int( request.forms.get("day") )

    # 入力値判定
    if (subject == ''):
        return template('main_task_add', message='不正な値です!!')
    elif (contents == ''):
        return template('main_task_add', message='不正な値です!!')
    elif (checkDate(dead_line_year, dead_line_month, dead_line_day) != True):
        return template('main_task_add', message='不正な値です!!')
    else:
        # ここに投げ込むメソッド名とかプログラム
        return 'success'


# 授業管理
@route('/時間割')
def time_table_view():
    return template('main_timetable')




@route('/hello/<name>')
def hello_test(name="trompot"):
    return template('login', name=name)

# error
@error(404)
def error404(error):
    return template('error')

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

# build in server
run(host='localhost', post=8080, debug=True)
