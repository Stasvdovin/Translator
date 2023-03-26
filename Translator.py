import streamlit as st
from transformers import pipeline
# Создаем модель для перевода текста
translator = pipeline(model="Helsinki-NLP/opus-mt-ru-en")
# Формируем заголовок для браузера
st.title("Приложения для перевода текста с русского на англиский язык")
# Строчка для ввода текста 
name = st.text_input("Введите текст на русском языке ", value ="")
# Сделаем функцию для перевода текста
@functools.cache
def text_perevod(name):
    return translator(name)
# Кнопка отправки ответа и вывода результата
if (st.button('Отправить')):
    result = text_perevod(name)
    st.success(result)
