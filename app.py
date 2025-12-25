import streamlit as st

# 1. Configurações Iniciais e Session State
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

st.title("🛒 Minha Lista de Compras")

# 2. Área de Entrada (Onde você adiciona itens)
with st.form("add_item"):
    nome = st.text_input("Produto:")
    qtd = st.number_input("Quantidade:", min_value=1, value=1)
    if st.form_submit_button("Adicionar"):
        st.session_state.carrinho.append({"nome": nome, "qtd": qtd, "finalizado": False})
        st.rerun()

# --- COLOQUE O TRECHO AQUI (Início da Exibição) ---

st.subheader("📌 Itens Pendentes")
for i, item in enumerate(st.session_state.carrinho):
    if not item["finalizado"]:
        # Se marcar o checkbox, o item muda para finalizado=True e a página recarrega
        if st.checkbox(f"{item['nome']} ({item['qtd']}x)", key=f"p_{i}"):
            st.session_state.carrinho[i]["finalizado"] = True
            st.rerun()

st.divider()

st.subheader("✅ Já no Carrinho")
for i, item in enumerate(st.session_state.carrinho):
    if item["finalizado"]:
        st.write(f"~~{item['nome']} ({item['qtd']}x)~~")

# --- FIM DO TRECHO ---

# 3. Resumo Financeiro (Opcional)
# Aqui entraria aquele código do total a pagar que estávamos mexendo.

# --- PARTE 3: O TOTAL DO QUE JÁ ESTÁ NO CARRINHO ---
st.metric("Total no Carrinho", f"R$ {total_confirmado:.2f}")

if st.button("Limpar Lista"):
    st.session_state.carrinho = []
    st.rerun()
