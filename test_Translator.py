from Translator import text_perevod
def test_text_perevod():
    assert text_perevod('как дела') == 'How you doing?'
    assert text_perevod('на уличе идет дождь') == "It's raining in the street."
