import streamlit as st 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título do aplicativo
st.title("Analisador de Dados Simples")

# Widget para upload de arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Ler o arquivo CSV para um DataFrame
    try:
        df = pd.read_csv(uploaded_file)

        # Mostrar o DataFrame
        st.write("Dados:")
        st.dataframe(df)  # Ou st.table(df) para uma tabela estática

        # Widget para escolher colunas para o gráfico
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()  # Colunas numéricas
        if numeric_cols:  # Verifica se há colunas numéricas
            x_col = st.selectbox("Selecione a coluna para o eixo X", numeric_cols)
            y_col = st.selectbox("Selecione a coluna para o eixo Y", numeric_cols)

            if x_col and y_col:  # Verifica se ambas as colunas foram selecionadas
                # Criar o gráfico de dispersão
                plt.figure(figsize=(8, 6))  # Ajusta o tamanho do gráfico
                plt.scatter(df[x_col], df[y_col])
                plt.xlabel(x_col)
                plt.ylabel(y_col)
                plt.title(f"Gráfico de Dispersão: {x_col} vs {y_col}")
                st.pyplot(plt)  # Mostrar o gráfico no Streamlit

        else:
            st.warning("O arquivo CSV não contém colunas numéricas para gerar o gráfico.")

        # Outras análises ou widgets podem ser adicionados aqui...
        if not numeric_cols:
             st.warning("Não há colunas numéricas no arquivo CSV.")
        else:
            # Estatísticas descritivas
            st.subheader("Estatísticas Descritivas")
            st.write(df.describe())

            # Histogramas
            st.subheader("Histogramas")
            for col in numeric_cols:
                plt.figure(figsize=(8, 6))
                plt.hist(df[col], bins=20)  # Ajuste o número de bins conforme necessário
                plt.title(f"Histograma de {col}")
                st.pyplot(plt)

    except Exception as e:
        st.error(f"Ocorreu um erro ao processar o arquivo: {e}")

else:
    st.info("Por favor, escolha um arquivo CSV para começar.")

