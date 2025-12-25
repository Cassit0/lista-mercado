import streamlit as st
import time

# 1. Configuração e Inicialização
st.set_page_config(page_title="Lista de Compras", page_icon="🛒")

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

st.title("🛒 Lista de Compras")

# 2. Formulário para Adicionar
with st.form("add_item", clear_on_submit=True):
    col_n, col_q = st.columns([3, 1])
    nome = col_n.text_input("Produto:")
    qtd = col_q.number_input("Qtd:", min_value=1, value=1)
    if st.form_submit_button("Adicionar"):
        if nome:
            # Geramos um ID único para o item não "se perder" entre as colunas
            id_item = f"{nome}_{time.time()}"
            st.session_state.carrinho.append({"id": id_item, "nome": nome, "qtd": qtd, "finalizado": False})
            st.rerun()

st.divider()

# 3. FILTRAGEM PRÉVIA (O segredo para as colunas não sumirem)
pendentes = [item for item in st.session_state.carrinho if not item["finalizado"]]
concluidos = [item for item in st.session_state.carrinho if item["finalizado"]]

col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("⏳ Pendentes")
    for item in pendentes:
        # Quando clica, procuramos o item na lista original pelo ID e mudamos para True
        if st.checkbox(f"{item['nome']} ({item['qtd']}x)", key=f"p_{item['id']}"):
            for i in st.session_state.carrinho:
                if i['id'] == item['id']:
                    i['finalizado'] = True
            st.rerun()

with col_dir:
    st.subheader("✅ No Carrinho")
    for item in concluidos:
        # Quando desmarca, procuramos o ID e mudamos para False
        if st.checkbox(f"~~{item['nome']}~~", value=True, key=f"c_{item['id']}"):
            for i in st.session_state.carrinho:
                if i['id'] == item['id']:
                    i['finalizado'] = False
            st.rerun()

st.divider()

# 4. BOTÃO LIMPAR (Limpa TUDO com 100% de certeza)
if st.button("🗑️ Limpar Lista Completa", use_container_width=True):
    st.session_state.carrinho = []
    st.rerun()
