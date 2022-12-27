import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'use_container_width' not in st.session_state:
    st.session_state['use_container_width'] = False


st.set_page_config(page_title='Dashboard Unemployment Rate & Crime Rate di USA')
st.subheader('Dashboard Unemployment Rate & Crime Rate di USA')
# data
dataset_file = 'data/Hasil .csv'
Sheet_name = 'Hasil'

df = pd.read_csv(dataset_file)
state = df["State"]
#df = pd.read_csv(dataset_file, sheet_name=Sheet_name,
#                   usecols='A:G', header=0)
#provinsi = df[df["Wilayah"] != 'USA']
#indo = df[df["Wilayah"] == 'USA']
#df.drop(columns='State', axis=1, inplace=True)
st.image(Image.open(
    'asset/map.png'))
st.text('')
st.text('')
st.text('')
#st.subheader('Jumlah Penduduk Miskin di Indonesia per Tahun')
#bar_chart = px.bar(indo,
#                   x='Tahun', y='Jumlah Penduduk Miskin (Ribu Jiwa)')
#st.plotly_chart(bar_chart)

st.subheader('Table Data Total Unemployment Rate & Crime Rate di USA')
st.dataframe(df, 1500, 600)


st.subheader('Unemployment Rate & Crime Rate di USA')
persentase_cr = px.line(df, title="Crime Rate di USA",
                        x='Year', y='Crime Rate', line_group='State', color='State')
persentase_ur = px.line(df, title="Unemployment Rate di USA",
                        x='Year', y='Unemployment Rate', line_group='State', color='State')

b1, b2 = st.columns(2)
b1.plotly_chart(persentase_ur)
b2.plotly_chart(persentase_cr)

st.subheader('Unemployment Rate & Crime Rate di USA (Map Chart Image)')
st.image(Image.open(
    'asset/map.png'))
st.subheader('Unemployment Rate & Crime Rate di USA (Map Chart Image)')
st.image(Image.open(
    'asset/map2.png'))

b3, b4 = st.columns(2)
st.text('Machine Learning dan Github Repository dapat dikunjungi pada link dibawah:')

linkgit = '[Github](https://github.com/FakhriFaishalRochdiana/SDG-16---Crime-Rate)'
linkml = '[Machine Learning](https://github.com/FakhriFaishalRochdiana/SDG-16---Crime-Rate/blob/main/Kelompok_4_Visualisasi_Data.ipynb)'
st.markdown(linkgit, unsafe_allow_html=True)
st.markdown(linkml, unsafe_allow_html=True)

#st.map(df)

#persentase_pend_miskin = px.line(provinsi, title='Persentase Penduduk Miskin di Indonesia Berdasarkan Provinsi',
#                                 x='Tahun', y='Persentase Masyarakat Miskin', line_group='Wilayah', color='Wilayah',)
#Jumlah_pend_miskin = px.line(provinsi, title='Jumlah Penduduk Miskin di Indonesia Berdasarkan Provinsi',
#                             x='Tahun', y='Jumlah Penduduk Miskin (Ribu Jiwa)', line_group='Wilayah', color='Wilayah',)
#b1, b2 = st.columns(2)
#b1.plotly_chart(persentase_pend_miskin)
#b2.plotly_chart(Jumlah_pend_miskin)
#rasio_gini = px.line(provinsi, title='Rasio Gini di Indonesia Berdasarkan Provinsi',
#                     x='Tahun', y='Gini Rasio', line_group='Wilayah', color='Wilayah',)
#st.plotly_chart(rasio_gini)
#
#c1, c2 = st.columns(2)
#makan = px.line(provinsi, title='Jumlah Penduduk Miskin di Indonesia Berdasarkan Provinsi',
#                x='Tahun', y='Garis Kemiskinan Makanan (Rupiah/Kapita/Bulan)', line_group='Wilayah', color='Wilayah',)
#non_makan = px.line(provinsi, title='Jumlah Penduduk Miskin di Indonesia Berdasarkan Provinsi',
#                    x='Tahun', y='Garis Kemiskinan Non Makanan (Rupiah/Kapita/Bulan)', line_group='Wilayah', color='Wilayah',)
#c1.plotly_chart(makan)
#c2.plotly_chart(non_makan)
#
#st.text('Selengkapnya dapat mengunjungi link berikut:')
#linkgit = '[Github](https://github.com/ReyhanAfrizal/No-Poverty-Indonesia-Kelompok-2)'
#linkml = '[Machine Learning](https://github.com/ReyhanAfrizal/No-Poverty-Indonesia-Kelompok-2/blob/master/Tubes_Visdas_2.ipynb)'
#st.markdown(linkgit, unsafe_allow_html=True)
#st.markdown(linkml, unsafe_allow_html=True)
