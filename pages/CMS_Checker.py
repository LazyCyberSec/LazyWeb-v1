import streamlit as st
import requests

st.title("Fast CMS Checker")

def check_cms(site):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31"
    }
    try:
        response = requests.get(site, headers=headers, timeout=20)
        content = response.text
        detected_cms = None

        if "Joomla" in content:
            detected_cms = "Joomla"
        elif "Vbulletin" in content:
            detected_cms = "Vbulletin"
        elif "WordPress" in content:
            detected_cms = "WordPress"
        elif "Drupal" in content:
            detected_cms = "Drupal"
        elif "Magento" in content:
            detected_cms = "Magento"
        elif "Opencart" in content:
            detected_cms = "Opencart"
        elif "XenForo" in content:
            detected_cms = "XenForo"
        elif "Prestashop" in content:
            detected_cms = "Prestashop"
        elif "Lokomedia" in content:
            detected_cms = "Lokomedia"
        else:
            detected_cms = "Unknown"

        return detected_cms
    except Exception as e:
        return "Error"

# Create a text input widget for manual input
input_sites = st.text_area("Enter site URLs (one per line)")

# Create a button to start the CMS check
if st.button("Start CMS Check"):
    sites = input_sites.split('\n')
    st.write(f"Total sites: {len(sites)}")
    st.write("Checking CMS for each site...")
    cms_results = []

    for site in sites:
        site = site.strip()
        if site:
            result = check_cms(site)
            cms_results.append((site, result))

    result_text = "\n".join([f"{site} [{result}]" if result != "Unknown" else f"{site} [Unknown]" for site, result in cms_results])
    st.text_area("CMS Check Results: ", result_text, height=400)

st.sidebar.markdown("Informasi Tambahan")
st.sidebar.info(
    "Ini adalah tools sederhana untuk mendeteksi CMS yang digunakan dari beberapa URL situs web sekaligus. "
    "Pastikan untuk memisahkan URL dengan baris baru. "
    "#NOTE : Tools ini tidak begitu akurat"
)
