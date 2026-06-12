import streamlit as st
import random
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="영어 표현 암기 퀴즈", page_icon="🇬🇧", layout="centered")

# ==========================================================
# 📚 2025년 7월(Jul 2025) 학습 데이터
# ==========================================================
QUIZ_DATA = [
    {"hint": "(시중에) 모두에게 돌아갈 만큼 설탕이 충분하지 않아요.", "answer": "there's just not enough sugar to go around", "note": ""},
    {"hint": "설령 코카콜라가 진짜 설탕으로 바꾸고 싶어 한다 해도, 과연 그 일을 해낼 수 있을까요?", "answer": "Even if Coke wanted to make the switch to real sugar, could it pull it off", "note": "pull it off: 성공적으로 해내다"},
    {"hint": "그 발표는 미국인들이 가장 좋아하는 음료 중 하나의 다음 행보가 무엇일지에 대한 엄청난 추측을 불러일으켰습니다.", "answer": "The announcement set off a frenzy of speculation about what was next for one of America's favorite drinks.", "note": "set off a frenzy of speculation: 엄청난 추측을 불러일으키다"},
    {"hint": "실제 상황은 방금 말했거나 생각한 것과 정반대입니다.", "answer": "It's the other way around really there.", "note": "the other way around: 정반대로"},
    {"hint": "그렇게 해서 설탕에 대한 소문이 급속히 퍼지기 시작했다.", "answer": "And so the sugar rumor mill went into overdrive", "note": "rumor mill: 소문, overdrive: 과속 상태"},
    {"hint": "멕시코 코카콜라는 진짜 짱이야.", "answer": "The coke out of Mexico is gas.", "note": "gas: (영국 슬랭) 정말 훌륭하다, 멋지다"},
    {"hint": "정말 참혹하다는 말로는 부족할 정도예요.", "answer": "it's incredibly harrowing to say the least.", "note": "harrowing: 몹시 참혹한, 고통스러운"},
    {"hint": "결국은 별거 아니었다.", "answer": "It was a bit of a nothing burger.", "note": "nothing burger: 별것 아닌 것, 과장된 것에 비해 실속이 없는 것"},
    {"hint": "기대는 낮추고, 결과는 더 좋게 만들어라.", "answer": "So always under promise and over deliver.", "note": "under promise and over deliver: 기대치는 낮게, 결과는 높게"},
    {"hint": "내가 아마추어처럼 느껴지지 않고도 자신 있게 카메라맨이라고 말할 수 있었다.", "answer": "I could call myself a cameraman without feeling like a dilettante.", "note": "dilettante: 아마추어, 반쪽짜리"},
    {"hint": "요즘 사람들은 연예인이랑 일방적인 관계에 익숙해져서, 그런 일이 있어도 아무렇지 않게 생각하죠.", "answer": "you won't even care because that's how Parasocial relationships with celebrities work these days.", "note": "Parasocial relationships: 일방적(준사회적) 관계"},
    {"hint": "그냥 넘을 수 없는 산처럼 느껴져요.", "answer": "it just feels like this insurmountable mountain.", "note": "insurmountable: 넘을 수 없는, 극복할 수 없는"},
    {"hint": "비밀 하나 알려줄게요.", "answer": "I'll let you in on a secret", "note": "let someone in on a secret: 비밀을 알려주다"},
    {"hint": "믿음을 가지고 용기 있게 도전했어요.", "answer": "I took a leap of faith", "note": "leap of faith: 믿음의 도약, 용기 있는 도전"},
    {"hint": "성찰은 이 문제를 해결하는 데 도움이 되는 귀중한 통찰의 보고를 제공합니다.", "answer": "Reflection provides a treasure trove of data to help you work through this.", "note": "treasure trove: 보물의 창고, 귀중한 보고"}
]

# ==========================================================
# 🧠 세션 상태 관리
# ==========================================================
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = QUIZ_DATA.copy()
    random.shuffle(st.session_state.quiz_data)
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.show_feedback = False
    st.session_state.selected_answer = None
    st.session_state.quiz_finished = False
    st.session_state.current_options = []

