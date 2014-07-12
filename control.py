__author__ = 'cshroba'

import model


def get_note(id):
    return "Note %s: %s" % (id, model.get_note(id) )# this is like printf in c++ of java


def save_note(id, note):
    return model.save_note(id, note)