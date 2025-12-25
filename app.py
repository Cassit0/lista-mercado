import streamlit as st

st.set_page_config(page_title="Checklist de Mercado", page_icon="🛒")

st.title("🛒 Minha Lista Prática")

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

# --- PARTE 1: ANOTAR (O que você faz em casa) ---
with st.expander("➕ Adicionar Itens à Lista", expanded=True):
    with st.form("add_item", clear_on_submit=True):
        nome = st.text_input("Produto")
        col1, col2 = st.columns(2)
        qtd = col1.number_input("Qtd", min_value=1, value=1)
        preco = col2.number_input("Preço Est. (R$)", min_value=0.0, value=0.0, step=0.10)
        if st.form_submit_button("Salvar na Lista"):
            if nome:
                st.session_state.carrinho.append({
                    "nome": nome, 
                    "qtd": qtd, 
                    "preco": preco,
                    "finalizado": False # Novo campo para o "Check"
                })
                st.rerun()

st.divider()

# --- PARTE 2: TICAR (O que você faz no mercado) ---
st.subheader("Sua Lista:")
total_confirmado = 0

if not st.session_state.carrinho:
    st.info("Sua lista está vazia!")
else:
    for i, item in enumerate(st.session_state.carrinho):
        # Cria uma linha com checkbox e informações
        col_check, col_info = st.columns([1, 4])
        
        # O checkbox define se o item foi "finalizado" (colocado no carrinho)
        item_checado = col_check.checkbox("", value=item["finalizado"], key=f"check_{i}")
        st.session_state.carrinho[i]["finalizado"] = item_checado
        
        if item_checado:
            # Se tiver riscado, mostra com um estilo diferente (opcional) e soma no total
            col_info.write(f"~~{item['nome']} ({item['qtd']}x)~~")
            total_confirmado += (item['qtd'] * item['preco'])
        else:
            col_info.write(f"**{item['nome']}** ({item['qtd']}x) - R$ {item['preco']:.2f}")

st.divider()

# --- PARTE 3: O TOTAL DO QUE JÁ ESTÁ NO CARRINHO ---
st.metric("Total no Carrinho", f"R$ {total_confirmado:.2f}")

if st.button("Limpar Lista"):
    st.session_state.carrinho = []
    st.rerun()
