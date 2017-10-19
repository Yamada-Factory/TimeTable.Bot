import datetime
from time_table import *

def checkDate(year, month, day):
    try:
        newDataStr="%04d/%02d/%02d"%(year,month,day)
        newDate=datetime.datetime.strptime(newDataStr,"%Y/%m/%d")
        return True
    except ValueError:
        return False

def toStringDate(year, month, day):
    return ('{}/{}/{}'.format(year, month, day))

def toDay():
    today = datetime.date.today()
    return toStringDate(today.year, today.month, today.day)

def tomorrow_Day():
    tomorrow = datetime.datetime.now() + datetime.timedelta(hours = 9)
    return toStringDate(tomorrow.year, tomorrow.month, tomorrow.day)

def referenceTask(date):
    # dateの課題及び授業取得
    date_task = get_task(date)
    date_time = get_time_table(date)

    task_the_Day = []

    # subjectに課題内容を代入する
    for i in range(len(date_task)):
        for j in range(len(date_time)):
            if(date_task[i].subject == date_time[j]):
                task_the_Day.append(date_task[i].value)
            else:
                task_the_Day.append('')
    return task_the_Day
