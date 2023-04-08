import streamlit as st
from transformers import pipeline


# Создаем модель для перевода текста
@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline(model="Helsinki-NLP/opus-mt-ru-en")


translator = load_model()

# Формируем заголовок для браузера
st.title("Приложения для перевода текста с русского на англиский язык")
# Строчка для ввода текста
enter_text = st.text_input("Введите текст на русском языке ", value="")


# Сделаем функцию для перевода текста
def text_perevod(enter_text):
    return translator(enter_text)


# Кнопка отправки ответа и вывода результата
def new_func(enter_text, text_perevod):
    if st.button("Отправить"):
        result = text_perevod(enter_text)
        st.success(result)


new_func(enter_text, text_perevod)
