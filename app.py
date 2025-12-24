import streamlit as st

# Configuração da página para parecer um app de celular
st.set_page_config(page_title="Meu Mercado", page_icon="🛒", layout="centered")

st.title("🛒 Lista de Compras")

# Garantir que a lista sobreviva a atualizações de página
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

# Campos de entrada simplificados para mobile
with st.container():
    nome = st.text_input("O que vai comprar?")
    col1, col2 = st.columns(2)
    with col1:
        qtd = st.number_input("Qtd", min_value=1, step=1, value=1)
    with col2:
        preco = st.number_input("Preço R$", min_value=0.0, step=0.10, value=0.0)
    
    if st.button("➕ Adicionar Item", use_container_width=True):
        if nome and preco >= 0:
            st.session_state.carrinho.append({
                "nome": nome, 
                "qtd": qtd, 
                "preco": preco, 
                "subtotal": qtd * preco
            })
            st.rerun()

st.divider()

# Exibição dos itens
total_geral = 0
for i, item in enumerate(st.session_state.carrinho):
    col_texto, col_botao = st.columns([4, 1])
    with col_texto:
        st.write(f"**{item['nome']}**")
        st.caption(f"{item['qtd']}x R${item['preco']:.2f} = R${item['subtotal']:.2f}")
    with col_botao:
        # Botão para remover item se errar
        if st.button("🗑️", key=f"del_{i}"):
            st.session_state.carrinho.pop(i)
            st.rerun()
    total_geral += item['subtotal']

st.divider()

# Valor total fixo no rodapé ou em destaque
st.metric("Total no Carrinho", f"R$ {total_geral:.2f}")

if st.button("Limpar Lista Toda"):
    st.session_state.carrinho = []
    st.rerun()
