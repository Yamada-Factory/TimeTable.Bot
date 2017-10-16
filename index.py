from bottle import *
import datetime
#from bottle import route, run, template, request

@route('/')
def top():
    return template('main_timetable')

# 課題管理
@route('/task')
def task_views():
    return template('main_task')

# 課題追加
@post('/task/add')
def task_add():
    return 0;

@route('/task/add')
def task_add_views():
    return template('main_task_add')

# 課題追加確認
@post('/task/add/check')
def task_add_cheak():
    subject = request.forms.get("subject")
    contents = request.forms.get("comment")
    dead_line_year = int( request.forms.get("year") )
    dead_line_month = int( request.forms.get("month") )
    dead_line_day = int( request.forms.get("day") )

    def checkDate(year, month, day):
        try:
            newDataStr="%04d/%02d/%02d"%(year,month,day)
            newDate=datetime.datetime.strptime(newDataStr,"%Y/%m/%d")
            return True
        except ValueError:
            return False

    if (subject == ''):
        return template('error')
    elif (contents == ''):
        return template('error')
    elif (checkDate(dead_line_year, dead_line_month, dead_line_day) != True):
        return template('error')
    else:
        return 'NONO'


#@route('/task/add')


#
# @route('/hello')
# def hello():
#     return "Hello World!"
#
# @route('/hello/<user>')
# def hello(user="taro"):
#     return "Hello {user}".format(user=user)
#
# @route('/test')
# def test():
#     return '''
#     <html>
#         <head></head>
#         <body>
#             <a href="http://www.google.co.jp">Google</a>
#         </body>
#     </html>
#     '''
#

@route('/hello/<name>')
#@view('login')
def hello_test(name="trompot"):
    return template('login', name=name)



# error
@error(404)
def error404(error):
    return "{error}".format(error=error)

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


# build in server
run(host='localhost', post=8080, debug=True)
