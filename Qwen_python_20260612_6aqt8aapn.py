import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="7월 핵심 표현 집중 퀴즈", page_icon="🇬", layout="centered")

# ==========================================================
# 📚 2025년 7월(Jul 2025) 핵심 표현 학습 데이터
# ==========================================================
QUIZ_DATA = [
    {
        "hint": "(시중에) 모두에게 돌아갈 만큼 설탕이 충분하지 않아요.",
        "sentence": "there's just not enough sugar to ________",
        "answer": "go around",
        "note": "go around: (양이) 모두에게 돌아갈 만큼 충분하다"
    },
    {
        "hint": "설령 코카콜라가 진짜 설탕으로 바꾸고 싶어 한다 해도, 과연 그 일을 해낼 수 있을까요?",
        "sentence": "Even if Coke wanted to make the switch to real sugar, could it ________",
        "answer": "pull it off",
        "note": "pull it off: (어려운 일을) 성공적으로 해내다"
    },
    {
        "hint": "그 발표는 미국인들이 가장 좋아하는 음료 중 하나의 다음 행보가 무엇일지에 대한 엄청난 추측을 불러일으켰습니다.",
        "sentence": "The announcement ________ about what was next for one of America's favorite drinks.",
        "answer": "set off a frenzy of speculation",
        "note": "set off a frenzy of speculation: 엄청난 추측을 불러일으키다"
    },
    {
        "hint": "실제 상황은 방금 말했거나 생각한 것과 정반대입니다.",
        "sentence": "It's ________ really there.",
        "answer": "the other way around",
        "note": "the other way around: 정반대로"
    },
    {
        "hint": "그렇게 해서 설탕에 대한 소문이 급속히 퍼지기 시작했다.",
        "sentence": "And so the sugar ________ ________",
        "answer": "rumor mill went into overdrive",
        "note": "rumor mill: 소문 / go into overdrive: 과속 상태(급속히 퍼지다)"
    },
    {
        "hint": "멕시코 코카콜라는 진짜 짱이야.",
        "sentence": "The coke out of Mexico is ________.",
        "answer": "gas",
        "note": "gas: (영국 슬랭) 정말 훌륭하다, 멋지다"
    },
    {
        "hint": "트럼프의 코카콜라 관련 게시물은 '고과당 옥수수 시럽 반대'라는 시대 정신을 건드렸다.",
        "sentence": "Trump's post about Coke ________ the anti high Fructose Corn Syrup ________.",
        "answer": "tapped into ... zeitgeist",
        "note": "tap into: 건드리다, 활용하다 / zeitgeist: 시대 정신"
    },
    {
        "hint": "우리는 과학, 신경과학, 화학에 푹 빠져서 열정적으로 이야기하는 걸 정말 좋아해요.",
        "sentence": "We love nothing more than ________ about science, neuroscience, and chemistry",
        "answer": "nerding out",
        "note": "nerd out: (특정 주제에) 푹 빠져서 열정적으로 이야기하다"
    },
    {
        "hint": "이 대화를 기꺼이 나눠줘서 고마워",
        "sentence": "thank you for ________ even have this conversation.",
        "answer": "being game to",
        "note": "be game to: 기꺼이 ~하려 하다"
    },
    {
        "hint": "이 이야기는 저희에게 정말 가깝고 개인적으로 와닿는 이야기입니다.",
        "sentence": "Now, this story obviously ________ for us here",
        "answer": "strikes close to home",
        "note": "strike close to home: 가깝고 개인적으로 와닿다"
    },
    {
        "hint": "어쩌면 그녀가 그렇게 묻는 건, 어떻게든 일상의 모습이라도 유지하고 싶어서일지도 몰라요.",
        "sentence": "maybe her questioning comes from this place of like wanting to maintain some ________ of normalcy.",
        "answer": "semblance",
        "note": "semblance of normalcy: 일상의 모습(겉모습)"
    },
    {
        "hint": "정말 참혹하다는 말로는 부족할 정도예요.",
        "sentence": "it's incredibly ________ ________ ________.",
        "answer": "harrowing to say the least",
        "note": "harrowing: 참혹한 / to say the least: 말로는 부족할 정도"
    },
    {
        "hint": "그건 마치 엘 카포네의 금고를 터뜨려 봤더니 먼지랑 빈 병 몇 개만 나온 것 같았다",
        "sentence": "It was like ________ El Capone safe and there was a bit of dirt and some empty bottles.",
        "answer": "blowing open",
        "note": "blow open: (금고 등을) 터뜨리다"
    },
    {
        "hint": "에프스타인 사건은 분명 오랫동안 트럼프 행정부를 따라다니며 괴롭혀 온 문제였다.",
        "sentence": "The Epstein story has certainly been something that's ________ the Trump administration for a very long time.",
        "answer": "dogged",
        "note": "dog: (사람을) 따라다니며 괴롭히다"
    },
    {
        "hint": "결국은 별거 아니었다",
        "sentence": "It was a bit of a ________.",
        "answer": "nothing burger",
        "note": "nothing burger: 별거 아닌 것, 과장된 것에 비해 실속이 없는 것"
    },
    {
        "hint": "이번 공개 계획은 사실상 실패작에 가까웠어요.",
        "sentence": "this planned release was kind of a ________.",
        "answer": "flop",
        "note": "flop: 실패작"
    },
    {
        "hint": "다른 말로 하자면, 유치하다고 표현할 수 있을 것 같아요.",
        "sentence": "I guess another word is like ________ is what I would describe it.",
        "answer": "sophomoric",
        "note": "sophomoric: 유치한, 미성숙한"
    },
    {
        "hint": "예전 보조자가 남긴 메모에는 에프스타인의 이름으로 만든 애크로스틱 퍼즐이 포함되어 있었어요.",
        "sentence": "There was a note from a former assistant that included an ________ with Epstein's name.",
        "answer": "acrostic",
        "note": "acrostic: 머리글자 퍼즐"
    },
    {
        "hint": "이렇게 요리해 주세요'라는 말은 절대 하지 마세요. 그건 셰프에게 대사 지시를 하는 거나 마찬가지고, 셰프들은 그런 걸 싫어하거든요",
        "sentence": "Please never say, cook it like this, because that's giving the chef a ________ and they don't like it.",
        "answer": "line reading",
        "note": "line reading: (배우에게 하는) 대사 지시"
    },
    {
        "hint": "약속하건대, 여덟 번째는 '당신이 아끼는 것을 기꺼이 버릴 줄 아는 것'입니다.",
        "sentence": "I promise number eight is be willing to ________ ________.",
        "answer": "kill your darlings",
        "note": "kill your darlings: (아끼는 것을 과감히) 버리다"
    },
    {
        "hint": "비행기가 땅으로 곤두박질치기 시작하든, 그 순간 나는 아내에게 팔꿈치를 툭 치며 '내 말 맞지?' 하고 으스댈 수 있죠.",
        "sentence": "Either the plane starts ________ towards Earth, at which point I get to elbow sweetie and ________ Was I right?",
        "answer": "nose diving ... gloat",
        "note": "nose dive: 곤두박질치다 / gloat: 으스대다, 우월감을 느끼다"
    },
    {
        "hint": "그러니까 정말로 유치하게 나가세요. 그게 통합니다.",
        "sentence": "So really go for the ________.",
        "answer": "juvenile",
        "note": "juvenile: 유치한, 미성숙한"
    },
    {
        "hint": "처음부터 밑바닥에서 시작해서 위로 올라가려 하지 마라",
        "sentence": "don't ________ ________ ________ the ladder.",
        "answer": "work your way up",
        "note": "work one's way up the ladder: 밑바닥에서 위로 올라가다"
    },
    {
        "hint": "기대는 낮추고, 결과는 더 좋게 만들어라.",
        "sentence": "So always ________ ________ and ________ ________.",
        "answer": "under promise ... over deliver",
        "note": "under promise and over deliver: 기대치는 낮게, 결과는 높게"
    },
    {
        "hint": "내가 아마추어처럼 느껴지지 않고도 자신 있게 카메라맨이라고 말할 수 있었다.",
        "sentence": "I could call myself a cameraman without feeling like a ________.",
        "answer": "dilettante",
        "note": "dilettante: 아마추어, 반쪽짜리"
    },
    {
        "hint": "그것들은 단지 우리가 지닌 날것 그대로인 우리의 기이한 성격들, 사소한 결점들일 수도 있어요.",
        "sentence": "They could just be our ________, our ________ and other SAT words...",
        "answer": "idiosyncrasies ... peccadillos",
        "note": "idiosyncrasies: 기이한 성격 / peccadillos: 사소한 결점"
    },
    {
        "hint": "그 감독이 그 아이디어를 제안했을 때 몰래 들었으면 정말 좋았을 텐데요.",
        "sentence": "I wish I could have been ________ ________ ________ when the director pitched it.",
        "answer": "a fly on the wall",
        "note": "a fly on the wall: 몰래 엿듣는 사람"
    },
    {
        "hint": "요즘 사람들은 연예인이랑 일방적인 관계에 익숙해져서, 그런 일이 있어도 아무렇지 않게 생각하죠.",
        "sentence": "you won't even care because that's how ________ ________ with celebrities work these days.",
        "answer": "Parasocial relationships",
        "note": "Parasocial relationships: 일방적(준사회적) 관계"
    },
    {
        "hint": "웃기고도 날카로운 유머로 가득한, 코미디언 겸 작가 지나의 무대!",
        "sentence": "Laugh in this hilarious and ________ ________ from comedian and screenwriter, Jena",
        "answer": "searing set",
        "note": "searing set: 날카로운(통렬한) 무대/공연"
    },
    {
        "hint": "미국 내 문맹 성인 대다수가 겉보기에는 미국 교육 시스템과 어느 정도 접촉이 있었다는 점을 지적하려는 것이다",
        "sentence": "the majority of illiterate American adults ________ had some kind of interaction with the American school system.",
        "answer": "ostensibly",
        "note": "ostensibly: 겉보기에는, 표면적으로는"
    },
    {
        "hint": "책을 읽는 우리의 능력, 혹은 그 부족함이 최근 사회적 흐름(시대정신) 속에 자리 잡고 있어요.",
        "sentence": "Our ability to read books or our ________ ________ has been in the zeitgeist lately.",
        "answer": "lack thereof",
        "note": "lack thereof: 그 부족함"
    },
    {
        "hint": "그건 인간을 달에 보내는 프로젝트나 암 정복을 위한 국가적 도전 과제처럼 진지하게 다뤄져야 할 문제라고 봐요.",
        "sentence": "And to me that should be seen as sort of like putting a man on the moon or cancer ________.",
        "answer": "moonshot",
        "note": "moonshot: 국가적 도전 과제, 야심 찬 프로젝트"
    },
    {
        "hint": "옥스퍼드가 2024년 올해의 단어로 'brain rot(두뇌 부패)'를 선정했다는 건, 우리는 이미 끝났다는 뜻이에요",
        "sentence": "we are ________ when Oxford's 2024 Word of the Year was ________.",
        "answer": "cooked ... brain rot",
        "note": "cooked: (슬랭) 끝났다, 망했다 / brain rot: 두뇌 부패"
    },
    {
        "hint": "그냥 넘을 수 없는 산처럼 느껴져요.",
        "sentence": "it just feels like this ________ mountain.",
        "answer": "insurmountable",
        "note": "insurmountable: 넘을 수 없는, 극복할 수 없는"
    },
    {
        "hint": "비밀 하나 알려줄게요",
        "sentence": "I'll ________ you ________ ________ a secret",
        "answer": "let ... in on",
        "note": "let someone in on a secret: 비밀을 알려주다"
    },
    {
        "hint": "전 세계 수억 명의 소농들이 내 입장에 처해 있다는 생각을 하지 않을 수 없었어요.",
        "sentence": "I couldn't help but think about hundreds of millions of small holder farmers all around the world who ________ my ________.",
        "answer": "wear ... shoes",
        "note": "wear someone's shoes: 누구의 입장에 처하다"
    },
    {
        "hint": "믿음을 가지고 용기 있게 도전했어요",
        "sentence": "I took a ________ of ________",
        "answer": "leap ... faith",
        "note": "leap of faith: 믿음의 도약, 용기 있는 도전"
    },
    {
        "hint": "쓴웃음을 지으며 말했어요. 악마는 거짓말쟁이야(말도 안 돼)라고요.",
        "sentence": "I laughed bitterly and told her, ________ ________ is a ________.",
        "answer": "the devil ... liar",
        "note": "the devil is a liar: 악마는 거짓말쟁이야(말도 안 되는 소리)"
    },
    {
        "hint": "눈물을 흘리며 밤새 뒤척였다.",
        "sentence": "I ________ ________, tears in my eyes.",
        "answer": "lay awake",
        "note": "lie awake: (잠이 오지 않아) 뒤척이다"
    },
    {
        "hint": "은하수와 안드로메다가 서로를 공전하는 모습을 마치 운명적인 파멸을 향한 연인의 춤 같다고 묘사했어요.",
        "sentence": "the professor described the Milky Way andromeda's orbiting each other almost in a lover's ________ of ________.",
        "answer": "dance ... doom",
        "note": "dance of doom: 운명적인 파멸을 향한 춤"
    },
    {
        "hint": "그 사람의 공을 가로채고 싶진 않아서, 여러분이 우리 대화를 직접 들어보게 하려고요",
        "sentence": "I don't wanna ________ his ________, so I'm gonna let you listen to our conversation yourself.",
        "answer": "steal ... thunder",
        "note": "steal someone's thunder: 공을 가로채다"
    },
    {
        "hint": "그들은 서로에게 이끌리고 있어요 — 하지만 그것이 결국 그들에게 위험이 될 거예요",
        "sentence": "They're just drawn to each other ________ their ________",
        "answer": "to ... peril",
        "note": "to one's peril: 결국 (자신에게) 위험이 되도록"
    },
    {
        "hint": "우주가 아직 젊고 작고 뜨거웠을 때는 이런 병합(충돌)이 일어나는 게 당연했어요.",
        "sentence": "When the universe is young and small and hot, these mergers are ________ ________ happen.",
        "answer": "bound to",
        "note": "bound to: ~하게 되어 있다, 당연하다"
    },
    {
        "hint": "그렇다면 안드로메다 은하가 정말 우리 은하와 충돌하게 된다면 어떤 일이 벌어질까요?",
        "sentence": "So what could happen if Andromeda Galaxy does kind of ________ ________ us?",
        "answer": "ram into",
        "note": "ram into: (강하게) 충돌하다"
    },
    {
        "hint": "우리 태양계를 벗어나 조금 더 멀리 시야를 넓혀봅시다.",
        "sentence": "let's ________ ________ past our solar system.",
        "answer": "zoom out",
        "note": "zoom out: (시야를) 넓히다, 물러나다"
    },
    {
        "hint": "이 글은 제 인생에서 가장 크고 중요한 결정 중 하나를 내리려던 시점에 쓴 것입니다.",
        "sentence": "I wrote this when I was ________ the ________ of making one of the biggest and most significant decisions of my life",
        "answer": "on ... cusp",
        "note": "on the cusp of: ~직전의 시점, 기로에 서다"
    },
    {
        "hint": "사제가 되는 것을 분별할 때 결혼하지 않는 독신 생활이 이 길의 일부라는 걸 알고 있었지만",
        "sentence": "I knew in discerning ministry that celibacy not getting married was ________ ________ the ________",
        "answer": "part ... package",
        "note": "part of the package: (떼려야 뗄 수 없는) 일부"
    },
    {
        "hint": "창의적인 일이긴 하지만, 예전처럼 활력이 느껴지진 않아요.",
        "sentence": "It's a creative role, but you don't quite feel you've got that ________",
        "answer": "zing",
        "note": "zing: 활력, 생동감"
    },
    {
        "hint": "그가 그냥 이 상황을 넘기고 감정을 억누르려 했다면 훨씬 쉬웠을 거예요.",
        "sentence": "It would've been so easy for him to have just ________ ________ this to try and suppress the emotions",
        "answer": "pushed past",
        "note": "push past: (감정이나 상황을) 넘기다, 억누르다"
    },
    {
        "hint": "성찰은 이 문제를 해결하는 데 도움이 되는 귀중한 통찰의 보고를 제공합니다.",
        "sentence": "Reflection provides a ________ ________ of data to help you ________ ________ this.",
        "answer": "treasure trove ... work through",
        "note": "treasure trove: 보물의 창고(귀중한 보고) / work through: 해결하다"
    },
    {
        "hint": "당신이 경이로움을 느끼는 순간에 온전히 몰입하라고요. ... 그걸 아무런 거리낌 없이 즐기세요.",
        "sentence": "I always tell people to ________ ________ your awe... and do that ________ as long as it's safe",
        "answer": "lean into ... unapologetically",
        "note": "lean into: 몰입하다 / unapologetically: 거리낌 없이, 당당하게"
    },
    {
        "hint": "모든 순간마다 뭔가 잘못됐을 때 ... 손이 날아가지 않기만을 바라곤 했어요.",
        "sentence": "Every moment, I was sort of thinking about like what I would do if something went wrong... hoping I wasn't gonna ________ my hand ________",
        "answer": "blow ... up",
        "note": "blow up: (폭발로) 날아가다, 파괴되다"
    },
    {
        "hint": "무슨 일이 있었던 걸까, 그게 아마도 그들이 혼란스러운 경험을 찾는 쪽으로 방향을 전환하게 만든 건 아닐까?",
        "sentence": "is it something happen that sort of may have ________ them ________ sort of seeking chaotic experiences.",
        "answer": "pivoted ... towards",
        "note": "pivot towards: ~쪽으로 방향을 전환하다"
    },
    {
        "hint": "바다로 떠밀려 갈 위험이 없기만 하면, 아무리 물이 차가워도 여전히 바다에 나간다고 합니다.",
        "sentence": "as long as there's not a risk that they're going to be ________ ________ ________ sea, then they still go out in the water",
        "answer": "blown away to",
        "note": "blown away to sea: 바다로 떠밀려 가다"
    }
]

