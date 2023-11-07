import streamlit as st
import requests

st.set_page_config(page_title='Admin Finder', layout='centered')

st.markdown('<img style="float: left; width: 15%;" src="https://i.ibb.co/6PQVYD9/logo.png" /><h1 style="float: left;">AdminFinder</h1>', unsafe_allow_html=True)

st.write('pastikan belakang site tidak ada / [http://example.com]')
url = st.text_input('Enter URL')
if st.button('RUN'):
    st.subheader('Scanning Results:')
    urls = url + ':80'
    adminfile = './txt/adminfile.txt'
    with open(adminfile, 'r') as file:
        adminfile = file.read().strip().split('\n')
        results = []
        for admin_url in adminfile:
            site = url + admin_url  # Concatenate url with admin_url
            response = requests.get(site)
            if response.status_code == 200:
                results.append(f"**Vulnerable:** {site}")
            else:
                results.append(f"Not Vulnerable: {site}")
        st.write("\n".join(results))

st.sidebar.markdown("Informasi Tambahan")
st.sidebar.info(
    "Ini adalah tools sederhana untuk mendeteksi path admin login pada website. "
)