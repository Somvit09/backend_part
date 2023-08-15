from .handler import *


def kickoff_database_tasks(email, res):
    response_json = res.json()
    hack_dictionary = response_json
    is_email_stored = add_email(email)
    is_hack_stored = add_hack(hack_dictionary)
    if is_hack_stored and is_email_stored:
        map_email_hacks(email, hack_dictionary)
    else:
        raise IndexError('Email or Hack was not stored properly')
