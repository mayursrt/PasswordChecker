#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
import requests
import hashlib
from PIL import Image
from check_pass import *
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Title and Logo
title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 5])
image = Image.open('assets/logo.JPG')
with title_container:
    with col1:
       st.image(image)
    with col2:
        st.title('Password Checker App')
        st.markdown("""
Check if your passwords have ever been a part of a Data Breach.

""")
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Body
st.write('')
st.markdown("<font size=3>This webapp uses the <a href='https://haveibeenpwned.com/Passwords'>HaveIBeenPwned</a> API to check if the password is included in the Pwned Password Database.</font>", unsafe_allow_html=True)
st.markdown("<font size=5>Pwned Passwords</font>", unsafe_allow_html=True)
st.markdown("<font size=3>Pwned Passwords are 613,584,246 real world passwords previously exposed in data breaches. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts.", unsafe_allow_html=True)
st.markdown("<font color='089e00' size=3>This Check is performed through the HaveIBeenPwned API and not the website, therefore it is safe from storing your passwords. Also it uses SHA-256 hashing algorithm to encode entered passwords.</font>", unsafe_allow_html=True)
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input
st.subheader('Enter a Password')


with st.form(key='my_form', clear_on_submit=True):
	user_password = st.text_input('', type='password')
	submit_button = st.form_submit_button(label='Check')
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Main Function
def main(password):
	count = api_check(password)
	if count:
		st.markdown(f"<font color=‘ff0000’ size=5>Oh no! Your password has been seen {count} times before.</font>", unsafe_allow_html=True)
		st.markdown(f"<font color=‘ff0000’ size=3>This password has previously appeared in a data breach and should never be used. If you've ever used it anywhere before, change it!</font>", unsafe_allow_html=True)
	else:
		st.markdown(f'<font color=‘089e00’ size=5>Your password is secure</font>', unsafe_allow_html=True)
		st.markdown(f"<font color=‘089e00’ size=3>This password wasn't found in any of the compromised Passwords loaded into Have I Been Pwned Database.</font>", unsafe_allow_html=True)
	return 

if user_password:
	main(user_password)
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Links
st.write('')
st.markdown(f"If you are not sure about trusting us by sending your passwords through the website or over the internet, Check out this <a href='https://github.com/sajinshivdas/PasswordChecker/tree/main/PasswordCheckerScript'>Password Checker Script</a>. This Script will allow you to check your passwords locally on your computer. ", unsafe_allow_html=True)
st.write('')
st.markdown(f"To make sure your accounts are safe by generating strong passwords, visit <a href='https://generate-password-webapp.herokuapp.com/'>Password Generator</a>.", unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------
# Footer


footer="""<style>

#MainMenu {visibility: hidden;}
a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Made in Streamlit with by <a href='https://github.com/sajinshivdas/PasswordChecker/tree/main/PasswordCheckerScript'>Sajin Shivdas</a>.

</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------



############################################################################################################################# 
#############################################################################################################################
