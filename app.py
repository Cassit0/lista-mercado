import streamlit as st

# 1. INICIALIZAÇÃO (Evita que a lista suma ao clicar)
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

st.title("🛒 Lista de Compras de Ano Novo")

# 2. ENTRADA DE DADOS
with st.expander("➕ Adicionar Novo Item", expanded=True):
    with st.form("novo_item", clear_on_submit=True):
        nome = st.text_input("Nome do item (ex: Champagne, Uva):")
        qtd = st.number_input("Quantidade:", min_value=1, value=1)
        btn_add = st.form_submit_button("Adicionar à Lista")
        
        if btn_add and nome:
            st.session_state.carrinho.append({"nome": nome, "qtd": qtd, "finalizado": False})
            st.rerun()
st.divider()

# 1. CRIAR LISTAS SEPARADAS ANTES DE MOSTRAR NA TELA
# Isso evita que o Streamlit se perca nos índices
itens_pendentes = [i for i in st.session_state.carrinho if not i.get("finalizado", False)]
itens_no_carrinho = [i for i in st.session_state.carrinho if i.get("finalizado", False)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("⏳ Pendentes")
    for item in itens_pendentes:
        # Usamos o nome do item na KEY para ser um identificador único
        if st.checkbox(f"{item['nome']} ({item['qtd']}x)", key=f"p_{item['nome']}"):
            item["finalizado"] = True
            st.rerun()

with col2:
    st.subheader("✅ No Carrinho")
    for item in itens_no_carrinho:
        # Mostra o item riscado. Se desmarcar, ele volta para pendente
        if st.checkbox(f"~~{item['nome']}~~", value=True, key=f"c_{item['nome']}"):
            item["finalizado"] = False
            st.rerun()
# 4. BOTÃO PARA LIMPAR TUDO (OPCIONAL)
if st.sidebar.button("Limpar Lista"):
    st.session_state.carrinho = []
    st.rerun()
