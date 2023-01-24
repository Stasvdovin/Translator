from Translator.py import name
def name():
    assert name('как дела') == 'How you doing?'
    assert name('на уличе идет дождь') == "It's raining in the street."
