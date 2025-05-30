import streamlit as st

#----------------------------------------------SIDEBAR
st.sidebar.title('SonicStar')
st.sidebar.write('Veja o clipe de algumas estrelas')

estilos=['Pop','Rock','Hip-Hop','MPB']
estilo=st.sidebar.selectbox('Escolha o estilo',estilos)


if estilo == 'Pop':
    Cantores =['Ariana Grande','Michael Jackson','Bruno Mars','Byoncé']
elif estilo == 'Rock':
    Cantores = ['The Beatles','Queen',"Guns N'Roses"]


Cantor =st.sidebar.selectbox('Faça sua escolha', Cantores)


#----------------------------------------------Principal
st.title("SonicStar")
st.write("Bem vindo ao seu universo musical.")
if Cantor == 'Ariana Grande':
    st.video('https://www.youtube.com/watch?v=QYh6mYIJG2Y')

