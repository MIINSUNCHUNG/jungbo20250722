import streamlit as st

st.set_page_config(page_title="복호화 체험", page_icon="🔓")
st.title("🔓 복호화 실습")

st.write("아래 제공된 **암호키**와 **암호문**을 보고, 원래의 문장을 복원해 보세요!")

# 고정된 암호키
original_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cipher_alphabet = list("UDAQCZGMHYXTKEFBINOSPRLJW")  # 이전 예시와 일치
cipher_map = dict(zip(cipher_alphabet, original_alphabet))

# 고정된 암호문 예시
ciphertext = "MCTTT NPOUCVTXP"
correct_plaintext = "HELLO STREAMLIT"

# 사용자 입력
st.subheader("🔐 암호문:")
st.code(ciphertext)

user_input = st.text_input("복호화한 결과를 입력해 보세요 (대문자만):")

if user_input:
    if user_input.upper() == correct_plaintext:
        st.success("✅ 정답입니다!")
    else:
        st.error("❌ 다시 해보세요.")

# 힌트용 암호키 보기
with st.expander("💡 암호 키 보기"):
    original_display = " ".join(original_alphabet)
    cipher_display = " ".join(cipher_alphabet)
    st.code(f"""
암호 알파벳:   {cipher_display}
원본 알파벳:   {original_display}
""", language="text")
