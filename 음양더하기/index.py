absolutes = [4,7,12]
signs = [True,False,True]

def solution(absolutes, signs):
    answer = 0;
    for i in range(len(absolutes)):
      if signs[i] == True:
        answer += absolutes[i]
      if signs[i] == False:
        answer -= absolutes[i]
    return answer
  
print(solution(absolutes,signs))