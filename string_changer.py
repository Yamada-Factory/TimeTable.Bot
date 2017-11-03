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


# 課題を文字列に変換する
def task_string(data):
    if len(data) == 0:
        return 'なし'
    out = '課題\n'
    for e in data:
        out += e.subject+' '+e.value+'\n'
    return out


# 課題リストを文字列に変換する
def task_list_string(data):
    if len(data) == 0:
        return 'なし'
    out = '課題リスト\n'
    for e in data:
        out += e[0].date+' '
        for t in e:
            out += t.subject+' '+t.value+' '
        out += '\n'
    return out


# 課題リストを文字列に変換する(id付き)
def task_list_string_id(data):
    if len(data) == 0:
        return 'なし'
    out = '課題リスト\n'
    for e in data:
        out += e[0].date+' '
        for t in e:
            out += '('+str(t.id)+' '+t.subject+' '+t.value+') '
        out += '\n'
    return out


# イベントを文字列に変換する
def event_string(data):
    if len(data) == 0:
        return 'なし'
    out = 'イベント\n'
    for e in data:
        out += e.event+'\n'
    return out


# イベントリストを文字列に変換する
def event_list_string(data):
    if len(data) == 0:
        return 'なし'
    out = 'イベントリスト\n'
    for e in data:
        out += e[0].date+' '
        for t in e:
            out += t.event+' '
        out += '\n'
    return out


# イベントリストを文字列に変換する(id付き)
def event_list_string_id(data):
    if len(data) == 0:
        return 'なし'
    out = 'イベントリスト\n'
    for e in data:
        out += e[0].date+' '
        for t in e:
            out += '('+str(t.id)+' '+t.event+') '
        out += '\n'
    return out
