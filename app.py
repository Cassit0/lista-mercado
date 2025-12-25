import streamlit as st

# 1. Configuração e Inicialização
st.set_page_config(page_title="Lista de Compras", page_icon="🛒")

# Inicializa o carrinho se ele não existir
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

st.title("🛒 Minha Lista de Compras")

# 2. Formulário para Adicionar Itens
with st.form("novo_item", clear_on_submit=True):
    col_nome, col_qtd = st.columns([3, 1])
    nome = col_nome.text_input("O que precisa comprar?")
    qtd = col_qtd.number_input("Qtd", min_value=1, value=1)
    if st.form_submit_button("Adicionar à Lista") and nome:
        # Adiciona como um novo dicionário
        st.session_state.carrinho.append({
            "id": f"{nome}_{len(st.session_state.carrinho)}", # ID Único
            "nome": nome, 
            "qtd": qtd, 
            "finalizado": False
        })
        st.rerun()

st.divider()

# 3. Exibição das Listas
col_pendente, col_carrinho = st.columns(2)

with col_pendente:
    st.subheader("⏳ Pendentes")
    # Filtramos e mostramos o que não está pronto
    for i, item in enumerate(st.session_state.carrinho):
        if not item["finalizado"]:
            # Usamos o ID único do item na KEY
            if st.checkbox(f"{item['nome']} ({item['qtd']}x)", key=f"p_{item['id']}"):
                st.session_state.carrinho[i]["finalizado"] = True
                st.rerun()

with col_carrinho:
    st.subheader("✅ No Carrinho")
    # Filtramos e mostramos o que já foi marcado
    for i, item in enumerate(st.session_state.carrinho):
        if item["finalizado"]:
            # Checkbox já marcado. Se desmarcar, volta para pendente
            if st.checkbox(f"~~{item['nome']}~~", value=True, key=f"c_{item['id']}"):
                st.session_state.carrinho[i]["finalizado"] = False
                st.rerun()

# 4. Botão de Limpar Lista (Barra Lateral)
if st.sidebar.button("🗑️ Limpar Lista Toda"):
    st.session_state.carrinho = []
    st.rerun()

st.sidebar.info("Dica: Marque o item para movê-lo para o carrinho.")
