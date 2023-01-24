import streamlit as st
from transformers import pipeline
# Создаем модель для перевода текста
translator = pipeline(model="Helsinki-NLP/opus-mt-ru-en")
# Формируем заголовок для браузера
st.title("Приложения для перевода текста с русского на англиский языки")
# Строчка для ввода текста 
name = st.text_input("Введите текст")
# Кнопка для вывода результата 
if(st.button('Отправить')):
    result = translator(name)
    st.success(result)
