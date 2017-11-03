import csv
import datetime
import setting as fs
import sqlite3
from data_objects import *
=======
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a


# 与えられた日付の時間割を返す
# 日付が不正ならNoneを返す
# 休みなどで時間割がなければ空リストを返す
def get_time_table(date):
    date = get_date(date)
    try:
        input_date = datetime.datetime.strptime(date, '%Y/%m/%d')
    except ValueError:
        print("誤った日付です")
        return None

    # デフォルトの時間割を読み込む
    with open(fs.TIME_TABLE, 'r') as f:
        table = []
        reader = csv.reader(f)
        for row in reader:
            table.append(row)

    # 時間割変更を読み込む
    change_list = get_time_table_change(date)

    # イベントを読み込む
    event_list = get_event(date)

    week = {'月曜': 0, '火曜': 1, '水曜': 2, '木曜': 3, '金曜': 4}
    table_event = ''

    for e in event_list:
        if e.event == '休み' or e.event == '時間割なし':
            table_event = '時間割なし'
            break
        for d in week.keys():
            if e.event == d:
                table_event = e.event
                break
    week_point = input_date.weekday()

    if table_event == '時間割なし' or week_point >= 5:
        return []
    elif table_event != '':
        week_point = week[table_event]

    for e in change_list:
        times = e.time.split('.')
        for t in times:
            table[week_point][int(t)-1] = e.subject
    return table[week_point]


# 要求された日付にある課題を返す(list<Task>)
# なければ空リスト
def get_task(date):
    tasks = access("SELECT * FROM task WHERE date = '{}'".format(get_date(date)))
    out = list()
    for task in tasks:
        out.append(Task(task))
    return out


# 要求された日付以降にある課題を返す(list<list<Task>>)
# なければ空リスト
def get_task_list(date):
    tasks = get_task_dict(date)
    out = list()
    for d in sorted(tasks.keys()):
        out.append(tasks[d])
    return out


# 要求された日付以降にある課題を返す(list<list<Task>>)
# なければ空リスト
def get_task_dict(date):
<<<<<<< HEAD
    date_list = access("SELECT DISTINCT date FROM task WHERE date >= '{}'".format(get_date(date)))
    task_dict = dict()
    for d in date_list:
        task_dict[d[0]] = list()
    tasks = access("SELECT * FROM task WHERE date >= '{}' ORDER BY date ASC ".format(get_date(date)))
=======
    date_list = access("SELECT DISTINCT date FROM task WHERE date >= '{}'".format(format_date(get_date(date))))
    task_dict = dict()
    for d in date_list:
        task_dict[d[0]] = list()
    tasks = access("SELECT * FROM task WHERE date >= '{}' ORDER BY date ASC ".format(format_date(get_date(date))))
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a
    for task in tasks:
        task_dict[task[0]].append(Task(task))
    return task_dict


# 要求された日付以降にある課題を返す(list<Task>)
# なければ空リスト
def get_task_list_one(date):
<<<<<<< HEAD
    tasks = access("SELECT * FROM task WHERE date >= '{}' ORDER BY date ASC ".format(get_date(date)))
=======
    tasks = access("SELECT * FROM task WHERE date >= '{}' ORDER BY date ASC ".format(format_date(get_date(date))))
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a
    out = list()
    for task in tasks:
        out.append(Task(task))
    return out


# 要求された日付にあるイベントを返す(list<Event>)
# なければ空リスト
def get_event(date):
    events = access("SELECT * FROM event WHERE date = '{}'".format(date))
    out = list()
    for event in events:
        out.append(Event(event))
    return out


# 要求された日付以降にある課題を返す(list<list<Task>>)
# なければ空リスト
def get_event_dict(date):
<<<<<<< HEAD
    event_list = access("SELECT DISTINCT date FROM event WHERE date >= '{}'".format(get_date(date)))
    event_dict = dict()
    for d in event_list:
        event_dict[d[0]] = list()
    tasks = access("SELECT * FROM event WHERE date >= '{}' ORDER BY date ASC ".format(get_date(date)))
=======
    event_list = access("SELECT DISTINCT date FROM event WHERE date >= '{}'".format(format_date(get_date(date))))
    event_dict = dict()
    for d in event_list:
        event_dict[d[0]] = list()
    tasks = access("SELECT * FROM event WHERE date >= '{}' ORDER BY date ASC ".format(format_date(get_date(date))))
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a
    for event in tasks:
        event_dict[event[0]].append(Event(event))
    return event_dict


# 要求された日付以降にあるイベントを返す(list<list<Event>>)
# なければ空リスト
def get_event_list(date):
<<<<<<< HEAD
    events = get_event_dict(date)
=======
    events = get_task_dict(date)
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a
    out = list()
    for d in sorted(events.keys()):
        out.append(events[d])
    return out


