# https://school.programmers.co.kr/learn/courses/30/lessons/72410#
# 신규 아이디 추천

import re
def solution(new_id):
    answer = ''
    res = re.sub('[^a-zA-Z0-9_.-]','', new_id).lower()
    res=res.replace('..','.').strip('.')
    if '..' in res:
        while res[res.find('..')+1] == '.':
            if res.find('..')+1 <len(res):
                res = res[:res.find('..')+1] +res[res.find('..')+2:]
            else:
                res = res[:res.find('..')+1]

    res = res.strip('.')
    if res == '':
        res = 'a'
    if len(res) > 15:
        res= res[0:15]
        if res[14] == '.':
            res=res[0:14]
    if len(res) < 3:
        while(len(res) < 3):
            res+=res[len(res)-1]
    answer = res
    return answer