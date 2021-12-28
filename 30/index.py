import sys
# from itertools import permutations

# n = sys.stdin.readline().rstrip()

# nums = list(n)
# nums = list(permutations(nums))

# arr = []

# for num in nums:
#   n = int(''.join(num))
#   if n % 30 == 0:
#     arr.append(n)


# print(max(arr) if arr else -1)


n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))
    
# 30의 배수를 구하는 방법
# 일의 자리수가 0
# 각 자리 숫자들 더했을때 3으로 나누어 떨어져야함