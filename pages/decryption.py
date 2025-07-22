import streamlit as st
import random

st.set_page_config(page_title="복호화 체험", page_icon="🔓")
st.title("🔓 복호화 실습")

st.write("암호키와 암호문을 보고, 원래 문장을 유추해보세요!")

# 고정 암호 키 설정
original_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cipher_alphabet = list("QWERTYUIOPASDFGHJKLZXCVBNM")  # 규칙 없는 무작위 대응
decrypt_map = dict(zip(cipher_alphabet, original_alphabet))

# 문제 목록
plaintext_samples = [
    "HELLO STREAMLIT",
    "SUBSTITUTION CIPHER",
    "PYTHON IS FUN",
    "ENCRYPTION DECRYPTION",
    "I LOVE CRYPTOGRAPHY",
    "SECRET MESSAGE",
    "LET US BREAK THIS CODE",
    "TRY TO DECRYPT THIS",
    "STREAMLIT IS AWESOME",
    "MONOALPHABETIC CIPHER"
]

# 세션 상태 초기화
if "selected_index" not in st.session_state:
    st.session_state.selected_index = random.randint(0, 9)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# 암호화 함수
def encrypt(msg, cipher_map):
    result = ""
    for c in msg.upper():
        if c in cipher_map:
            result += cipher_map[c]
        elif c == " ":
            result += " "
        else:
            result += c
    return result

# 🔄 문제 바꾸기 버튼
if st.button("🔄 문제 바꾸기"):
    st.session_state.selected_index = random.randint(0, 9)
    st.session_state.attempts = 0
    st.session_state.show_answer = False

# 선택된 문제 가져오기
selected_plaintext = plaintext_samples[st.session_state.selected_index]
cipher_map = dict(zip(original_alphabet, cipher_alphabet))
selected_ciphertext = encrypt(selected_plaintext, cipher_map)

st.subheader("🔐 암호문:")
st.code(selected_ciphertext)

# 사용자 입력
user_input = st.text_input("복호화한 문장을 입력하세요 (대문자만, 공백 포함):")

if user_input:
    if user_input.upper() == selected_plaintext:
        st.success("✅ 정답입니다!")
        st.session_state.attempts = 0
        st.session_state.selected_index = random.randint(0, 9)
        st.session_state.show_answer = False
    else:
        st.session_state.attempts += 1
        if st.session_state.attempts >= 3:
            st.session_state.show_answer = True
            st.error("❌ 오답입니다. 3번 시도하셨습니다. 정답을 확인하세요.")
        else:
            st.error(f"❌ 다시 해보세요. (시도 {st.session_state.attempts}/3)")

# 정답 공개
if st.session_state.show_answer:
    st.info(f"✅ 정답: `{selected_plaintext}`")
    if st.button("🔁 새 문제로 넘어가기"):
        st.session_state.selected_index = random.randint(0, 9)
        st.session_state.attempts = 0
        st.session_state.show_answer = False

# 암호키 보기
with st.expander("💡 암호 키 보기"):
    original_display = " ".join(original_alphabet)
    cipher_display = " ".join(cipher_alphabet)
    st.code(f"""
암호 알파벳:   {cipher_display}
원본 알파벳:   {original_display}
""", language="text")
