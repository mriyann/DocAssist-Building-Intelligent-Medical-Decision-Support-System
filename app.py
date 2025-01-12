import pickle
import streamlit as st

df=pickle.load(open('df.pkl','rb'))
clf=pickle.load(open('rf_clf.pkl','rb'))

label_map= {'Diseased':'Diseased','Healthy':'Healthy'}

st.header("DocAssist")
st.subheader('Building Intelligent Medical Decision Support System')
st.divider()

HAEMATOCRIT=st.slider("Enter the Haematocrit of the person",min_value=10,max_value=80,value=0,step=1)
HAEMOGLOBINS=st.slider("Enter the Haemoglobins of the person",min_value=1,max_value=40,value=0,step=1)
ERYTHROCYTE=st.slider("Enter the Erythrocyte of the person",min_value=1,max_value=40,value=0,step=1)
LEUCOCYTE=st.slider("Enter the Leucocyte of the person",min_value=1,max_value=90,value=0,step=1)
THROMBOCYTE=st.number_input("Enter the Leucocyte of the person", min_value=None, max_value=None)
MCH=st.slider("Enter the MCH of the person",min_value=1,max_value=60,value=0,step=1)
MCHC=st.slider("Enter the MCHC of the person",min_value=1,max_value=60,value=0,step=1)
MCV=st.number_input("Enter the MCV of the person", min_value=None, max_value=None)
AGE=st.number_input("Enter the Age of the person", min_value=None, max_value=None,step=1)

if st.button("PREDICT"):
    op=clf.predict([[HAEMATOCRIT,HAEMOGLOBINS,ERYTHROCYTE,LEUCOCYTE,THROMBOCYTE,MCH,MCHC,MCV,AGE]])
    op_str = op[0]
    st.subheader(f"Considering the symptoms the person is {op_str}")
