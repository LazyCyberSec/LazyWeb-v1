import streamlit as st
import webbrowser

# Set page title and favicon
st.set_page_config(
    page_title="Lazy Cyber Security Community",
    page_icon="🔒",
)



# Title and Logo
st.title("Lazy Cyber Security Community")
st.image("https://raw.githubusercontent.com/LazyCyberSec/LazyFinder/main/logo.png", width=200)
st.markdown("Welcome to the Lazy Cyber Security community!")
st.write("")

# Sidebar navigation
st.header("About Us")
st.write("Lazy Cyber Security is a community dedicated to cybersecurity enthusiasts who want to learn and share their knowledge in a relaxed and collaborative environment.")
st.write("Join us to explore the world of cybersecurity, discuss the latest trends, and participate in educational activities.")
st.markdown("### Join our community today!")
if st.button("Join Now"):
    webbrowser.open_new_tab('https://discord.gg/uDhvBHDG')


# Define page content

st.sidebar.markdown("Informasi Tambahan")
st.sidebar.info(
    "Ini adalah web tools lazy cyber security untuk membantu kalian dalam bug hunting/pentest. "
)

with st.sidebar:
    st.info('Youtube : Lazy Cyber Security')



# Add some style to the main content
st.markdown(
    """
    <style>
    body {
        background-color: #f3f3f3;
        color: #333;
    }
    .sidebar .sidebar-content {
        background-color: #333;
        color: #f3f3f3;
    }
    .sidebar .radio-box .label, .sidebar .radio-box .label:hover {
        color: #333;
    }
    .stButton > button {
        background-color: #333;
        color: #f3f3f3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

