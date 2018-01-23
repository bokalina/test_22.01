"""Models."""


class Comment(object):
    
    def __init__(self, text, date):
        """Counstructor."""
        self.text = text
        self.date = date
    def __repr__(self):
        return "(text: %s, date: %s)" % (self.text, self.date)

COMMENTS = [
    ("komentar1 ,2018-01-22"), 
    ("kometar2, 2018-01-22"), 
    ("komentar3, 2018-01-22")
]