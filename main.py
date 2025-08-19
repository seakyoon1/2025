import streamlit as st

# 🎨 MBTI별 스트레스 해소법 데이터 + 이모지
mbti_tips = {
    "ISTJ": "📋 계획 세우기 ✨ 정리 정돈 🗂️ 문제를 차근차근 해결하면 마음이 안정돼요.",
    "ISFJ": "🤗 가까운 사람들과 따뜻한 시간 💞 조용한 휴식 ☕ 따뜻한 차가 큰 힘이 됩니다.",
    "INFJ": "📖 일기 쓰기 ✍️ 깊은 사색 🌌 독서와 명상 🧘‍♂️이 마음을 정리해줘요.",
    "INTJ": "🔮 미래 계획 세우기 📝 혼자만의 시간 ⏳ 책 읽기 📚가 최고의 힐링!",
    
    "ISTP": "🔧 새로운 것 실험하기 🛠️ 만들기 활동 🎮 혼자 집중할 수 있는 게 좋아요.",
    "ISFP": "🌿 자연 속 산책 🚶‍♀️ 음악 🎶 그림 🎨 사진 📸 같은 감각 활동이 효과적이에요.",
    "INFP": "📝 창작 활동 (글쓰기·그림) 🎨 혼자 사색하기 🌌 몽상 ✨이 큰 힘이 돼요.",
    "INTP": "💡 새로운 아이디어 탐구 🤯 깊은 사고 🤓 관심 있는 주제 연구 📚가 스트레스 해소법!",
    
    "ESTP": "⚡ 신나는 운동 🏀 즉흥적인 활동 🎢 사람들과 에너지 충전 🎉!",
    "ESFP": "🎶 음악 듣기 🎤 춤추기 💃 파티 🥳 친구들과 어울리기 👯가 최고예요.",
    "ENFP": "🌈 새로운 경험 ✈️ 친구들과 깊은 대화 💬 웃음 가득한 시간 😂이 활력이 됩니다.",
    "ENTP": "🔥 열띤 토론 🗣️ 새로운 도전 🚀 즉흥적인 모험 🌍이 스트레스 해소법!",
    
    "ESTJ": "📊 일정 관리 📅 책임감 있는 활동 💪 성취감 ✨이 큰 에너지가 됩니다.",
    "ESFJ": "💞 사람들을 돕기 🤝 따뜻한 교류 🫂 가족·친구와 함께하는 시간 🏡이 좋아요.",
    "ENFJ": "🫶 진솔한 대화 💬 의미 있는 활동 🌟 누군가를 돕는 일 🤲이 힐링이에요.",
    "ENTJ": "🎯 목표 세우기 🏆 생산적인 활동 📈 리더십 발휘 👑가 최고의 해소법!"
}

# 🌟 Streamlit 앱 UI
st.set_page_config(page_title="MBTI Stress Relief", page_icon="🌿", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>🌿 MBTI별 스트레스 해소법 ✨</h1>
    <p style='text-align: center; font-size:18px;'>당신의 MBTI를 선택하면 <b>맞춤형 스트레스 해소법</b>을 알려드립니다! 💡</p>
    """,
    unsafe_allow_html=True
)

# 사용자 MBTI 선택
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요:", list(mbti_tips.keys()))

# 결과 출력 (카드 스타일)
if selected_mbti:
    st.markdown(
        f"""
        <div style='
            background: linear-gradient(135deg, #ffecd2, #fcb69f);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            margin-top: 20px;
            text-align: center;
        '>
            <h2 style='color:#2E8B57;'>💡 {selected_mbti} 타입의 스트레스 해소법</h2>
            <p style='font-size:20px; color:#333;'>{mbti_tips[selected_mbti]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# 푸터
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:14px; color:gray;'>✨ Made with ❤️ using Streamlit ✨</p>",
    unsafe_allow_html=True
)
