import streamlit as st
import pandas as pd
# python -m streamlit run app.py

# ------------------------------------------------- sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Tropa do 7 Cars')



carros = ['Jetta', 'Mercedes', 'Porsche', 'Fusca', 'Toro']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)


# ------------------------------------------------------------------- Principal
st.title('Tropa do 7 - Cars')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}')

if opcao == 'Jetta':
    diaria = 450

if opcao == 'Mercedes':
    diaria = 500

if opcao == 'Porsche':
    diaria = 800

if opcao == 'Fusca':
    diaria = 250

if opcao == 'Toro':
    diaria = 350



if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    alugel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a ser pagado é R${alugel_total:.2f}')