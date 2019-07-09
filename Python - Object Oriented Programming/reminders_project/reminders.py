import datetime 

class Lists:

    entry_id = 0

    def __init__(self, name):
        self.name = name
        self.entries = []
        
    def entries_count(self):
        return len(self.entries)

    def show_list_name(self):
        print(self.name)

    def add_entry(self, memo, tags=None):
        Lists.entry_id += 1 
        entry = Entry(memo, tags)
        entry.entry_id = Lists.entry_id
        self.entries.append(entry)

    
class Entry:

    def __init__(self, memo, tags=None):
        self.memo = memo
        self.tags = tags
        self.create_date = datetime.datetime.today()
        self.completed = False
        self.entry_id = 0

    def match(self, filter):
        return filter in self.memo or filter in self.tags


class Reminder:

    def __init__(self, priority=0):
        self.priority = priority
        self.date_reminder = None 
        self.time_reminder = None 

    def remind_on_date(self, date):
        self.date_reminder = date

    def remind_at_time(self, time):
        self.time_reminder = time  



        