# 要求された日付以降にあるイベントを返す(list<Event>)
# なければ空リスト
def get_event_list_one(date):
<<<<<<< HEAD
    events = access("SELECT * FROM event WHERE date >= '{}' ORDER BY date ASC ".format(get_date(date)))
=======
    events = access("SELECT * FROM event WHERE date >= '{}' ORDER BY date ASC ".format(format_date(get_date(date))))
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a
    out = list()
    for event in events:
        out.append(Event(event))
    return out


# time_table_change内にある変更を返す(list<Change>)
# なければ空リスト
def get_time_table_change(date):
<<<<<<< HEAD
    changes = access("SELECT * FROM time_table_change WHERE date = '{}'".format(get_date(date)))
=======
    changes = access("SELECT * FROM time_table_change WHERE date = '{}'".format(format_date(get_date(date))))
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a
    out = list()
    for change in changes:
        out.append(Change(change))
    return out


# 時間割変更をdbに追記する
# 成功ならTrueを返す
def add_time_table_change(date, time, subject):
    try:
<<<<<<< HEAD
        access('INSERT INTO time_table_change(date, time, subject) VALUES {}'.format((get_date(date), time, subject)))
=======
        access('INSERT INTO time_table_change(date, time, subject) VALUES {}'.format((format_date(get_date(date)), time, subject)))
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a
        return True
    except sqlite3.IntegrityError:
        return False


# イベントをdbに追記する
# 成功ならTrueを返す
def add_event(date, event):
    try:
<<<<<<< HEAD
        access("INSERT INTO event(date, event) VALUES {}".format((get_date(date), event)))
        return True
    except sqlite3.IntegrityError:
        return False


=======
        access("INSERT INTO event(date, value) VALUES {}".format((format_date(get_date(date)), event)))
        return True
    except sqlite3.IntegrityError:
        return False


>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a
# 課題をdbに追記する
# 成功ならTrueを返す
def add_task(date, subject, value):
    try:
<<<<<<< HEAD
        access('INSERT INTO task(date, subject, value) VALUES {}'.format((get_date(date), subject, value)))
    except sqlite3.IntegrityError:
        return False


# 時間割変更をdbから削除する
# 成功ならTrueを返す
def delete_time_table_change(date, time, subject):
    access("DELETE FROM time_table_change WHERE date == '{}' AND time == '{}' AND subject == '{}'".format(get_date(date), time, subject))


# イベントをdbから削除する
# 成功ならTrueを返す
def delete_event(date, event):
    access("DELETE FROM event WHERE date == '{}' AND event == '{}'".format(get_date(date), event))


# 課題をdbから削除する
# 成功ならTrueを返す
def delete_task(date, subject, value):
    access("DELETE FROM task WHERE date == '{}' AND subject == '{}' AND value == '{}'".format(get_date(date), subject, value))

=======
        access('INSERT INTO task(date, subject, value) VALUES {}'.format((format_date(get_date(date)), subject, value)))
    except sqlite3.IntegrityError:
        return False


# 時間割変更をdbから削除する
# 成功ならTrueを返す
def delete_time_table_change(date, time, subject):
    access("DELETE FROM time_table_change WHERE date == '{}' AND time == '{}' AND subject == '{}'".format(date, time, subject))


# イベントをdbから削除する
# 成功ならTrueを返す
def delete_event(date, event):
    access("DELETE FROM event WHERE date == '{}' AND value == '{}'".format(date, event))


# 課題をdbから削除する
# 成功ならTrueを返す
def delete_task(date, subject, value):
    access("DELETE FROM task WHERE date == '{}' AND subject == '{}' AND value == '{}'".format(date, subject, value))


# 指定IDの時間割変更をdbから削除する
# 成功ならTrueを返す
def delete_time_table_change_id(id):
    access("DELETE FROM time_table_change WHERE id == {}".format(id))


# 指定IDのイベントをdbから削除する
# 成功ならTrueを返す
def delete_event_id(id):
    access("DELETE FROM event WHERE id == {}".format(id))


# 指定IDの課題をdbから削除する
# 成功ならTrueを返す
def delete_task_id(id):
    access("DELETE FROM task WHERE id == {}".format(id))


# 指定IDの時間割変更を更新する
# 成功ならTrueを返す
def update_time_table_change(id, date, time, subject):
    access("UPDATE time_table_change SET date='{}', time='{}', subject='{}' WHERE id = {}".format(date, time, subject, id))


# 指定IDのイベントを更新する
# 成功ならTrueを返す
def update_event(id, date, event):
    access("UPDATE event SET date='{}', event.='{}' WHERE id = {}".format(date, event, id))


# 指定IDの課題を更新する
# 成功ならTrueを返す
def update_task(id, date, subject, value):
    access("UPDATE task SET date='{}', subject='{}', value='{}' WHERE id = {}".format(date, subject, value, id))


