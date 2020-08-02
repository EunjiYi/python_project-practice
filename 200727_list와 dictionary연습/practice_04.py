book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

#1. cnt사용
title_cnt = {}
for title in book_title:
    if title in title_cnt:
        title_cnt[title] += 1
    else:
        title_cnt[title] = 1
print(title_cnt)   

#2. count() 함수 사용
title_cnt = {}
for title in book_title:
    title_cnt[title] = book_title.count(title)
print(title_cnt)


#3. get() 메소드 사용
# 와우...
# key 가 딕셔너리에 있는 경우 key 에 대응하는 값을 돌려주고, 그렇지 않으면 default 를 돌려준다.
title_cnt = {}
for title in book_title:
    title_cnt[title] = title_cnt.get(title, 0) +1
print(title_cnt)