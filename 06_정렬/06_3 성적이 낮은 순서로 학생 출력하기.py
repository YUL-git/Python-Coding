n = int(input())
array = [input().split() for _ in range(n) ]
array.sort(key= lambda x: x[1])  # 여기서 완전 잘못했어 숫자형이기에 숫자로 변환해주어야 하는데
print(array)                     # 단순히 운 좋게 됌 '1''10''3'으로 정렬하기 때문에 주의하자

# 풀이
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0],end= ' ')
