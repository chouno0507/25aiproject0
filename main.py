import streamlit as st

# MBTI 유형 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI 궁합 추천 데이터
mbti_matches = {
    "INTJ": ("ENFP", "ENFP는 감정과 즉흥성을 통해 INTJ의 논리적이고 계획적인 성향을 균형 잡아줍니다."),
    "INTP": ("ESFJ", "ESFJ는 INTP의 내향적이고 분석적인 면을 보완하며 현실적인 안정감을 줍니다."),
    "ENTJ": ("INFP", "INFP의 따뜻함과 이상주의는 ENTJ의 추진력과 리더십을 부드럽게 완화시킵니다."),
    "ENTP": ("INFJ", "INFJ의 깊은 통찰력은 ENTP의 창의성과 에너지에 깊이를 더합니다."),
    "INFJ": ("ENFP", "ENFP의 외향성과 열정은 INFJ의 내향적이면서 신중한 면을 열어줍니다."),
    "INFP": ("ENFJ", "ENFJ는 INFP의 감성을 존중하면서도 사회적 관계를 넓히는 데 도움을 줍니다."),
    "ENFJ": ("INFP", "INFP의 진정성과 감정은 ENFJ의 지도력과 조화를 이룹니다."),
    "ENFP": ("INTJ", "INTJ의 체계적인 사고는 ENFP의 창의성을 실현 가능하게 도와줍니다."),
    "ISTJ": ("ESFP", "ESFP는 ISTJ의 계획성과 책임감에 생기를 불어넣습니다."),
    "ISFJ": ("ESTP", "ESTP의 활동성과 유연함이 ISFJ의 헌신적인 성격에 활력을 줍니다."),
    "ESTJ": ("ISFP", "ISFP의 부드러움과 감성이 ESTJ의 실용적인 성향을 부드럽게 해줍니다."),
    "ESFJ": ("INTP", "INTP의 깊이 있는 사고는 ESFJ의 사교성과 균형을 이룹니다."),
    "ISTP": ("ENFJ", "ENFJ는 ISTP의 고요함 속에 숨은 가치를 이끌어낼 수 있습니다."),
    "ISFP": ("ESTJ", "ESTJ의 조직력은 ISFP의 감성을 안전하게 보호합니다."),
    "ESTP": ("ISFJ", "ISFJ의 안정적인 성향은 ESTP의 즉흥적인 행동에 중심을 잡아줍니다."),
    "ESFP": ("ISTJ", "ISTJ는 ESFP의 활기찬 삶에 실용적인 균형을 제공합니다."),
}

# Streamlit UI
st.title("💍 MBTI 궁합 추천 웹앱")
st.subheader("당신의 MBTI를 선택하면 결혼에 가장 적합한 궁합을 알려드릴게요!")

# 사용자 MBTI 선택
user_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", mbti_types)

if user_mbti:
    match_mbti, reason = mbti_matches.get(user_mbti, ("알 수 없음", "해당 궁합 정보가 없습니다."))
    st.markdown("---")
    st.success(f"✅ 당신에게 가장 잘 맞는 결혼 MBTI는: **{match_mbti}** 입니다!")
    st.markdown(f"**이유:** {reason}")
