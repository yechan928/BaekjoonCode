import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
people = [set() for _ in range(n)]
camp = []
for i in range(m):
    data = list(map(int, sys.stdin.readline().split()))
    p = data[1:]
    camp.append(p)
song_id = 0
all_song = set()
for i in camp:
    if 1 in i:
        all_song.add(song_id)
        for j in i:
            people[j - 1].add(song_id)
        song_id += 1
    else:
        share = set()
        for j in i:
            share |= people[j - 1]
        for j in i:
            people[j - 1] = share.copy()

for i in range(n):
    if people[i] == all_song:
        print(i + 1)


# 합집합 기호(set에서만) "|="
# copy()를 해야 값까지 복사가 됨
# people[j-1] = share만 하면 모든 사람이 같은 set객체만 가리키게 됨
