lines = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

def ms(time):
  hour = int(time[:2]) * 3600
  minute = int(time[3:5]) * 60
  second = int(time[6:8])
  millisecond = int(time[9:])
  return (hour + minute + second) * 1000 + millisecond
  
def solution(lines):
  answer = 0
  line = []
  for i in lines:
    i = i.split(' ')
    line.append(ms(i[1]))
  print(line)
  return answer
  

print(solution(lines))