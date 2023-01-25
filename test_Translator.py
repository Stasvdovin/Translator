# Проведем проверку функции перевода текста 
from Translator import text_perevod
def test_text_perevod():
    assert text_perevod('Хорошая погода') == [{'translation_text': 'Good weather.'}]
    assert text_perevod('сегодня идет дождь') == [{'translation_text': "It's raining today."}]
    
