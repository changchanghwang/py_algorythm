def isPrime(n,m):
  prime = [True]*(m+1)
  count=0
  for i in range(2,int(m**0.5)+1):
    if prime[i]:
      for j in range(2*i, m+1, i):
        prime[j] = False
  for i in range(n+1,m+1):
    if i>1 and prime[i] ==True:
      count+=1
  return count
  
while 1:
  n = int(input())
  m = 2*n
  if n==0:
    break
  else:
    print(isPrime(n,m))
