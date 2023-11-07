import streamlit as st
import requests

def main():
    st.title("Dork Generator")


    uploaded_keywords = st.file_uploader("Upload a text file with keywords", type=["txt"])
    uploaded_wd = st.file_uploader("Upload the 'wd.txt' file", type=["txt"])

    if uploaded_keywords is not None and uploaded_wd is not None:
        keywords = uploaded_keywords.read().decode('utf-8').splitlines()  # Decode as UTF-8
        wd_text = uploaded_wd.read().decode('utf-8').splitlines()  # Decode as UTF-8
        results = generate_dorks(keywords, wd_text)


        download_button = st.button("Download Combined Dorks")
        if download_button:
            download_combined_dorks(results)

def generate_dorks(keywords, wd_text):
    results = []
    for keyword in keywords:
        keyword = keyword.strip()
        for wd in wd_text:
            wd = wd.strip()
            result = f"{keyword}\t{wd}"
            results.append(result)
    return results

def download_combined_dorks(results):
    combined_dorks_text = "\n".join(results)
    st.text("Downloading...")
    st.download_button(
        label="Click to download Combined Dorks",
        data=combined_dorks_text,
        key="combined_dorks.txt",
        help="Save the combined dorks as a text file",
    )

st.sidebar.markdown("Informasi Tambahan")
st.sidebar.info(
    "Ini adalah tools sederhana untuk membuat dork secara mudah dengan cara mengcombine file text. "
)


if __name__ == '__main__':
    main()
