import re

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def sharp_to_low(x):
  return re.sub('([A-G])(\#)',lambda x : x.group(1).lower(),x) 


def solution(m, musicinfos):
  m = sharp_to_low(m) # #이들어간 음을 소문자로 변경
  array = []
  for musicinfo in musicinfos:
    info = musicinfo.split(',')
    startTime = int((info[0].split(':'))[0])*60 + int((info[0].split(':'))[1]) # 시를 분으로 변경
    endTime = int((info[1].split(':'))[0])*60 + int((info[1].split(':'))[1]) # 시를 분으로 변경
    music = sharp_to_low(info(-1)) # #이들어간 음을 소문자로 변경
    playTime = endTime - startTime
    music = music*(playTime // len(music)) + music[:playTime % len(music)] # 재생시간에 따른 음 표시
    if m in music: # 재생음악에 찾는 음악이 포함되어있으면
      array.append((playTime,info[2]))
      
  if not len(array): # 찾은 음악이 없으면
    return '(None)'
  else: # 있으면
    array.sort(key = lambda x:-x[0]) # 재생시간 순으로 나열
    return array[0][1]


solution(m,musicinfos)