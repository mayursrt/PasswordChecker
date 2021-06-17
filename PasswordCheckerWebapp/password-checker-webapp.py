import streamlit as st
import requests
import hashlib
from PIL import Image
import sys


#----------------------------------------------------------------------------------------------------------------------------
# Title and Logo

title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 5])
image = Image.open('assets/logo.jpg')
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

st.markdown("<font size=3>This webapp uses the HaveIBeenPwned API to check if the password is included in the Pwned Password Database.</font>", unsafe_allow_html=True)
st.markdown("<font size=5>Pwned Passwords</font>", unsafe_allow_html=True)
st.markdown("<font size=3>Pwned Passwords are 613,584,246 real world passwords previously exposed in data breaches. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts.", unsafe_allow_html=True)
st.markdown("<font color='089e00' size=3>This Check is performed through the API therefore it is safe. Also it uses SHA-256 hashing algorithm to encode entered passwords</font>", unsafe_allow_html=True)
#----------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------
# User Input
st.subheader('Enter your Password')

user_password = st.text_input('', type='password')
#----------------------------------------------------------------------------------------------------------------------------

############################################################################################################################# 
#############################################################################################################################
#----------------------------------------------------------------------------------------------------------------------------
# Functions
def  req_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)

	if res.status_code != 200:
		raise RuntimeError(f'ERROR FETCHING: {res.status_code}, CHECK API AND TRY AGAIN')
	return res

def get_count(hashes, tail_hash):
	hashes =  (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == tail_hash:
			return count
	return 0

def api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = req_api_data(first5_char)
	return get_count(response, tail)


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




#----------------------------------------------------------------------------------------------------------------------------
#Footer
#MainMenu {visibility: hidden;}

footer="""<style>


a:link , a:visited{
color: blue;
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
<p>Made in Streamlit with ❤️ by <a href='https://github.com/mayursrt'>Mayur</a>.

</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

# <a style='display: block; text-align: center;' href="https://github.com/mayursrt" target="_blank">Mayur Machhi</a>

#----------------------------------------------------------------------------------------------------------------------------
# hide_streamlit_style = """
#             <style>
#             footer {visibility: hidden;}
#             footer:after {
# 	content:'Made in streamlit with ❤️ by Mayur'; 
# 	visibility: visible;
# 	display: block;
# 	position: relative;
# 	#background-color: red;
# 	padding: 5px;
# 	top: 2px;
# 	width: 100%;
# background-color: white;
# color: black;
# text-align: center;
# }
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#----------------------------------------------------------------------------------------------------------------------------