# ==========================================================
# 세션 상태 관리
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
def generate_options(correct_answer, all_data):
    """정답 1개와 오답 3개를 섞어 4지 선다 보기를 생성합니다."""
    wrong_options = [item["answer"] for item in all_data if item["answer"] != correct_answer]
    sampled_wrongs = random.sample(wrong_options, min(3, len(wrong_options)))
    options = [correct_answer] + sampled_wrongs
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
st.title("🇬 7월 핵심 표현 집중 퀴즈")
st.caption("문장 전체가 아닌, 각 문장의 핵심 표현(구/숙어)만 집중적으로 익혀보세요!")
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
        st.markdown("👑 완벽합니다! 7월 핵심 표현을 모두 마스터하셨네요!")
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
    
    # 사이드바에 진행률 표시
    with st.sidebar:
        st.header("📊 진행 현황")
        st.progress((st.session_state.current_idx) / total_q)
        st.metric("문제", f"{st.session_state.current_idx + 1} / {total_q}")
        st.metric("현재 점수", f"{st.session_state.score} / {st.session_state.current_idx}")
        st.divider()
        if st.button("🔄 퀴즈 리셋", use_container_width=True):
            reset_quiz()
            st.rerun()

    # 힌트 표시 (한국어 번역)
    st.markdown(f"### 💡 힌트 (한국어): {current_q['hint']}")
    
    # 영어 문장 표시 (빈칸 포함)
    st.markdown(f"### 📝 영어 문장 (빈칸 채우기):")
    st.info(f"**{current_q['sentence']}**")
    
    # 보기 생성 (세션 상태에 저장하여 리렌더링 시 변경되지 않게 함)
    if not st.session_state.current_options or not st.session_state.show_feedback:
        st.session_state.current_options = generate_options(current_q["answer"], st.session_state.quiz_data)
    
    options = st.session_state.current_options
    
    # 라디오 버튼으로 선택 (피드백이 보일 때는 비활성화)
    selected = st.radio(
        "빈칸에 들어갈 알맞은 표현을 선택하세요:",
        options,
        index=None,
        disabled=st.session_state.show_feedback,
        key="quiz_radio"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ 정답 확인", type="primary", disabled=(selected is None or st.session_state.show_feedback), use_container_width=True):
            check_answer(selected, current_q["answer"])
            st.rerun()
            
    with col2:
        if st.button("➡️ 다음 문제", disabled=not st.session_state.show_feedback, use_container_width=True):
            next_question()
            st.rerun()

    # 피드백 표시
    if st.session_state.show_feedback:
        st.markdown("---")
        # 빈칸이 채워진 전체 문장 보여주기
        filled_sentence = current_q["sentence"].replace("________", f"**{current_q['answer']}**")
        st.markdown(f"#### 📝 완성된 문장:")
        st.success(f"`{filled_sentence}`")
        
        if st.session_state.selected_answer == current_q["answer"]:
            st.success("✅ **정답입니다!** 훌륭해요.")
        else:
            st.error(f"❌ **틀렸습니다.**")
            st.markdown(f"👉 **정답 표현:** `{current_q['answer']}`")
            
        if current_q["note"]:
            st.markdown(f"📌 **노트:** {current_q['note']}")
