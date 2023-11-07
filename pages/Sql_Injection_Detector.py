import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
import datetime

# ANSI escape sequences for color formatting
GREEN = '<span style="color: green;">'
END_COLOR = '</span>'

def detect_sql_injection(url, payload):
    test_url = f"{url}{payload}"
    response = requests.get(test_url)
    content = response.text
    sql_injection_patterns = [
        r"SQL syntax.*?MySQL",
        r"Warning.*?\Wmysqli?_",
        r"MySQLSyntaxErrorException",
        r"valid MySQL result",
        r"check the manual that (corresponds to|fits) your MySQL server version",
        r"SQL syntax",
    ]
    potential_sql_injection = False
    for pattern in sql_injection_patterns:
        if re.search(pattern, content, re.I):
            potential_sql_injection = True
            break
    return test_url, potential_sql_injection

def main():
    st.markdown('<img style="float: left; width: 15%;" src="https://i.ibb.co/6PQVYD9/logo.png" /><h1 style="float: left;">SQL Injection Detector</h1>', unsafe_allow_html=True)

    st.header("Input Target URLs:")
    target_urls = st.text_area("Enter the target URLs (one URL per line):")

    if st.button("Detect SQL Injection"):
        if not target_urls:
            st.warning("Please enter target URLs.")
            return

        base_urls = target_urls.split('\n')

        payloads = [
            "'123",
            "''123",
            "`123",
            '")123',
            '"))123',
            '`)123',
            '``))123',
            "'))123",
            "')123\"123",
            "[]123",
            '""123',
            "'\"123",
            '"\'123',
            "\\123",
        ]

        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        result_file = f"result_sqli_{current_date}.txt"

        with st.spinner("Scanning for SQL Injection..."):
            result_output = []
            for base_url in base_urls:
                for payload in payloads:
                    url, is_vulnerable = detect_sql_injection(base_url, payload)
                    if is_vulnerable:
                        result_output.append(url)

            if not result_output:
                st.info("No SQL Injection vulnerabilities detected.")
            else:
                st.success(f"Detected {len(result_output)} SQL Injection vulnerabilities:")
                result_text = "\n".join([f"Vuln : {url}" for url in result_output])
                st.text_area("SQL Injection Results:", result_text, height=400)

                with open(result_file, "w") as output_file:
                    for url in result_output:
                        output_file.write(f"Potensi SQL Injection terdeteksi pada URL: {url}\n")

st.sidebar.markdown("Informasi Tambahan")
st.sidebar.info(
    "Ini adalah tools sederhana untuk mendeteksi kerentanan sql injection dari beberapa URL situs web sekaligus. "
    "Pastikan untuk memisahkan URL dengan baris baru."
)

if __name__ == "__main__":
    main()
