import datetime 

class Lists:

    def __init__(self, name):
        self.name = name
        self.entries = []
        
    def entries_count(self):
        return len(self.entries)

    def show_name(self):
        print(self.name)
    
class Entry:
    
    id = 0

    def __init__(self, memo, tags=None):
        self.memo = memo
        self.tags = tags
        self.create_date = datetime.datetime.today()
        Entry.id += 1
        self.id = Entry.id 
        self.completed = False


class Reminder:

    def __init__(self, priority=0):
        self.priority = priority
        self.date_reminder = None 
        self.time_reminder = None 

    def remind_on_date(self, date):
        self.date_reminder = date

    def remind_at_time(self, time):
        self.time_reminder = time  



        





