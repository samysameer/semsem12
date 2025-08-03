import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


 
df = pd.read_csv('D:\Sleep\sleep.csv')
print(df.head())

df['Sleep Disorder'] = df['Sleep Disorder'].replace(np.nan, 'Normal')

st.sidebar.header("sleep dashboard")
st.sidebar.image("D:\Sleep\website.jpg")
st.sidebar.write("Samy sameer")

cat_filter = st.sidebar.selectbox('Filters',['Gender','Occupation','BMI Category',None,'Sleep Disorder'])

a1,a2,a3,a4 = st.columns(4)
a1.metric ("Avd age",round(df['Age'].mean(),2))
a2.metric ("Count of ID",round(df['Person ID'].count(),0))
a3.metric("Max daily steps",round(df['Daily Steps'].max(),0))
a4.metric("Avg sleep duration",round(df['Sleep Duration'].mean(),0))

st.subheader('Sleep quality vs stress level' ,)

fig = px.scatter(data_frame=df,x='Stress Level',y='Quality of Sleep',color=cat_filter,size='Quality of Sleep')
st.plotly_chart(fig,use_container_width=True)


c1, c2 = st.columns([4,3])
with c1:
    st.text('Occupation VS Avg Sleep Duration (Sorted)')

    avg_sleep_by_occ = df.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending=False).reset_index()
    fig1 = px.bar(data_frame=avg_sleep_by_occ, x='Occupation', y='Sleep Duration')
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.text('Gender VS Quality of Sleep')
    gender_sleep = df.groupby('Gender')['Quality of Sleep'].mean().reset_index()
    fig2 = px.pie(gender_sleep, names='Gender', values='Quality of Sleep')
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Pair Plot & Heatmap for Numerical Features")
