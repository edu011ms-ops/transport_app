import streamlit as st

st.set_page_config(layout="centered")

st.title("Gerador de Imagens")

# estado para controlar se já clicou
if "mostrar" not in st.session_state:
    st.session_state.mostrar = False

if "imagem_atual" not in st.session_state:
    st.session_state.imagem_atual = 1

# estilo do botão
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

# botão principal
st.markdown('<div class="center">', unsafe_allow_html=True)

if st.button("GERAR IMAGEM"):
    st.session_state.mostrar = True

st.markdown('</div>', unsafe_allow_html=True)

# mostrar imagem
if st.session_state.mostrar:
    
    # escolher imagem
    if st.session_state.imagem_atual == 1:
        st.image("foto1.png", use_container_width=True)
    else:
        st.image("foto2.png", use_container_width=True)

    # botão "OU"
    if st.button("OU"):
        # alterna imagem
        if st.session_state.imagem_atual == 1:
            st.session_state.imagem_atual = 2
        else:
            st.session_state.imagem_atual = 1

        st.rerun()
