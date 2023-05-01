import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid
import pandas as pd
from PIL import Image
import time
@st.cache_data
def data ():
    parameters = ['NOM', 'WILAYA','COMMUNE','NUMERO','PRODUIT','QUANTITE','TOTAL']
    dfk= pd.DataFrame(columns=parameters)
    df1=dfk
    dfk.to_excel('data.xlsx')
    
    st.cache_data.clear()
img=Image.open("a.jpg")
st.set_page_config(page_title='Saisie Rapide', page_icon=img, layout='centered', initial_sidebar_state='auto')
col1, col2, col3 = st.columns(3)

with col1:
   st.header("")
   

with col2:
   st.header("")
   #original_title = '<h2 style="font-family:Courier; color:red; font-size: 15px center;">Ajouter Clients</h2>'
   #st.markdown(original_title, unsafe_allow_html=True)
   st.image("a.jpg")
with col3:
   st.header("")
co1, co2, co3 = st.columns(3)
with co1:
   st.header("")
   

with co2:
   st.header("")
   #original_title = '<h2 style="font-family:Courier; color:red; font-size: 15px center;">Ajouter Clients</h2>'
   #st.markdown(original_title, unsafe_allow_html=True)
   
with co3:
   st.header("")
   with st.spinner('Wait for it...'):
    

    if st.button("Remettre a Zero"):
        st.balloons()
        time.sleep(2)
        data ()
        
        
        
        st.experimental_rerun()
        
        
a=[]
with st.form("form",clear_on_submit = True):
    cmd=st.text_area("")
    #if cmd:
       # st.write(cmd)
    submit_button = st.form_submit_button("Ajouter Commande")
a=cmd.split("\n")
extra_submit_button = st.button("Afficher commandes")
if extra_submit_button:
    df2 = pd.read_excel('data.xlsx')
    if len(df2)>0:
            
            df3=df2[['NOM', 'WILAYA','COMMUNE','NUMERO','PRODUIT','QUANTITE','TOTAL']].copy()
        
            AgGrid(df3, columns_auto_size_mode=1,editable=True)
        
    else:
        st.info('List commandes vide', icon="ℹ️")
    #submit_button = True

if submit_button:
    if (len(a)<7):
        st.warning('Data non valide verifiez vous informations .')
        st.stop()
    if (len(a)>7):
        st.warning('Data non valide verifiez vous informations .')
        st.stop()
    new=['NOM', 'WILAYA','COMMUNE','NUMERO','PRODUIT','QUANTITE','TOTAL']
    new_row = pd.DataFrame(a, index=new).T
    df2 = pd.read_excel('data.xlsx')
    df2 = pd.concat((df2, new_row),ignore_index=True)
    df2.to_excel('data.xlsx')
    
    
    st.success('commande ajouter avec succes', icon="✅")
    st.write(a)
    
