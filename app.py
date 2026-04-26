import streamlit as st

st.set_page_config(layout="centered")

st.title("Exibir Imagem")

# CSS para centralizar e aumentar botão
st.markdown("""
    <style>
    .center {
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }
    div.stButton > button {
        width: 300px;
        height: 100px;
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

# centralizar botão
st.markdown('<div class="center">', unsafe_allow_html=True)

clicou = st.button("MOSTRAR IMAGEM")

st.markdown('</div>', unsafe_allow_html=True)

# quando clicar
if clicou:
    st.image("foto1.png", caption="Minha imagem", use_container_width=True)