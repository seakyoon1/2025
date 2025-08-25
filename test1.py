import streamlit as st
from PIL import Image

st.title("🧍‍♂️ 인체 탐험 앱")
st.write("인체 그림에서 장기를 선택하면 설명을 볼 수 있어요!")

# 이미지 불러오기
body_img = Image.open("human_body.png")
st.image(body_img, use_column_width=True)

# 장기 선택 (드롭다운 방식)
organ = st.selectbox("궁금한 장기를 선택하세요 👇", ["심장", "폐", "간", "위", "신장"])

# 장기 설명
organ_info = {
    "심장": "심장은 혈액을 전신에 공급하는 펌프 역할을 합니다 ❤️",
    "폐": "폐는 산소와 이산화탄소를 교환하는 호흡 기관입니다 🌬️",
    "간": "간은 해독, 영양소 저장, 대사 조절을 담당합니다 🧪",
    "위": "위는 음식물을 분해하고 소화를 시작하는 기관입니다 🍴",
    "신장": "신장은 노폐물을 걸러내고 체액 균형을 유지합니다 💧",
}

st.info(organ_info[organ])
