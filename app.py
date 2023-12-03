import streamlit as st
from PIL import Image


def preload_content():
    """ preload content used in web app """

    bank = Image.open('data/bank.jpg')
    target = Image.open('data/Target.png')
    age = Image.open('data/Age.png')
    cat = Image.open('data/Categorical.png')
    numer = Image.open('data/Numeric.png')
    numer_dep = Image.open('data/Numeric_depend.png')
    corr = Image.open('data/Matrix_corr.png')

    return bank, target, age, cat, numer, numer_dep, corr


def render_page(bank, target, age, cat, numer, numer_dep, corr):
    """ creates app page with tabs """

    st.title('Склонность к отклику на предложение банка')
    st.subheader('Исследуем данные, предсказываем отклик, оцениваем важность факторов')
    st.write('Материал - данные клиентов банка')
    st.image(bank)

    tab1, tab2, tab3 = st.tabs([':mag: Исследовать', ':mage: Предсказать', ':vertical_traffic_light: Оценить'])

    with tab1:
        st.write('Exploratory data analysis: исследуем наши данные, предварительно очищенные и обработанные :sparkles:')

        st.write('**Целевая переменная - отклик**')
        st.image(target)
        st.write('Клиенты гораздо чаще отказываются от услуги')
        st.write('В задаче имеется дисбаланс классов')
        st.divider()

        st.write('**Возраст клиентов**')
        st.image(age)
        st.write('Минимальный возраст - 20 лет')
        st.write('Самый распространённый возраст - от 20 до 40 лет')
        st.divider()

        st.write('**Категориальные признаки:** пол, статус работы и статус пенсии')
        st.image(cat)
        st.write('Среди клиентов: мужчин вдвое больше, чем женщин')
        st.write('Большиство клиентов работают и не получают пенсию')
        st.divider()

        st.write('**Числовые характеристики**')
        st.image(numer)
        st.write('Средний возраст 40 лет')
        st.write('Средняя зарплата 14 000')
        st.divider()

        st.write('**Зависимости числовых признаков**')
        st.image(numer_dep)
        st.write('Количество ссуд положительно коррелирует с количеством погашенных ссуд')
        st.write('Количество детей положительно коррелирует с количеством иждивенцев')
        st.divider()

        st.write('**Матрица корреляций числовых признаков**')
        st.image(corr)
        st.write('Количество ссуд положительно коррелирует с количеством погашенных ссуд')
        st.write('Занятость клиентов отрицательно коррелирует с выходом на пенсию')
        st.write('Отклик имеет наибольшую корреляцию с возрастом')
        st.divider()

    with tab2:
        pass

    with tab3:
        pass


def load_page():
    """ loads main page """

    bank, target, age, cat, numer, numer_dep, corr = preload_content()

    st.set_page_config(layout="wide",
                       page_title="Отклики на услуги банка",
                       page_icon=':bank:')

    render_page(bank, target, age, cat, numer, numer_dep, corr)


if __name__ == "__main__":
    load_page()
