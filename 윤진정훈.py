import streamlit as st
import time

# --- 1. 초기 설정 및 시작 화면 ---
st.set_page_config(layout="wide")
st.title("🏫 서울국제고 F3 선생님과의 데이트 시뮬레이션")

# 사용자 이름 입력 받기 (st.text_input 사용)
# st.session_state는 Streamlit에서 변수 상태를 유지하기 위해 사용됩니다.
if 'name' not in st.session_state:
    st.session_state.name = ''
    st.session_state.stage = 0
    st.session_state.quiz_answers = ['X', 'X', 'O']
    st.session_state.quiz_index = 0

if st.session_state.name == '':
    user_input = st.text_input('사용자의 이름(성 제외)을 입력하시오:', key='input_name')
    if user_input:
        st.session_state.name = user_input
        st.session_state.stage = 1
        st.experimental_rerun() # 이름 입력 후 페이지 새로고침

# --- 2. 다이얼로그 및 스토리 진행 ---
if st.session_state.stage >= 1:
    name = st.session_state.name
    
    # 1부 대사
    dialogues_part1 = [
        f'이제 {name}님은 서울국제고의 최고 미남 선생님들, 일명 f3와 만나게 될 예정입니다. 그럼 즐거운 시간 되시길 바랍니다^^',
        '엔터키를 누르면 대사가 넘어갑니다.',
        f"{name}: 어..? 여긴 어디지?",
        "???: 으앗 내 돌이!!!!! 안돼!!! (정체불명의 사람이 당신을 밀친다)",
        f"{name}: 누구...세요?",
        "황석규 선생님: 내 이름은 황석규. 요 인근에 희귀한 돌이 있다고 해서 가고 있던 중이에요.",
        f"{name}: (자세히 보니 이 선생님 어디서 많이 뵌 분 같은데.. 설마.. 전설의 돌 수집가로 알려져 있는 서울국제고의 황석규 선생님?!)",
        f"{name}: 혹시… 황석규 선생님 맞으신가요?",
        "황석규 선생님: (놀라는 표정을 지으며) 내 이름을 어떻게 아는지.. 아니 그것보다 내가 중국에서 데려온 145번째 아기 돌을 학생이 깔고 있습니다앗! 빨리 나오세요!",
        f"{name}: 아앗 죄송해요!ㅜㅜ 이건.. 미크로파키케팔로사우루스 아닌가요?",
        "선생님께서 놀란 기색이 역력하다. 갑자기 눈에 안광이 생기신다.",
        "황석규 선생님: 이 화석 이름을 알다니.. 학생은 정말 제 지구과학 수업을 들을 자격이 있는 학생이네요.",
        "system: 당신에 대한 황석규 선생님의 호감도 +100",
        "황석규 선생님: (혼잣말 아닌 혼잣말로) 아…하하하하 이렇게 훌륭한 학생은 처음이야… 크크큭 당장 호주로 같이 가서 화석을 몰래 가져오고 싶군…… 화석이 2배나 된다니!! 짜릿해~",
        f"{name}: (같이 화석 줍기라니.. 아직은 조금 이른 것 같은데..) 그럼 먼저 가보겠습니다!",
        f"{name}(이)는 선생님께 급하게 인사하고 다시 돌아간다. 뒤에서 선생님께서 뭐라고 외치는 소리가 들렸지만 아직은 섣불리 마음을 결정하고 싶지 않았다.",
        "빠른 걸음으로 걷다 보니 학교 본관으로 보이는 곳으로 들어왔다.",
        f"어떤 사람이 {name}와 또래로 보이는 학생과 대화하고 있는 것을 발견한다. 그때 그분과 눈이 마주친다. {name}을 보자마자 느리지만 빠르게 다가온다.",
        f"???: 아… 우리 {name}은(는) 공부 잘 하고 있으신가… 수능에서 서울과고 이길려면 열심히 해야할텐데.",
        f"system: {name}은 어딘가 들었던 말투라고 생각하며 대화를 이어간다.",
        f"{name}: 어엇.. 뭔가 익숙한 말투같은데..",
        "???: 아 잠깐 비켜주시죠, 지금 맛있는 국밥집을 가야해서..",
        f"{name}: 앗, 국밥집이라면.. 설마 박계현 선생님?? 지금 성균관대 앞에 있는 일송칼국수에 가시는 건가요?",
        f"박계현 선생님: 아니.. {name}은(는) 일송칼국수를 압니까? 언제 한번 같이 먹으러 가시죠",
        f"{name}: 엇 좋습니다!",
        "system: 설국의 두번째 최고 미남인 박계현 선생님과 함께 다음 음식 중 무엇을 먹으러 갈지 결정해주세요."
    ]

    # 다이얼로그 출력 (버튼을 눌러 진행)
    if 'dialogue_index' not in st.session_state:
        st.session_state.dialogue_index = 0
    
    if st.session_state.stage == 1:
        
        # 현재 인덱스까지 대사 출력
        for i in range(st.session_state.dialogue_index):
            st.text(dialogues_part1[i])
            
        # 다음 대사 출력
        if st.session_state.dialogue_index < len(dialogues_part1):
            st.markdown(f"**{dialogues_part1[st.session_state.dialogue_index]}**")
            
            # 다음 대사 버튼
            if st.button('엔터키 (다음 대사)'):
                st.session_state.dialogue_index += 1
                st.experimental_rerun()
        else:
            st.session_state.stage = 2
            st.experimental_rerun() # 다음 스테이지로 이동

