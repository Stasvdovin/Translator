import streamlit as st
from transformers import pipeline
# Создаем модель для перевода текста
translator = pipeline(model="Helsinki-NLP/opus-mt-ru-en")
# Формируем заголовок для браузера
st.title("Приложения для перевода текста с русского на англиский язык")
# Строчка для ввода текста 
name = st.text_area("Введите текст", value ="")
def text_perevod(name):
    return translator(name)
st.text_area('Тут появится перевод.', value = text_perevod(name), disabled = False)