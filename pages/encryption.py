import streamlit as st
import random
import string

st.set_page_config(page_title="암호화 체험", page_icon="🔐")
st.title("🔐 암호화 실습")

st.write("원하는 메시지를 입력하고 무작위로 생성된 암호키를 사용하여 암호문을 생성해보세요!")

# 암호키 고정 or 새로 생성
if "cipher_key" not in st.session_state:
    st.session_state["cipher_key"] = random.sample(string.ascii_uppercase, 26)

def regenerate_key():
    st.session_state["cipher_key"] = random.sample(string.ascii_uppercase, 26)

# 새로고침 버튼
if st.button("🔄 암호 키 새로고침"):
    regenerate_key()

# 키 표시
original_alphabet = list(string.ascii_uppercase)
cipher_alphabet = st.session_state["cipher_key"]

original_display = " ".join(original_alphabet)
cipher_display = " ".join(cipher_alphabet)

st.subheader("🔑 현재 암호 키")
st.code(f"""
원본 알파벳:   {original_display}
암호 알파벳:   {cipher_display}
""", language="text")

# 사용자 입력
plaintext = st.text_input("암호화할 메시지를 입력하세요 (대문자, 띄어쓰기 포함 가능):", "HELLO STREAMLIT")

# 암호화 수행
cipher_map = dict(zip(original_alphabet, cipher_alphabet))

ciphertext = ""
for char in plaintext.upper():
    if char in cipher_map:
        ciphertext += cipher_map[char]
    else:
        ciphertext += char  # 띄어쓰기, 특수문자 등

st.subheader("🧾 암호화된 메시지")
st.code(ciphertext)
