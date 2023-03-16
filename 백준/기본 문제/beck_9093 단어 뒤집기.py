# Stack 구현을 통한 풀이
N = int(input())

for i in range(N):
    string = input()
    string += " "
    stack = []
    for j in string:
        if j!= " ":
            stack.append(j)
        else:
            while stack:
                print(stack.pop(), end='') # 단어가 한 글자씩 띄어서 출력되거나 줄 바꿈 되어 출력된느 것을 방지
            print(' ', end='') # 단어와 단어 사이를 띄어쓰기로 설정하여 단어와 단어를 구분해줌

# List 내부에서 제공하는 기능을 이용한 ㅁ풀이
N = int(input())
for i in range(N):
    string = list(input().split())
    for j in string:
        print(j[::-1],end=' ')
'''
arr[A:B:C]의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라
>> arr = range(10)
>> arr
[0,1,2,3,4,5,6,7,8,9]
>> arr[::2] # 처음부터 끝까지 두 칸 간격으로
[0,2,4,6,8]
>> arr[1::2] # index 1 부터 끝까지 두 칸 간격으로
[1,3,5,7,9]
>> arr[::-1] # 처음부터 끝까지 -1칸 간격으로 ( == 역순으로)
[9,8,7,6,5,4,3,2,1,0]
>> arr[::-2] # 처음부터 끝까지 -2칸 간격으로 ( == 역순, 두 칸 간격으로)
[9,7,5,3,1]
>> arr[3::-1] # index 3 부터 끝까지 -1칸 간격으로 ( == 역순으로)
[3,2,1,0]
>> arr[1:6:2] # index 1 부터 index 6 까지 두 칸 간격으로
[1,3,5]
'''

