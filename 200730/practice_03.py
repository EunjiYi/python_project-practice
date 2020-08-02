
import random

class ClassHelper:
    def __init__(self, students):
        self.students = students #1. 학생이름으로 구성된 리스트 받아서 인스턴스변수에 할당
        
    
    def pick(self, num):
        return random.sample(self.students, num)  #2.학생들명단에서 인자n명 만큼 랜덤으로 추출한다.
    
    def match_pair(self):
        # 여기에 두 명씩 랜덤으로 페어짜는 로직 넣기.
        random.shuffle(self.students) #와 셔플이라는 엄청난 기능이 있다니
        pairs = []
        pair_cnt = len(self.students) // 2 #인덱스 그림 그려서 따져보기
        
        for idx in range(pair_cnt):
            #마지막 조
            if idx == pair_cnt -1 : 
                pairs.append(self.students[idx*2:])
            #두 명씩 랜덤으로 조짜기
            else: #else없으면 마지막조 넣고 또 슬라이싱을 하게 됨.
                #아니면 else 쓰지말고 if문끝나고 바로 return해버리자.
                pairs.append(self.students[idx*2:idx*2+2])
        
        return pairs
        




ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])
print(ch.pick(4)) #=> ['박싸피', '이싸피', '김싸피', '정싸피']  -할때마다 바뀜
print(ch.match_pair()) #[['정싸피', '이싸피'], ['김싸피', '조싸피', '박싸피']] -할때마다 바뀜