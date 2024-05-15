'''
Class for do PadraoController
'''
import streamlit as st
from datetime import datetime
import pandas as pd

# criar lista de Login
login = []

login = [{"Apelido":'Suporte',"Password": '123'},
         {"Apelido":'Visitante',"Password": 'visitante123'},
         {"Apelido":'Maria',"Password": 'Maria@123'}
        ]
apelidos = ['Suporte', 'Visitante', 'Maria']

# Função para verificar as informações
def validacao(info):
    nome, idade, destino, pagamento, data = info
    erros = []

    # Verificar se o nome não contém caracteres numéricos
    if any(char.isdigit() for char in nome):
        erros.append("Nome inválido, pois contém caracteres numéricos")

    # Verificar se a idade é um número
    try:
        idade = int(idade)
    except ValueError:
        erros.append("Idade inválida, não é um número")

    # Verificar se o destino é composto por apenas uma palavra
    if ' ' in destino:
        erros.append("Destino inválido, não é uma palavra única")

    # Verificar se o pagamento foi confirmado é um valor booleano
    if not isinstance(pagamento, bool):
        erros.append("Pagamento inválido, a informação não é do tipo bool")

    # Verificar se a data da viagem é válida e não é uma data passada
    try:
        data = datetime.strptime(data, "%d/%m/%Y")
        if data < datetime.now():
            erros.append("Data da viagem menor que a data atual.")
    except ValueError:
        erros.append("Data da viagem inválida")

    if erros:
        return ", ".join(erros)
    else:
        return "Viagem processada! Aguarde para impressão do ticket"

# Função para estilizar o DataFrame
def style_df(df):
    styled_df = df.style.apply(style_invalid_info, subset=['Validação'])
    styled_df = styled_df.apply(style_invalid_date, subset=['Data da Viagem'])
    styled_df = styled_df.apply(style_invalid_name, subset=['Nome'])
    styled_df = styled_df.apply(style_invalid_idade, subset=['Idade'])
    styled_df = styled_df.apply(style_invalid_destino, subset=['Destino'])
    styled_df = styled_df.apply(style_invalid_pagamento, subset=['Pagamento'])
    return styled_df

# Função para estilizar informações inválidas
def style_invalid_info(s):
    color = 'red' if 'informações inválidas' in s else 'black'
    return [f'color: {color}']*len(s)

# Função para estilizar datas inválidas
def style_invalid_date(series):
    styled = []
    for date in series:
        try:
            datetime.strptime(date, "%d/%m/%Y")
            if datetime.strptime(date, "%d/%m/%Y") < datetime.now():
                styled.append('color: red')
            else:
                styled.append('color: black')
        except ValueError:
            styled.append('color: red')
    return styled

# Função para estilizar nomes inválidos
def style_invalid_name(series):
    styled = []
    for nome in series:
        if any(char.isdigit() for char in nome):
            styled.append('color: red')
        else:
            styled.append('color: black')
    return styled

# Função para estilizar idade inválida
def style_invalid_idade(series):
    styled = []
    for idade in series:
        try:
            # Verificar se é possível converter o valor para inteiro
            int(idade)
            styled.append('color: black')
        except ValueError:
            styled.append('color: red')
    return styled

# Função para estilizar destino inválido
def style_invalid_destino(series):
    styled = []
    for destino in series:
        if ' ' in destino:
            styled.append('color: red')
        else:
            styled.append('color: black')
    return styled

# Função para estilizar pagamento inválido
def style_invalid_pagamento(series):
    styled = []
    for pagamento in series:
        if not isinstance(pagamento, bool):
            styled.append('color: red')
        else:
            styled.append('color: black')
    return styled

# Função para criar e estilizar o DataFrame
def create_style_df(informacoes):
    # Criar um DataFrame com as informações
    df = pd.DataFrame(informacoes, columns=["Nome", "Idade", "Destino", "Pagamento", "Data da Viagem"])
    # Aplicar a função verificar_informacoes a cada linha do DataFrame
    df['Validação'] = df.apply(validacao, axis=1)
    # Estilizar o DataFrame
    styled_df = style_df(df)
    return styled_df

# Lista de informações
informacoes = [
    ("Lucas", "28", "Chile", True, "30/03/2024"),
    ("1223", "10", "Brasil", False, "20/04/2026"),
    ("Amanda", "24n", "França", True, "22/09/2025"),
    ("Vitória", "33", "Marrocos", "True", "25/12/2024"),
    ("Romero", "63", "Argentina", False, "17/03/2022"),
    ("matheus", "21", "Londres", True, "12/06/2024"),
    ("JuLia", "31", "São Mateus", True, "23/04/2024"),
    ("Venâncio", "50", "China", True, "22?05/2024"),
    ("Maria", 23, "India", False, "07/12/2024"),
    ("Pedro", "42", "Br4sil", True, "05/05/2024"),
    ("Tom", 33, "Servolo", False, "02/05/1998")
]