# ==========================================================
# 🎮 퀴즈 로직 함수
# ==========================================================
def generate_options(correct_item, all_data):
    wrong_options = [item for item in all_data if item["answer"] != correct_item["answer"]]
    sampled_wrongs = random.sample(wrong_options, min(3, len(wrong_options)))
    options = [correct_item["answer"]] + [item["answer"] for item in sampled_wrongs]
    random.shuffle(options)
    return options

def check_answer(selected, correct):
    st.session_state.show_feedback = True
    st.session_state.selected_answer = selected
    if selected == correct:
        st.session_state.score += 1

def next_question():
    st.session_state.current_idx += 1
    st.session_state.show_feedback = False
    st.session_state.selected_answer = None
    if st.session_state.current_idx >= len(st.session_state.quiz_data):
        st.session_state.quiz_finished = True

def reset_quiz():
    st.session_state.quiz_data = QUIZ_DATA.copy()
    random.shuffle(st.session_state.quiz_data)
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.show_feedback = False
    st.session_state.selected_answer = None
    st.session_state.quiz_finished = False
    st.session_state.current_options = []

# ==========================================================
# 🎨 UI (화면) 구성
# ==========================================================
st.title("🇬🇧 영어 표현 암기 퀴즈")
st.markdown("---")

if st.session_state.quiz_finished:
    # 🏆 결과 화면
    total = len(st.session_state.quiz_data)
    score = st.session_state.score
    accuracy = (score / total) * 100
    
    st.success(f"🎉 퀴즈 완료! 최종 점수: **{score} / {total}**")
    st.progress(accuracy / 100)
    st.markdown(f"### 정답률: {accuracy:.1f}%")
    
    if accuracy == 100:
        st.balloons()
        st.markdown("👑 완벽합니다! 7월 표현을 모두 마스터하셨네요!")
    elif accuracy >= 80:
        st.markdown("👏 아주 훌륭합니다! 조금만 더 복습하면 완벽해질 거예요.")
    else:
        st.markdown("💪 틀린 문제는 노트와 함께 다시 한번 복습해 보세요!")
    
    if st.button("🔄 퀴즈 다시 시작", type="primary"):
        reset_quiz()
        st.rerun()

else:
    # ❓ 퀴즈 진행 화면
    current_q = st.session_state.quiz_data[st.session_state.current_idx]
    total_q = len(st.session_state.quiz_data)
    
    # 진행률 표시
    st.progress((st.session_state.current_idx) / total_q)
    st.caption(f"문제 {st.session_state.current_idx + 1} / {total_q}")
    
    st.markdown(f"### 💡 힌트: {current_q['hint']}")
    
    # 보기 생성 (세션 상태에 저장하여 리렌더링 시 변경되지 않게 함)
    if not st.session_state.current_options or not st.session_state.show_feedback:
        st.session_state.current_options = generate_options(current_q, st.session_state.quiz_data)
    
    options = st.session_state.current_options
    
    # 라디오 버튼으로 선택 (피드백이 보일 때는 비활성화)
    selected = st.radio(
        "알맞은 영어 문장을 선택하세요:",
        options,
        index=None,
        disabled=st.session_state.show_feedback,
        key="quiz_radio"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ 정답 확인", type="primary", disabled=(selected is None or st.session_state.show_feedback)):
            check_answer(selected, current_q["answer"])
            st.rerun()
            
    with col2:
        if st.button("➡️ 다음 문제", disabled=not st.session_state.show_feedback):
            next_question()
            st.rerun()

    # 피드백 표시
    if st.session_state.show_feedback:
        st.markdown("---")
        if st.session_state.selected_answer == current_q["answer"]:
            st.success("✅ **정답입니다!** 훌륭해요.")
        else:
            st.error(f"❌ **틀렸습니다.**")
            st.markdown(f"👉 **정답:** `{current_q['answer']}`")
            
        if current_q["note"]:
            st.info(f"📝 **노트:** {current_q['note']}")
