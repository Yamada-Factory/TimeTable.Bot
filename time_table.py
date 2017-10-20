import csv
import datetime
import setting as fs


# 与えられた日付の時間割を返す
# 日付が不正ならNoneを返す
# 休みなどで時間割がなければ空リストを返す
def get_time_table(date):
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
    change_list = get_time_table_change_all()
    change = list()
    if date in change_list:
        change = change_list[date]

    # イベントを読み込む
    event_list = get_event(date)

    week = {'月曜': 0, '火曜': 1, '水曜': 2, '木曜': 3, '金曜': 4}
    table_event = ''
    # if '休み' in event_list:
    #     table_event = '休み'

    for e in event_list:
        if e.event == '休み':
            table_event = e
            break
        for d in week.keys():
            if e.event == d:
                table_event = e.event
                break
    week_point = input_date.weekday()

    if table_event == '休み' or week_point >= 5:
        return []
    elif table_event != '':
        week_point = week[table_event]

    for e in change:
        times = e.time.split('.')
        for t in times:
            table[week_point][int(t)-1] = e.subject
    return table[week_point]


# 要求された日付にある課題を返す(list<Task>)
# なければ空リスト
def get_task(date):
    task_list = get_task_list_all()
    if date in task_list:
        return task_list[date]
    return []


# 要求された日付以降にある課題を返す(list<list<Task>>)
# なければ空リスト
def get_task_list(date):
    task_list = get_task_list_all()
    out_list = list()
    for d in task_list.keys():
        if d >= date:
            out_list.append(task_list[d])
    return out_list


# task.csv内にある課題をすべて取得する(dict<日付:string, list<string>>)
# なければ空dict
def get_task_list_all():
    with open(fs.TASK, 'r') as f:
        reader = csv.reader(f)
        task_list = dict()
        for row in reader:
            if len(row) < 3:
                continue
            if row[0] in task_list:
                task_list[row[0]].append(Task(row[0], row[1], row[2]))
            else:
                task_list[row[0]] = [Task(row[0], row[1], row[2])]
        return task_list


# 要求された日付にあるイベントを返す(list<Event>)
# なければ空リスト
def get_event(date):
    event_list = get_event_list_all()
    if date in event_list:
        return event_list[date]
    return []


# 要求された日付以降にあるイベントを返す(list<list<Event>>)
# なければ空リスト
def get_event_list(date):
    event_list = get_event_list_all()
    out_list = list()
    for d in event_list.keys():
        if d >= date:
            out_list.append(event_list[d])
    return out_list


# event.csv内にある全てのイベントのdict<日付:string, list<Event>>を返す
# なければ空dict
def get_event_list_all():
    with open(fs.EVENT, 'r') as f:
        reader = csv.reader(f)
        event_list = dict()
        for row in reader:
            if len(row) < 2:
                continue
            if row[0] in event_list:
                event_list[row[0]].append(Event(row[0], row[1]))
            else:
                event_list[row[0]] = [Event(row[0], row[1])]
        return event_list


# time_table_change.csv内にある全ての変更を返す(dict<日付:string, list<Change>>)
# なければ空dict
def get_time_table_change_all():
    with open(fs.CHANGE, 'r') as f:
        reader = csv.reader(f)
        change_list = dict()
        for row in reader:
            if len(row) < 3:
                continue
            if row[0] in change_list:
                change_list[row[0]].append(Change(row[0], row[1], row[2]))
            else:
                change_list[row[0]] = [Change(row[0], row[1], row[2])]
        return change_list


# 時間割変更をcsvに追記する
# 成功ならTrueを返す
def add_time_table_change(date, time, subject):
    if not check_date(date):
        return False
    table_change = get_time_table_change_all()
    change = Change(date, time, subject)
    if date in table_change:
        for e in table_change[date]:
            if e == change:
                return False
        table_change[date].append(change)
    else:
        table_change[date] = [change]

    # list(2次元)に変換
    out = list()
    for key in sorted(table_change.keys()):
        for e in table_change[key]:
            out.append([key, e.time, e.subject])

    with open(fs.CHANGE, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out)
    return True


# イベントをcsvに追記する
# 成功ならTrueを返す
def add_event(date, event):
    if not check_date(date):
        return False
    event_list = get_event_list_all()
    if date in event_list:
        for e in event_list[date]:
            if e.event == event:
                return False
        event_list[date].append(Event(date, event))
    else:
        event_list[date] = [Event(date, event)]

    out = list()
    for key in sorted(event_list.keys()):
        for e in event_list[key]:
            out.append([key, e.event])

    with open(fs.EVENT, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out)
    return True


# 課題をcsvに追記する
# 成功ならTrueを返す
def add_task(date, subject, value):
    if not check_date(date):
        return False
    task_list = get_task_list_all()
    task = Task(date, subject, value)
    if date in task_list:
        for e in task_list[date]:
            if e == task:
                return False
        task_list[date].append(task)
    else:
        task_list[date] = [task]

    out = list()
    for key in sorted(task_list.keys()):
        for e in task_list[key]:
            out.append([key, e.subject, e.value])

    with open(fs.TASK, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out)
    return True


# 未実装
# def delete_time_table_change(date, time, subject):
# def delete_event(date, event):
# def delete_task(date, subject, value):

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
    return out


# 課題を文字列に変換する
def task_string(data):
    if len(data) == 0:
        return 'なし'
    out = ''
    for e in data:
        out += e.subject+' '+e.value+'\n'
    return out


# 課題リストを文字列に変換する
def task_list_string(data):
    if len(data) == 0:
        return 'なし'
    out = ''
    for e in data:
        out += e[0].date+' '
        for t in e:
            out += t.subject+' '+t.value+' '
        out += '\n'
    return out


# イベントを文字列に変換する
def event_string(data):
    if len(data) == 0:
        return 'なし'
    out = ''
    for e in data:
        out += e.value+'\n'
    return out


# イベントリストを文字列に変換する
def event_list_string(data):
    if len(data) == 0:
        return 'なし'
    out = ''
    for e in data:
        out += e[0].date+' '
        for t in e:
            out += t.event+' '
        out += '\n'
    return out


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
def get_date(str):
    if str == '今日':
        return datetime.datetime.today().strftime('%Y/%m/%d')
    if str == '明日':
        return (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y/%m/%d')
    if str == '明後日':
        return (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y/%m/%d')
    return str


class Task:
    def __init__(self, date, subject, value):
        self.date = date
        self.subject = subject
        self.value = value

    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        return self.__dict__ == other.__dict__

    def __str__(self):
        return 'task[date='+self.date+', subject='+self.subject+', value='+self.value+']'

    def get_list(self):
        return [self.subject, self.value]


class Change:
    def __init__(self, date, time, subject):
        self.date = date
        self.time = time
        self.subject = subject

    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        return self.__dict__ == other.__dict__

    def get_list(self):
        return [self.time, self.subject]

class Event:
    def __init__(self, date, event):
        self.date = date
        self.event = event
        
