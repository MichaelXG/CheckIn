import streamlit as st
import streamlit_antd_components as sac
import pages.Viagem.FormCheckin as fck

from pages.Home.Create_Home import Create_Home    
from pages.Login.Login import login_page    
from Controllers.PadraoController import *  

def Main():
    # Menu
    with st.sidebar:
        st.image('data:image/png;base64,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', width=None, use_column_width='auto') 
        selected_usu = sac.menu([
            sac.MenuItem(f'Bem-vindo, "{st.session_state.Apelido_L}"!', icon=sac.BsIcon(name='person-bounding-box', color='rgb(20,80,90)')),   
            # Usuário Logado
            sac.MenuItem(type='divider'),
            sac.MenuItem('Logout', icon=sac.BsIcon(name='box-arrow-left', color='red')),
            sac.MenuItem(type='divider'),
        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_login')
    
    if selected_usu == 'Logout':
        st.session_state.logged_in = False
        st.rerun()  
          
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Menu Principal', icon=sac.BsIcon(name='person-bounding-box', color='rgb(20,80,90)')),   
            # Check in
            sac.MenuItem(type='divider'),
            sac.MenuItem('Check In',  icon=sac.BsIcon(name='person-fill', color='rgb(20,80,90)'), description='Adicionar novo Aluno'),
        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_principal')
    
    if selected == 'Menu Principal':
        Create_Home()
    elif selected == 'Check In':
        if __name__ == "__main__":
            fck.Form_Checkin()   
          
# Lógica para alternar entre as páginas com base na ação do usuário
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
 
st.set_page_config(
    page_title="Check in - Viagens",
    page_icon=":airplane_departure:",
    layout="wide",
    initial_sidebar_state="expanded"
)   
        
if __name__ == "__main__":
    if st.session_state.logged_in:        
        Main()
    else:
        opcao = st.radio("Escolha uma opção:", ["Login"], horizontal= True)
        if opcao == "Login":
            if __name__ == "__main__":
                login_page()
