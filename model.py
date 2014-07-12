__author__ = 'cshroba'


# I'm just gonna use a dictionary
# but of course normally you would
# write notes to a file or DB.

notes = {}




def get_note(id):
    if id in notes:
        return notes[id]
    return "NO NOTE FOUND"


def save_note(id, note):
    notes[id] = note
    return id