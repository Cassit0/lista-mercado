import streamlit as st

# 1. Configuração e Inicialização Segura
st.set_page_config(page_title="Lista de Compras", page_icon="🛒")

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

st.title("🛒 Minha Lista de Compras")

# 2. Formulário para Adicionar
with st.form("form_novo_item", clear_on_submit=True):
    col1, col2 = st.columns([3, 1])
    nome_item = col1.text_input("Produto:")
    qtd_item = col2.number_input("Qtd:", min_value=1, value=1)
    
    if st.form_submit_button("Adicionar"):
        if nome_item:
            # Criamos um dicionário simples
            novo = {"nome": nome_item, "qtd": qtd_item, "finalizado": False}
            st.session_state.carrinho.append(novo)
            st.rerun()

st.divider()

# 3. Exibição com Colunas
col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("⏳ Pendentes")
    # Usamos o list(enumerate) para evitar erros de índice ao alterar a lista
    for i, item in enumerate(st.session_state.carrinho):
        if not item["finalizado"]:
            # A KEY precisa ser única para cada checkbox
            if st.checkbox(f"{item['nome']} ({item['qtd']}x)", key=f"item_{i}_{item['nome']}"):
                st.session_state.carrinho[i]["finalizado"] = True
                st.rerun()

with col_dir:
    st.subheader("✅ No Carrinho")
    for i, item in enumerate(st.session_state.carrinho):
        if item["finalizado"]:
            # Checkbox marcado para riscar o texto
            if st.checkbox(f"~~{item['nome']}~~", value=True, key=f"pago_{i}_{item['nome']}"):
                st.session_state.carrinho[i]["finalizado"] = False
                st.rerun()

st.divider()

# 4. Botão de Limpar (Abaixo de tudo para fácil acesso)
if st.button("🗑️ Limpar Lista Completa", use_container_width=True):
    st.session_state.carrinho = []
    st.rerun()
