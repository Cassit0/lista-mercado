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

# Garantir que as colunas existam
col_esq, col_dir = st.columns(2)

# Filtrar as listas antes de exibir para evitar erros de índice
pendentes = [item for item in st.session_state.carrinho if not item.get("finalizado")]
no_carrinho = [item for item in st.session_state.carrinho if item.get("finalizado")]

with col_esq:
    st.subheader("⏳ Pendentes")
    for item in pendentes:
        # Usamos o nome do item como chave para ser único
        if st.checkbox(f"{item['nome']} ({item['qtd']}x)", key=f"check_{item['nome']}"):
            # Localizar o item na lista original e marcar como finalizado
            for i, original in enumerate(st.session_state.carrinho):
                if original['nome'] == item['nome']:
                    st.session_state.carrinho[i]["finalizado"] = True
            st.rerun()

with col_dir:
    st.subheader("✅ No Carrinho")
    for item in no_carrinho:
        # Se clicar aqui, ele volta para a lista de pendentes
        if st.checkbox(f"~~{item['nome']}~~", value=True, key=f"uncheck_{item['nome']}"):
            for i, original in enumerate(st.session_state.carrinho):
                if original['nome'] == item['nome']:
                    st.session_state.carrinho[i]["finalizado"] = False
            st.rerun()
# 4. BOTÃO PARA LIMPAR TUDO (OPCIONAL)
if st.sidebar.button("Limpar Lista"):
    st.session_state.carrinho = []
    st.rerun()
