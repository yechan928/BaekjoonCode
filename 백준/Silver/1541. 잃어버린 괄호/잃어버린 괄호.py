import sys
sick = sys.stdin.readline().strip()
part = sick.split("-")
#part안에서 +를 기준으로 나눠서 다 더해버리기
total = sum(map(int,part[0].split("+")))
for i in part[1:]:
    total -= sum(map(int,i.split("+")))
print(total)