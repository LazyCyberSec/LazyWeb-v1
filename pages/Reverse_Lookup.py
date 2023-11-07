import streamlit as st
import re
import requests

st.markdown('<img style="float: left; width: 15%;" src="https://i.ibb.co/6PQVYD9/logo.png" /><h1 style="float: left;">Reverse domain/ip Lookup</h1>', unsafe_allow_html=True)


s = requests.Session()
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

def reverse_domain():
    uploaded_file = st.file_uploader("Upload a text file with domain names", type=["txt"])
    if uploaded_file:
        file_contents = uploaded_file.read().decode("utf-8")
        domain_list = file_contents.splitlines()

        reversed_domains = set()
        result_text = ""  # Inisialisasi teks hasil kosong
        for domain in domain_list:
            if domain.startswith("http://"):
                domain = domain.replace("http://", "")
            if domain.startswith("https://"):
                domain = domain.replace("https://", "")
            
            response = s.get(f"https://rapiddns.io/sameip/{domain}?full=1#result", headers=ua)
            if response.status_code == 200:
                content = response.content.decode("utf-8")
                pattern = r"</th>\n<td>(.*?)</td>"
                results = re.findall(pattern, content)
                if results:
                    result_text += f"Site: {domain} - [ {len(results)} ]\n"  # Menambahkan teks hasil ke variabel result_text
                    for result in results:
                        result = result.strip()
                        if result.startswith("www."):
                            result = result[4:]
                        reversed_domains.add(result)

        if reversed_domains:
            st.header("Reversed Domains with Results:")
            result_text = '\n'.join(reversed_domains)
            st.text_area("Domains with Results:", result_text)

            # Add a download button
            st.download_button(
                label="Download Results",
                data=result_text,
                key="download_results.txt",
                help="Click here to download the results as a text file."
            )
        else:
            st.warning("No domains with results were found in the input file.")

st.sidebar.markdown("Informasi Tambahan")
st.sidebar.info(
    "Ini adalah tools sederhana untuk reverse ip lookup beberapa domain situs web sekaligus. "
    "Pastikan untuk memisahkan domain dengan baris baru."
)
reverse_domain()
