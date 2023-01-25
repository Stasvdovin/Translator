import streamlit as st
from transformers import pipeline
# Создаем модель для перевода текста
@st.cache(allow_output_mutation=True)
def load_model():
    model = pipeline(model="Helsinki-NLP/opus-mt-ru-en")
    return model
translator = model
# Формируем заголовок для браузера
st.title("Приложения для перевода текста с русского на англиский язык")
# Строчка для ввода текста 
name = st.text_input("Введите текст на русском языке ", value ="")
# Сделаем функцию для перевода текста
def text_perevod(name):
    return translator(name)
# Кнопка отправки ответа и вывода результата
if (st.button('Отправить')):
    result = text_perevod(name)
    st.success(result)