# 時間割リストを文字列に変換する
def time_table_string(time_table):
    if time_table is None:
        return '日付が不正です'
    if len(time_table) == 0:
        return '時間割なし'

    i = 1
    out = '時間割\n'
    for e in time_table:
        if e != 'null':
            out += str(i)+' '+e+'\n'
        else:
            out += str(i)+'\n'
        i += 1
    return out
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a

# 指定IDの時間割変更をdbから削除する
# 成功ならTrueを返す
def delete_time_table_change_id(id):
    access("DELETE FROM time_table_change WHERE id == {}".format(id))


# 指定IDのイベントをdbから削除する
# 成功ならTrueを返す
def delete_event_id(id):
    access("DELETE FROM event WHERE id == {}".format(id))


# 指定IDの課題をdbから削除する
# 成功ならTrueを返す
def delete_task_id(id):
    access("DELETE FROM task WHERE id == {}".format(id))


# 指定IDの時間割変更を更新する
# 成功ならTrueを返す
def update_time_table_change(id, date, time, subject):
    access("UPDATE time_table_change SET date='{}', time='{}', subject='{}' WHERE id = {}".format(get_date(date), time, subject, id))


# 指定IDのイベントを更新する
# 成功ならTrueを返す
def update_event(id, date, event):
    access("UPDATE event SET date='{}', event='{}' WHERE id = {}".format(get_date(date), event, id))


# 指定IDの課題を更新する
# 成功ならTrueを返す
def update_task(id, date, subject, value):
    access("UPDATE task SET date='{}', subject='{}', value='{}' WHERE id = {}".format(get_date(date), subject, value, id))


# 引数の日付の正当性を確かめる
def check_date(date):
    try:
        datetime.datetime.strptime(date, '%Y/%m/%d')
        return True
    except ValueError:
        print("誤った日付です")
        return False


# 今日や明日などの文字列を日付に変換する
# すでに日付ならばそのまま返す
def get_date(date_name):
    if date_name == '今日':
        return datetime.datetime.today().strftime('%Y/%m/%d')
    if date_name == '明日':
        return (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y/%m/%d')
    if date_name == '明後日':
        return (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y/%m/%d')
    if date_name == '明々後日':
        return (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%Y/%m/%d')
    if date_name == '昨日':
        return (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime('%Y/%m/%d')
    if date_name == '来週':
        return (datetime.datetime.today() + datetime.timedelta(days=7)).strftime('%Y/%m/%d')
    return format_date(date_name)


# 与えられた日付を 年4桁/月2桁/日2桁(str) の形式に変換する
def format_date(date):
    d = date.split('/')
    month = d[1] if len(d[1]) == 2 else '0' + d[1]
    day = d[2] if len(d[2]) == 2 else '0' + d[2]
    date_s = '{}/{}/{}'.format(d[0], month, day)
    if check_date(date_s):
        return date_s
    raise ValueError


def access(query):
    connection = sqlite3.connect(fs.SQL)
    cursor = connection.cursor()
    result = cursor.execute(query).fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def data_base_initialize():
    access('''CREATE TABLE task(date text NOT NULL, subject text NOT NULL, value text NOT NULL, id integer PRIMARY KEY NOT NULL, UNIQUE(date, subject, value))''')
<<<<<<< HEAD
    access('''CREATE TABLE event(date text NOT NULL, event text NOT NULL, id integer PRIMARY KEY NOT NULL, UNIQUE(date, event))''')
    access('''CREATE TABLE time_table_change(date text NOT NULL, time text NOT NULL, subject text NOT NULL, id integer PRIMARY KEY NOT NULL, UNIQUE(date, time, subject))''')
=======
    access('''CREATE TABLE event(date text NOT NULL, subject text NOT NULL, value text NOT NULL, id integer PRIMARY KEY NOT NULL, UNIQUE(date, subject, value))''')
    access('''CREATE TABLE time_table_change(date text NOT NULL, time text NOT NULL, subject text NOT NULL, id integer PRIMARY KEY NOT NULL, UNIQUE(date, time, subject))''')


class Task:
    def __init__(self, data):
        self.id = data[3]
        self.date = data[0]
        self.subject = data[1]
        self.value = data[2]

    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        return self.__dict__ == other.__dict__

    def __str__(self):
        return 'task[date='+self.date+', subject='+self.subject+', value='+self.value+']'

    def get_list(self):
        return [self.subject, self.value]


class Change:
    def __init__(self, data):
        self.id = data[3]
        self.date = data[0]
        self.time = data[1]
        self.subject = data[2]

    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        return self.__dict__ == other.__dict__

    def get_list(self):
        return [self.time, self.subject]


class Event:
    def __init__(self, data):
        self.id = data[2]
        self.date = data[0]
        self.event = data[1]

    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        return self.__dict__ == other.__dict__
>>>>>>> 2e525204a120c37f7473aee2c05497fb4693d62a
