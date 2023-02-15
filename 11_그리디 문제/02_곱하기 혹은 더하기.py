알고리즘) 0을 제외한 연산에서 최대한 많은 곱셈을 실행하기
## 0일 때는 덧셈을 했지만 1일 경우에 덧셈을 할 생각을 하지 못함
n = list(map(int,input()))
result = n[0]
for i in range(1,len(n)):
    num = n[i]
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)