import streamlit as st

# 1. Configuração e Inicialização
st.set_page_config(page_title="Lista de Compras", page_icon="🛒")

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

st.title("🛒 Minha Lista de Compras")

# 2. Adicionar Itens
with st.form("form_novo", clear_on_submit=True):
    col1, col2 = st.columns([3, 1])
    nome = col1.text_input("Item:")
    qtd = col2.number_input("Qtd:", min_value=1, value=1)
    if st.form_submit_button("Adicionar"):
        if nome:
            # Cada item ganha um ID único baseado no tempo para não dar erro de chave
            import time
            novo_item = {"id": str(time.time()), "nome": nome, "qtd": qtd, "finalizado": False}
            st.session_state.carrinho.append(novo_item)
            st.rerun()

st.divider()

# 3. EXIBIÇÃO (O segredo está aqui)
col_esq, col_dir = st.columns(2)

# Usamos uma cópia da lista para iterar com segurança
for i, item in enumerate(st.session_state.carrinho):
    if not item["finalizado"]:
        with col_esq:
            # Se marcar aqui, ele muda o status e recarrega
            if st.checkbox(f"{item['nome']} ({item['qtd']}x)", key=item["id"]):
                st.session_state.carrinho[i]["finalizado"] = True
                st.rerun()
    else:
        with col_dir:
            # Se desmarcar aqui, ele volta para a esquerda
            # value=True porque ele JÁ está finalizado
            if st.checkbox(f"~~{item['nome']}~~", value=True, key=item["id"]):
                st.session_state.carrinho[i]["finalizado"] = False
                st.rerun()

st.divider()

# 4. BOTÃO LIMPAR (Agora ele apaga TUDO)
if st.button("🗑️ Limpar Lista Completa", use_container_width=True):
    st.session_state.carrinho = [] # Esvazia a lista inteira, marcados ou não
    st.rerun()
