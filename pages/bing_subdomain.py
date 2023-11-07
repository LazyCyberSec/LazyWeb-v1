import streamlit as st
import requests
from bs4 import BeautifulSoup

# No Max Execution Time
# You don't need to set time limit in Python

# Curl Function
def curlreq(domain):
    try:
        response = requests.get(domain)
        return response.text
    except Exception as e:
        return ""

# URL Cleaning
def cleanme(url):
    if url.startswith("http://") or url.startswith("https://"):
        url = url.split("//")[1]
    if url.startswith("www."):
        url = url[4:]
    return url.split("/")[0]

# Enter Domain Name
st.markdown('<img style="float: left; width: 15%;" src="https://i.ibb.co/6PQVYD9/logo.png" /><h1 style="float: left;">Bing Subdomain Scanner</h1>', unsafe_allow_html=True)
web = st.text_input("Enter Domain Name (e.g., yahoo.com)")
if st.button("Scan Subdomains"):
    i = 1
    subdomains = []
    while True:
        website = curlreq(f"http://www.bing.com/search?q=domain%3a{web}&first={i}")
        soup = BeautifulSoup(website, 'html.parser')
        links = soup.find_all('cite')
        for link in links:
            subdomain = link.get_text()
            subdomains.append(subdomain)

        if i == 1:
            i = 11
        else:
            i = i + 12

        if "Next" not in website:
            break

    # Get unique results
    subdomains = list(set(subdomains))
    subdomains.sort()

    # Display results
    st.text_area("Subdomains:", "\n".join(map(cleanme, subdomains)))
    st.write(f"Number of Subdomains: {len(subdomains)}")

st.sidebar.markdown("Informasi Tambahan")
st.sidebar.info(
    "Ini adalah tools sederhana untuk mendeteksi subdomain pada website menggunakan search engine bing. "
)