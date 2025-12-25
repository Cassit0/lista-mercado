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

st.divider()

# Criamos duas colunas reais para o visual ficar organizado
col1, col2 = st.columns(2)

with col1:
    st.subheader("⏳ Pendentes")
    # Percorre a lista e só mostra o que finalizado == False
    for i, item in enumerate(st.session_state.carrinho):
        if not item.get("finalizado", False): 
            # O segredo: a chave (key) precisa ser única para o Streamlit não se perder
            if st.checkbox(f"{item['nome']} ({item['qtd']}x)", key=f"pendente_{i}_{item['nome']}"):
                st.session_state.carrinho[i]["finalizado"] = True
                st.rerun()

with col2:
    st.subheader("✅ No Carrinho")
    # Percorre a lista novamente e só mostra o que finalizado == True
    for i, item in enumerate(st.session_state.carrinho):
        if item.get("finalizado", False):
            # Usamos outro checkbox ou apenas um texto riscado
            # Se quiser poder "desmarcar" para ele voltar para a lista de cima:
            if st.checkbox(f"~~{item['nome']}~~", value=True, key=f"pago_{i}_{item['nome']}"):
                st.session_state.carrinho[i]["finalizado"] = False
                st.rerun()
# 4. BOTÃO PARA LIMPAR TUDO (OPCIONAL)
if st.sidebar.button("Limpar Lista"):
    st.session_state.carrinho = []
    st.rerun()