# --- 3. 음식 선택 (라디오 버튼 사용) ---
if st.session_state.stage == 2:
    
    foods = ["콩나물국밥", "떡볶이", "곱창"]
    
    st.subheader(f'{name}님, 박계현 선생님과 함께 드실 음식 한 가지를 선택해주세요:')
    
    # 라디오 버튼으로 선택
    selected_food = st.radio(
        '음식 목록',
        foods,
        index=None,
        key='food_choice'
    )
    
    if selected_food:
        st.session_state.selected_food = selected_food
        st.write(f'✅ {name}님이 선택한 음식은 **{selected_food}** 입니다.')
        
        st.session_state.stage = 3
        st.experimental_rerun()

# --- 4. 음식 선택 결과 및 퀴즈 시작 ---
if st.session_state.stage == 3:
    name = st.session_state.name
    selected_food = st.session_state.selected_food

    st.success(f"{name}은 박계현 선생님과 함께 {selected_food}을(를) 먹으러 간다.")
    st.markdown(f"**{selected_food}**에 밑반찬까지 야무지게 먹는 당신에 대한 박계현 선생님의 호감도가 **100** 올라갔다. 밥을 먹는 동안 선생님이 미적분 킬러문항을 설명해주셨다. 당신의 이해력에 또 한번 감동하셔서 호감도가 **200** 올라갔다!")
    
    # 2부 대사
    dialogues_part2=[
        "박계현 선생님은 설국 아이들이 유리함수와 무리함수를 이해하지 못하는 것을 하소연하시며 떠나가셨다. 선생님의 뒷모습을 보며 여운이 남아 아주 오랫동안 그 자리에 서있었다.",
        f"???: 어엇 이게 누구지 왜 {name}은 여기 있는거지?",
        f"{name}: 앗 이 익숙한 목소리는 누구지? 설마.. F3의 마지막 멤버인가??",
        f" 그 사이 누군가 {name}을 향해 걸어온다. {name}은 그의 얼굴에서 나오는 빛 때문에 얼굴을 제대로 쳐다보지 못한다.",
        f"{name}: 아앗… 이 어마무시한 광채는… 김.병.관 선생님???",
        f"김병관 선생님: {name}이 대단하네~ 선생님을 바로 알아보고!",
        f"{name}: 하하핫. 제가 이래봐도 정보 1등급이였다고요~ 게다가 제 꿈은 정보통신공학과에 가는거에요!",
        f"김병관 선생님:({name}을(를) 향해 따뜻한 미소를 지으며 답한다.) 오오 역시 우리 {name}이야~!",
        "system: 당신에 대한 김병관 선생님의 호감도 +100",
        "바로 그 때, 당신이 전에 함께 이야기를 나누었던 두 명의 선생님들이 등장한다.",
        f"system: 이제 모든 선생님들의 호감도가 100이 넘어 선택할 시간이 왔습니다.",
        f"{name}: 아.. 너무 어려운데…하.. 시간을 조금만 더 주시면 안될까요?",
        "황석규 선생님: 선택하지 못하겠다면… 우리가 내는 퀴즈를 맞춰보는 것은 어떤지.. 허허허",
        f"김병관 선생님: 좋은 생각이군요! {name}이 퀴즈를 풀어 1등급이 나오면 그 과목의 선생님과 함께 데이트 할 수 있는 기회를 줄게.",
        f"박계현 선생님: {name}은 이미 저와 함께 국밥을 먹으러 가기로 했다만, 그래도 이 방법으로 한번 해보죠.. 샤샤샤샤샤",
        "system: 선생님들의 초고난도 퀴즈를 풀어보세요! 정답은 O,X를 대문자로 입력해야 인정됩니다."
    ]
    
    # 대사 출력 (다음 버튼 클릭)
    if 'dialogue_index_2' not in st.session_state:
        st.session_state.dialogue_index_2 = 0
        
    for i in range(st.session_state.dialogue_index_2):
        st.text(dialogues_part2[i])
        
    if st.session_state.dialogue_index_2 < len(dialogues_part2):
        st.markdown(f"**{dialogues_part2[st.session_state.dialogue_index_2]}**")
        
        if st.button('계속하려면 엔터키를 누르십시오'):
            st.session_state.dialogue_index_2 += 1
            st.experimental_rerun()
    else:
        st.session_state.stage = 4
        st.experimental_rerun()

