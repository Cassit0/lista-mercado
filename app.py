import streamlit as st

# 1. Configuração e Inicialização
st.set_page_config(page_title="Lista de Compras", page_icon="🛒")

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

# FUNÇÕES DE AÇÃO (O segredo para funcionar)
def marcar_como_finalizado(index):
    st.session_state.carrinho[index]["finalizado"] = True

def desmarcar_item(index):
    st.session_state.carrinho[index]["finalizado"] = False

def limpar_lista():
    st.session_state.carrinho = []

st.title("🛒 Minha Lista de Compras")

# 2. Formulário de Entrada
with st.form("novo_item", clear_on_submit=True):
    c1, c2 = st.columns([3, 1])
    nome = c1.text_input("O que comprar?")
    qtd = c2.number_input("Qtd:", min_value=1, value=1)
    if st.form_submit_button("Adicionar"):
        if nome:
            st.session_state.carrinho.append({"nome": nome, "qtd": qtd, "finalizado": False})
            st.rerun()

st.divider()

# 3. Exibição em Duas Colunas Reais
col_pendente, col_carrinho = st.columns(2)

with col_pendente:
    st.subheader("⏳ Pendentes")
    # Percorremos a lista original
    for i, item in enumerate(st.session_state.carrinho):
        if not item["finalizado"]:
            # Usamos on_change para garantir que ele mude ANTES de desenhar a tela
            st.checkbox(
                f"{item['nome']} ({item['qtd']}x)", 
                key=f"p_{i}_{item['nome']}", 
                on_change=marcar_como_finalizado, 
                args=(i,)
            )

with col_carrinho:
    st.subheader("✅ No Carrinho")
    for i, item in enumerate(st.session_state.carrinho):
        if item["finalizado"]:
            st.checkbox(
                f"~~{item['nome']}~~", 
                value=True, 
                key=f"c_{i}_{item['nome']}", 
                on_change=desmarcar_item, 
                args=(i,)
            )

st.divider()

# 4. Botão de Limpar (Fora das colunas)
if st.button("🗑️ Limpar Lista Completa", use_container_width=True, on_click=limpar_lista):
    st.rerun()
