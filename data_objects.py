#!/usr/local/bin/python3
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
