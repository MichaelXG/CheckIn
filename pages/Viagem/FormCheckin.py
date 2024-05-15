import streamlit as st
from Controllers.PadraoController import *
import streamlit_antd_components as sac
import Utils as ut
    
def Form_Checkin():  

    ut.Divisor('Valídar Check In - Viagem', 'clipboard2-data', 'rgb(20,80,90)', 'ListarTarefa01')

    with st.container(border=True):
        # Obter o DataFrame estilizado
        styled_df = create_style_df(informacoes)
        
        # Exibir o DataFrame estilizado como HTML
        st.write(styled_df.to_html(), unsafe_allow_html=True)
       
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'ListarTarefa02')