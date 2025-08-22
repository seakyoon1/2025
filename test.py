import streamlit as st
import pandas as pd
from PIL import Image

# --------------------
# 1. 장기 데이터 준비
# --------------------
organs = [
    {
        "name": "심장 (Heart ❤️)",
        "category": "순환기계",
        "function": "혈액을 온몸에 순환시키는 펌프 역할",
        "diseases": "심근경색, 부정맥, 고혈압",
        "fact": "심장은 하루 약 10만 번 뛴다."
    },
    {
        "name": "폐 (Lungs 🫁)",
        "category": "호흡기계",
        "function": "산소를 혈액으로 전달하고 이산화탄소를 배출",
        "diseases": "폐렴, 천식, 폐암",
        "fact": "성인의 폐에는 약 3억 개의 폐포가 있다."
    },
    {
        "name": "간 (Liver 🩸)",
        "category": "소화기계",
        "function": "해독, 단백질 합성, 에너지 저장",
        "diseases": "간염, 간경화, 간암",
        "fact": "간은 인체에서 가장 큰 내장 기관이다."
    },
    {
        "name": "위 (Stomach 🍲)",
        "category": "소화기계",
        "function": "음식을 분해하고 소화 효소 분비",
        "diseases": "위염, 위궤양, 위암",
        "fact": "위액은 염산을 포함하여 음식물을 분해한다."
    },
    {
        "name": "신장 (Kidneys 🫘)",
        "category": "배설기계",
        "function": "노폐물과 수분을 걸러 소변 생성",
        "diseases": "신부전, 신결석",
        "fact": "신장은 하루에 약 50갤런의 혈액을 여과한다."
    },
    {
        "name": "소장 (Small Intestine ➰)",
        "category": "소화기계",
        "function": "영양소 흡수",
        "diseases": "장염, 크론병",
        "fact": "소장은 길이가 약 6m에 달한다."
    },
    {
        "name": "대장 (Large Intestine 🔄)",
        "category": "소화기계",
        "function": "수분 흡수와 대변 형성",
        "diseases": "대장암, 과민성 대장증후군",
        "fact": "대장은 약 1.5m 길이로 수분을 재흡수한다."
    },
    {
        "name": "췌장 (Pancreas 🧪)",
        "category": "소화기계",
        "function": "인슐린 분비와 소화 효소 생산",
        "diseases": "당뇨병, 췌장염",
        "fact": "췌장은 혈당 조절에 중요한 기관이다."
    },
    {
        "name": "뇌 (Brain 🧠)",
        "category": "신경계",
        "function": "신체 기능 조절과 정보 처리",
        "diseases": "치매, 뇌졸중, 파킨슨병",
        "fact": "성인 뇌는 약 860억 개의 뉴런으로 구성된다."
    },
    {
        "name": "피부 (Skin 🩹)",
        "category": "외피계",
        "function": "신체 보호와 체온 조절",
        "diseases": "피부염, 피부암",
        "fact": "피부는 인체에서 가장 큰 장기이다."
    }
]

organs_df = pd.DataFrame(organs)

# --------------------
# 2. Streamlit UI
# --------------------
st.set_page_config(page_title="인체 장기 지도", page_icon="🧍", layout="wide")

st.title("🧍 인체 장기 3D 지도 (기본 버전)")
st.write("장기를 선택하면 기능, 관련 질환, 흥미로운 사실을 볼 수 있습니다.")

# 사이드바 - 장기 선택
st.sidebar.header("🔍 장기 선택")
organ_names = organs_df["name"].tolist()
selected_organ = st.sidebar.selectbox("보고 싶은 장기를 선택하세요", organ_names)

# 메인 화면 - 이미지 표시
body_img = Image.open("human_body.png")  # 인체 이미지 파일 필요 (같은 폴더에 저장)
st.image(body_img, caption="인체 그림", use_column_width=True)

# 선택한 장기 정보 표시
organ_info = organs_df[organs_df["name"] == selected_organ].iloc[0]

st.subheader(f"{organ_info['name']}")
st.markdown(f"**🧩 계통:** {organ_info['category']}")
st.markdown(f"**⚙️ 기능:** {organ_info['function']}")
st.markdown(f"**🩺 관련 질환:** {organ_info['diseases']}")
st.markdown(f"**💡 흥미로운 사실:** {organ_info['fact']}")

st.success("좌측 사이드바에서 다른 장기를 선택해보세요!")

