'''
아래와 같은 2 × 2 격자의 왼쪽 위 모서리에서 출발하여 오른쪽 아래 모서리까지 도달하는 길은 모두 6가지가 있습니다 (거슬러 가지는 않기로 합니다).
그러면 20 × 20 격자에는 모두 몇 개의 경로가 있습니까?
'''
def gen_f(n):
    l = [1] * n
    for _ in range(n):
        for i,_ in enumerate(l):
            if i is 0:
                l[i] += 1    
            else: 
                l[i] = li[i] + l[i-1]
            yield l

# res = 0
for li in gen_f(20):
    print(li)

# print(res)