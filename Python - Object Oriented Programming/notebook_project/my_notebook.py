import datetime 

# stores the value of the last note_id

last_id = 0 

class Note:
    """A Note object that will be stored in a Notebook. Match string in memo 
    or in tags.
    """

    def __init__(self, memo, tags=""):
        """initialize a note with a memo and optional tags.
        """

        self.memo = memo
        self.tags = tags 
        self.creation_date = datetime.date.today()
        
        global last_id 
        last_id += 1
        self.id = last_id 

    def match(self, filter):
        """Check if note matches filter text. Return True for match, otherwise False.
        """
        return filter in self.memo or filter in self.tags 

class Notebook:
    """A collection of notes that can be tagged, modified or searched.
    """

    def __init__(self):
        """Initialize an empty notebook.
        """
        self.notes = []

    def new_note(self, memo, tags=""):
        """Create a new note and add it to the notebook list.
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None 

    def modify_memo(self, note_id, memo):
        """Find a note by id and change the memo.
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False 
    
    def modify_tags(self, note_id, tags):
        """Find the note by id and change its tags.
        """
        self._find_note(note_id).tags = tags 
    
    def search(self, filter):
        """Find all notes that match a given filter string."""
        return [note for note in self.notes if note.match(filter)]