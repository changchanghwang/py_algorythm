expression = "100-200*300-500+20"

def solution(expression):
    answer = []
    answer.append(one(expression))
    answer.append(two(expression))
    answer.append(three(expression))
    answer.append(four(expression))
    answer.append(five(expression))
    answer.append(six(expression))
    return abs(max(answer))

def one(expression): # +>*>-
  if '-' in expression:
    expression = expression.split('-') #우선순위가 낮은 것부터 - 
  for i in range(len(expression)):
    if '*' in expression[i]:
      expression[i] = expression[i].split('*') # 우선순위가 낮은 것부터 *
      
  for i in range(len(expression)):
    if '+' in expression[i]:
      expression[i] = eval(expression[i]) # 1차원 배열인 애들은 먼저 + 계산
    else:
      for j in range(len(expression[i])): # 2차원 배열인 것들은
        if '+' in expression[i][j]:
          expression[i][j] = eval(expression[i][j]) # 2중for문에서 + 계산
    if str(type(expression[i])) == "<class 'list'>": # 원소가 배열인 것들만 미리 계산
      b = 1
      for k in expression[i]:
        b *= int(k) # 2차원 배열 *계산
      expression[i] = b    
  a = int(expression[0]) # 첫번째는 양수기 때문에
  for i in range(1, len(expression)): 
    a -= int(expression[i]) # 마지막 -계산
  return abs(a)

def two(expression): # ->+>*
  if '*' in expression:
    expression = expression.split('*')
  for i in range(len(expression)):
    if '+' in expression[i]:
      expression[i] = expression[i].split('+')
      
  for i in range(len(expression)):          
    if '-' in expression[i]:
      expression[i] = eval(expression[i])
    else:
      for j in range(len(expression[i])):
        if '-' in expression[i][j]:
          expression[i][j] = eval(expression[i][j])
    if str(type(expression[i])) == "<class 'list'>":
      b = 0
      for k in expression[i]:
        b += int(k)
      expression[i] = b
  a = int(expression[0])
  for i in range(1, len(expression)):
    a *= int(expression[i])
  return abs(a)

def three(expression): # +>->*
  if '*' in expression:
    expression = expression.split('*') #우선순위가 낮은 것부터 - 
  for i in range(len(expression)):
    if '-' in expression[i]:
      expression[i] = expression[i].split('-') # 우선순위가 낮은 것부터 *
      
  for i in range(len(expression)):
    if '+' in expression[i]:
      expression[i] = eval(expression[i]) # 1차원 배열인 애들은 먼저 + 계산
    else:
      for j in range(len(expression[i])): # 2차원 배열인 것들은
        if '+' in expression[i][j]:
          expression[i][j] = eval(expression[i][j]) # 2중for문에서 + 계산
    if str(type(expression[i])) == "<class 'list'>": # 원소가 배열인 것들만 미리 계산
      b = 1
      for k in expression[i]:
        b -= int(k) # 2차원 배열 *계산
      expression[i] = b    
  a = int(expression[0]) # 첫번째는 양수기 때문에
  for i in range(1, len(expression)): 
    a *= int(expression[i]) # 마지막 -계산
  return abs(a)

def four(expression): # ->*>+
  if '+' in expression:
    expression = expression.split('+')
  for i in range(len(expression)):
    if '*' in expression[i]:
      expression[i] = expression[i].split('*')
      
  for i in range(len(expression)):          
    if '-' in expression[i]:
      expression[i] = eval(expression[i])
    else:
      for j in range(len(expression[i])):
        if '-' in expression[i][j]:
          expression[i][j] = eval(expression[i][j])
    if str(type(expression[i])) == "<class 'list'>":
      b = 0
      for k in expression[i]:
        b *= int(k)
      expression[i] = b
  a = int(expression[0])
  for i in range(1, len(expression)):
    a += int(expression[i])
  return abs(a)  

def five(expression): # *>->+
  if '+' in expression:
    expression = expression.split('+')
  for i in range(len(expression)):
    if '-' in expression[i]:
      expression[i] = expression[i].split('-')
      
  for i in range(len(expression)):          
    if '*' in expression[i]:
      expression[i] = eval(expression[i])
    else:
      for j in range(len(expression[i])):
        if '*' in expression[i][j]:
          expression[i][j] = eval(expression[i][j])
    if str(type(expression[i])) == "<class 'list'>":
      b = 0
      for k in expression[i]:
        b -= int(k)
      expression[i] = b
  a = int(expression[0])
  for i in range(1, len(expression)):
    a += int(expression[i])
  return abs(a)   

def six(expression): # *>+>-
  if '-' in expression:
    expression = expression.split('-')
  for i in range(len(expression)):
    if '+' in expression[i]:
      expression[i] = expression[i].split('+')
      
  for i in range(len(expression)):          
    if '*' in expression[i]:
      expression[i] = eval(expression[i])
    else:
      for j in range(len(expression[i])):
        if '*' in expression[i][j]:
          expression[i][j] = eval(expression[i][j])
    if str(type(expression[i])) == "<class 'list'>":
      b = 0
      for k in expression[i]:
        b += int(k)
      expression[i] = b
  a = int(expression[0])
  for i in range(1, len(expression)):
    a -= int(expression[i])
  return abs(a)     

print(solution(expression))