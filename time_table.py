import csv
from datetime import datetime
import setting as fs


# 与えられた日付の時間割を返す
# 日付が不正ならNoneを返す
# 休みなどで時間割がなければ空リストを返す
def get_time_table(date):
    try:
        input_date = datetime.strptime(date, '%Y/%m/%d')
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
    event_list = get_event_list(date)

    week = {'月曜': 0, '火曜': 1, '水曜': 2, '木曜': 3, '金曜': 4}
    table_event = ''
    for e in event_list:
        if e == '休み':
            table_event = e
            break
        for d in week.keys():
            if e == d:
                table_event = e
                break
    week_point = input_date.weekday()

    if table_event == '休み':
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
            if row[0] in task_list:
                task_list[row[0]].append(Task(row[0], row[1], row[2]))
            else:
                task_list[row[0]] = [(row[0], row[1], row[2])]
        return task_list


# 要求された日付にあるイベントを返す(list<string>)
# なければ空リスト
def get_event(date):
    event_list = get_event_list_all()
    if date in event_list:
        return event_list[date]
    return []


# 要求された日付以降にあるイベントを返す(list<list<string>>)
# なければ空リスト
def get_event_list(date):
    event_list = get_event_list_all()
    out_list = list()
    for d in event_list.keys():
        if d >= date:
            out_list.append(event_list[d])
    return out_list


# event.csv内にある全てのイベントのdict<日付:string, list<string>>を返す
# なければ空dict
def get_event_list_all():
    with open(fs.EVENT, 'r') as f:
        reader = csv.reader(f)
        event_list = dict()
        for row in reader:
            if row[0] in event_list:
                event_list[row[0]].append(row[1])
            else:
                event_list[row[0]] = [row[1]]
        return event_list


# time_table_change.csv内にある全ての変更を返す(dict<日付:string, list<Change>>)
# なければ空dict
def get_time_table_change_all():
    with open(fs.CHANGE, 'r') as f:
        reader = csv.reader(f)
        change_list = dict()
        for row in reader:
            if row[0] in change_list:
                change_list[row[0]].append(Change(row[0], row[1], row[2]))
            else:
                change_list[row[0]] = Change(row[0], row[1], row[2])
        return change_list


def add_time_table_change(date, time, subject):
    table_change = get_time_table_change_all()
    change = Change(date, time, subject)
    if date in table_change:
        for e in table_change[date]:
            if e == change:
                return
        table_change[date].append(change)
    else:
        table_change[date] = [change]

    # list(2次元)に変換
    out = list()
    for key, value in table_change.items():
        for e in value:
            out.append([key, e.time, e.subject])

    with open(fs.CHANGE, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out)


def add_event(date, event):
    event_list = get_event_list_all()
    if date in event_list:
        for e in event_list[date]:
            if e == event:
                return
        event_list[date].append(event)
    else:
        event_list[date] = [event]

    out = list()
    for key, value in event_list.items():
        for e in value:
            out.append([key, e])

    with open(fs.EVENT, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out)


def add_task(date, subject, value):
    task_list = get_task_list_all()
    task = Task(date, subject, value)
    if date in task_list:
        for e in task_list[date]:
            if e == task:
                return
        task_list[date].append(task)
    else:
        task_list[date] = [task]

    out = list()
    for key, value in task_list.items():
        for e in value:
            out.append([key, e.subject, e.value])

    with open(fs.TASK, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out)


# 未実装
# def delete_time_table_change(date, time, subject):
# def delete_event(date, event):
# def delete_task(date, subject, value):

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


def check_date(date):
    try:
        datetime.strptime(date, '%Y/%m/%d')
        return True
    except ValueError:
        print("誤った日付です")
        return False


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
