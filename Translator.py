import streamlit as st
from transformers import pipeline


@st.cache(allow_output_mutation=True)  # Создаем модель для перевода текста
def load_model():
    return pipeline(model="Helsinki-NLP/opus-mt-ru-en")


translator = load_model()


st.title(
    "Приложения для перевода текста с русского на англиский язык"
)  # Формируем заголовок для браузера
name = st.text_input(
    "Введите текст на русском языке ", value=""
)  # Строчка для ввода текста


def text_perevod(name):  # Сделаем функцию для перевода текста
    return translator(name)


if st.button("Отправить"):  # Кнопка отправки ответа и вывода результата
    result = text_perevod(name)
    st.success(result)
    
