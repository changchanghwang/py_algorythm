input = 20


def find_prime_list_under_number(n):
  sieve = [True] * n 
  for i in range(2, n**0.5 + 1):
    if sieve[i] == True:         
      for j in range(2*i, n, i):
        sieve[j] = False
  return [i for i in range(2, n) if sieve[i] == True]


result = find_prime_list_under_number(input)
print(result)