# --- 5. 퀴즈 진행 (반복문 대체) ---
if st.session_state.stage == 4:
    
    questions = ["1.황석규 선생님: 공룡은 쥬라기 시대에 출현하였다.", "2.박계현 선생님: Y=2X+7 에서 Y절편은 8이다.", "3.김병관 선생님: 나의 생일은 12월 26일이다."]
    
    quiz_idx = st.session_state.quiz_index
    
    if quiz_idx < len(questions):
        st.subheader(f"✏️ {questions[quiz_idx]}")
        
        # 퀴즈 입력 폼
        user_answer = st.text_input("system: 정답을 입력하세요 (O 또는 X):", key=f'quiz_{quiz_idx}').upper()
        
        if user_answer:
            if user_answer == st.session_state.quiz_answers[quiz_idx]:
                st.success("✅ 정답입니다!")
                st.session_state.quiz_index += 1
                time.sleep(1) # 잠시 멈췄다가 다음 문제로 이동
                st.experimental_rerun()
            elif user_answer in ['O', 'X']:
                st.error("❌ 오답입니다. 다시 입력하세요.")
            else:
                st.warning("정답은 O 또는 X만 입력해야 합니다.")
    else:
        st.session_state.stage = 5
        st.experimental_rerun()

# --- 6. 엔딩 ---
if st.session_state.stage == 5:
    
    dialogues_ending = [
        "system:✨✨✨ 모든 문제를 완벽하게 맞췄습니다! ✨✨✨",
        "system: 세 선생님이 당신을 애제자로 인정합니다!",
        "황석규 선생님: 이제 넌 내 최고의 제자야! 이제 함께 호주로 가 새로운 돌을 찾으러 가자!",
        "박계현 선생님: 역시… 계산력도 논리력도 최고시군요. 그럼 일송칼국수로 함께 가실까요? 후.. 샤샤샤샤샤",
        "김병관 선생님: 내 생일까지 기억하다니... 정말 감동이야.",
        "system: 이후 당신은 설국의 F3와 함께 행복한 시간을 보내게 됩니다.",
        "system: 그러나….",
        "system: 깨어나 보니 시험 10일 전????",
        "system: 그렇습니다.. 이 모든 것은 다 꿈이였습니다. 이제 매일 아침 태권도를 하고 졸음을 참으며 수업을 듣고 야자를 5시간이나 하는 생활이 반복될 것입니다.",
        "system: 그러나 힘을 내십시오!! 당신의 삶속에서 설국의 F3를 언제나 만날 수 있으니까요! 그럼 이만~"
    ]
    
    # 엔딩 출력
    for line in dialogues_ending:
        st.text(line)
    
    # 폰트 아트는 st.code로 처리
    st.code("""
⠀  ⠀⠀⠀⠀⠀  ⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⡿⠟⠙⠛⠛⠁⠀⠈⠙⢿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⣿⣿⠀⠀⠊⣉⡙⠆⣤⣞⡉⠃⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⣻⣿⣿⡆⠀⠀⠈⢁⣠⣈⡛⠁⠀⢸⣿⡟⠀⠀⢀⢀⠀⠀⠀⠀
⠀ ⠀⠀⠀⢰⣿⣿⣿⣿⠃⠀⠀⠰⣯⣼⣿⣿⠀⠀⠀⢻⣿⣦⡀⡏⠉⠑⡄  ⠀
 ⠀⠀⠀⣾⣿⣿⣿⡇⠀⠀⠀⠀⠙⠿⠿⠋⠀⠀⠀⠈⣿⣿⡃⢱⠀⠀⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣷⠤⣄⣀⣀⣀⠀⠀⠀⠀⢀⡠⠾⠿⠟⢡⠃⠀⠀⡇⠀⠀⠀
 ⠀⠀⠀⠈⠙⠓⠀⠀⠀⣴⣿⣧⣼⣽⣷⣾⣟⠉⠉⠒⠒⠊⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠜⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⡤⠖⠋⠀   ⠀⠀
    """)
    st.info("이야기가 종료되었습니다. 처음부터 다시 시작하려면 새로고침하세요.")
