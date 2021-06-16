import streamlit as st
import requests
import hashlib
from PIL import Image
import sys


title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 5])
#image = Image.open('assets/logo.jpg')
with title_container:
    #with col1:
    #    st.image(image)
    with col2:
        st.title('Password Checker App')
        st.markdown("""
Check if your passwords have ever been Hacked.

-by Mayur Machhi
""")

