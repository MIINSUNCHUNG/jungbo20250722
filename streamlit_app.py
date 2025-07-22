import streamlit as st
import random

st.set_page_config(page_title="무작위 치환형 암호", page_icon="🔐")
st.title("🧠 치환형 암호 기법이란?")

st.write("""
치환형 암호는 **알파벳 각각을 무작위로 다른 알파벳에 1:1 대응시켜 암호화**하는 방식입니다.

이 방식은 단순히 알파벳을 밀어서 바꾸는 시저 암호보다 더 복잡하며, **예측이 어렵기 때문에 보안성이 향상**됩니다.
""")

# 알파벳 정의
original_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
random_alphabet = original_alphabet.copy()
random.seed(42)  # 고정된 랜덤값을 사용 (같은 결과 보장)
random.shuffle(random_alphabet)

# 표시용 문자열
original_display = " ".join(original_alphabet)
random_display = " ".join(random_alphabet)

st.subheader("🔑 무작위 암호 키")
st.code(f"""
원본 알파벳:   {original_display}
암호 알파벳:   {random_display}
""", language="text")

# 암호 매핑 생성
cipher_map = dict(zip(original_alphabet, random_alphabet))

st.subheader("📝 원본 메시지 → 암호 메시지")

plaintext = "HELLO STREAMLIT"
ciphertext = ""

for char in plaintext:
    if char.upper() in cipher_map:
        ciphertext += cipher_map[char.upper()]
    elif char == " ":
        ciphertext += " "
    else:
        ciphertext += char

st.code(f"""
원본 메시지:  {plaintext}
암호 메시지:  {ciphertext}
""", language="text")

st.write("""
이 예시에서는 **고정된 규칙 없이 임의로 대응되는 암호키**를 사용하여 암호화되었습니다.  
동일한 키를 알아야만 복호화가 가능하며, 빈도 분석 등을 통해 해독하는 것도 가능합니다.
""")

st.warning("⚠️ 암호키가 유출되면 해독이 가능하므로, 키 관리는 매우 중요합니다.")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
