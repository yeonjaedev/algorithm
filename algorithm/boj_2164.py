# https://www.acmicpc.net/problem/2164
# 카드2

# 문제에서
# 배열을 쓰면 배열의 삽입, 삭제 시간복잡도 O(N)
# N ≤ 500,000
# N-1 번까지 반복을 해야함
# 1. 맨 앞의 값을 `삭제`
# 2. 맨 앞의 값을 `삭제` , 맨 뒤로 보내기 `삽입`
# ⇒ 삽입,삭제 총 3번
# ( N-1 ) * 3N  = 3N(N-1) ⇒ O(N^2)
# 500,000 * 500,000 = 250000000000 = 25 * 10의 10승
# 10^8 이 1억 ⇒ 1억에 1초
# 제한시간 2초니까 2억번 이내 여야 하는데
# 이문제는 10^10 이니까 100억 → 100초
# ⇒ Queue 를 써야 함
# ⇒ 큐의 삽입 삭제는 O(1) 이므로 N-1 번 반복해도 O(N) 임

from collections import deque
# n = int(input())
#
# dq = deque()
# for i in reversed(range(1,n+1)) :
#     dq.append(i)
# idx = 0
#
# while(len(dq) > 0):
#     if len(dq) == 1:
#         print(dq[0])
#         break;
#     if (idx + 1) % 2 == 1:
#         dq.pop()
#     else:
#         dq.appendleft(dq.pop())
#     idx += 1
#     # print(dq)


N = int(input())
dq = deque(range(1,N+1))
while(len(dq) > 1):
    dq.popleft()
    dq.append(dq.popleft())
print(dq.pop())