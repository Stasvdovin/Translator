import streamlit as st
from transformers import pipeline
# Создаем модель для перевода текста
translator = pipeline(model="Helsinki-NLP/opus-mt-ru-en")
# Формируем заголовок для браузера
st.title("Приложения для перевода текста с русского на англиский язык")
# Строчка для ввода текста 
name = st.text_area("Введите текст на русском языке ", value ="")
# Сделаем функцию для перевода текста
def text_perevod(name):
    return translator(name)
# Строчка для вывода Перевода 
st.text_area('Перевод на английском языке', value = text_perevod(name), disabled = False)