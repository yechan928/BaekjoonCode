n,x = map(int, input().split())
numbers= list(map(int, input().split())) #여러 개의 수를 공백으로 구분지으며 입력할때 리스트에 담는 거
result=[]
for j in range(0,n):
    if numbers[j]<x:
        result.append(numbers[j])
print(" ".join(map(str,result)))#join 함수 쓸때는 리스트의 요소가 문자열이어야 하기 때문에 변환
# join 함수 
# .join(리스트) 
# : 매개변수로 들어온 리스트에 있는 요소 하나하나를 다 합쳐서 하나의 문자열로 바꾸어 반환하는 함수, 즉 하나의 문자열이 됨 
# "구분자".join(리스트)
# : 리스트의 값과 값 사이에 '구분자'를 넣어 하나의 문자열로 합쳐준다
# 리스트의 요소가 str(문자열) 타입이어야 한다. (int 같은 숫자는 사용 불가 → map(str, 리스트)로 변환 필요!)
# 리스트 뿐만 아니라 튜플이나 이터러블 객체에도 사용가능 

#간단한 예시 join()
# words = ["안녕", "세상", "파이썬"]
# result = " ".join(words)  # 공백을 구분자로 사용
# print(result)  # 안녕 세상 파이썬 
