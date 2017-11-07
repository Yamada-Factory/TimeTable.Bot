import line_api
import setting
from time_table import *
from string_changer import *


table = time_table_string(get_time_table(get_date("明日")))
task = task_string(get_task(get_date("明日")))
event = event_string(get_event(get_date("明日")))

line_api.push_message(setting.ID, [table, task, event])
