# import numpy

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
  stack = []
  count = 0
  
  ## numpy를 사용하여 행과 열을 사용하기 편하도록 변경
  # board = numpy.array(board) ##list에서 numpy로 변경
  # board = board.T ## 행과 열을 서로 바꿔줌
  
  # board = numpy.flip(board, axis=1) ## 왼쪽이 바닥으로 오도록 열 순서 변경
  # board = board.tolist() ## numpy에서 list로 변경
  
  #zip을 활용한 행렬 변경
  board = list(map(list, zip(*board)))
  for i in board:
    i.reverse()
  print(board)
  
  
  # 배열에서 0 제거
  for i in board:
    while 0 in i:
      i.remove(0)
  
  ## 순수 로직
  for i in moves:
    if board[i-1]:
      doll = board[i-1].pop()
      if stack and stack[-1] == doll:
        stack.pop()
        count += 2
      else:
        stack.append(doll)
    else:
      continue
  return count

print(solution(board,moves))