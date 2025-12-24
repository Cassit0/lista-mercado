import streamlit as st

st.set_page_config(page_title="Meu Mercado", page_icon="🛒")

st.title("🛒 Lista de Compras")

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

# --- FORMULÁRIO QUE LIMPA SOZINHO ---
with st.form("meu_formulario", clear_on_submit=True):
    nome = st.text_input("O que vai comprar?")
    col1, col2 = st.columns(2)
    with col1:
        qtd = st.number_input("Qtd", min_value=1, step=1, value=1)
    with col2:
        preco = st.number_input("Preço R$", min_value=0.0, step=0.10, value=0.0)
    
    # O botão de enviar o formulário
    submit = st.form_submit_button("➕ Adicionar Item", use_container_width=True)

# Lógica fora do formulário para processar o item
if submit:
    if nome and preco >= 0:
        st.session_state.carrinho.append({
            "nome": nome, 
            "qtd": qtd, 
            "preco": preco, 
            "subtotal": qtd * preco
        })
        st.rerun() # Recarrega para mostrar o item na lista abaixo

st.divider()

# --- EXIBIÇÃO ---
total_geral = 0
for i, item in enumerate(st.session_state.carrinho):
    c1, c2 = st.columns([4, 1])
    c1.write(f"**{item['nome']}** - {item['qtd']}x R${item['preco']:.2f}")
    if c2.button("🗑️", key=f"del_{i}"):
        st.session_state.carrinho.pop(i)
        st.rerun()
    total_geral += item['subtotal']

st.divider()
st.metric("Total no Carrinho", f"R$ {total_geral:.2f}")
