import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_preconnect_css(url):
    st.markdown(f'<link rel="preconnect" href="{url}">', unsafe_allow_html=True)
    
def remote_preconnect_crossorigin_css(url):
    st.markdown(f'<link rel="preconnect" href="{url}" crossorigin>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)
    
plot_color_list = [
    "rgba(91, 22, 106, 1)",
    "rgba(124, 213, 77, 1)",
    "rgba(59, 12, 71, 1)",
    "rgba(138, 12, 184, 1)",
    "rgba(18, 139, 177, 1)",
    "rgba(35, 206, 217, 1)",
    "rgba(35, 128, 15, 1)",
    "rgba(143, 56, 22, 1)",
    "rgba(219, 78, 109, 1)",
    "rgba(84, 12, 34, 1)",
]

jms_color_list = ['#8f0fd4', '#0072e8', '#009cdc', '#00c7b1', '#71db5c', '#fcdd14', '#282d32', '#808080', '#b1b1b1', '#d5d5d5']