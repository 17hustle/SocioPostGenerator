import streamlit as st
from fewshots import FewShots
from post_gen import gen_post
length_options = ["Short", "Medium", "High"]
language_options = ["English", "Hinglish"]

def main():
    st.title("Socio Post Generator")
    col1, col2, col3  =st.columns(3)
    fs = FewShots()
    with col1:
        
        selected_tag = st.selectbox("Title", options=fs.get_tags())

    with col2:
        selected_length =st.selectbox("Length", options=length_options)
    
    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = gen_post(selected_length,selected_language,selected_tag)
        st.write(post)
if __name__ == "__main__":
    main()