import streamlit as st
import requests
import hashlib
from PIL import Image
import sys
import SessionState


#----------------------------------------------------------------------------------------------------------------------------
# Title and Logo

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

""")
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input
st.subheader('Enter your Password')

user_password = st.text_input('', value)


# state = SessionState.get(key=0)

# ta_placeholder = st.empty()

# if st.button('Clear'):
#     state.key += 1

# x = ta_placeholder.text_area('Some text', value='', key=state.key)

# x


#----------------------------------------------------------------------------------------------------------------------------


#############################################################################################################################
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


# count = api_check(user_password)
# if count:
# 	st.markdown(f'{user_password} has been hacked {count} times, time to change your password')
# else:
# 	st.markdown(f'{user_password} is secure')

def main(password):
	count = api_check(password)
	if count:
		st.markdown(f'{password} has been hacked {count} times, time to change your password')
	else:
		st.markdown(f'{password} is secure')
	return 

if user_password:
	main(user_password)


############################################################################################################################# 



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
<p>Made with ❤️ by <a href='https://github.com/mayursrt'>Mayur</a>.

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