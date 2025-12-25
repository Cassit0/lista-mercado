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

# 3. EXIBIÇÃO - O TRECHO QUE VOCÊ COLOCOU
col_pendente, col_carrinho = st.columns(2)

with col_pendente:
    st.subheader("⏳ Pendentes")
    # Usamos uma cópia da lista para evitar erros de índice ao alterar o estado
    for i, item in enumerate(st.session_state.carrinho):
        if not item["finalizado"]:
            # O segredo é a KEY única (p_ + nome + indice)
            if st.checkbox(f"{item['nome']} ({item['qtd']}x)", key=f"p_{i}_{item['nome']}"):
                st.session_state.carrinho[i]["finalizado"] = True
                st.rerun()

with col_carrinho:
    st.subheader("✅ No Carrinho")
    for i, item in enumerate(st.session_state.carrinho):
        if item["finalizado"]:
            # Se quiser desmarcar e voltar para pendente:
            if st.checkbox(f"~~{item['nome']}~~", value=True, key=f"c_{i}_{item['nome']}"):
                # Se ele desmarcar o que já estava feito
                st.session_state.carrinho[i]["finalizado"] = False
                st.rerun()

# 4. BOTÃO PARA LIMPAR TUDO (OPCIONAL)
if st.sidebar.button("Limpar Lista"):
    st.session_state.carrinho = []
    st.rerun()
