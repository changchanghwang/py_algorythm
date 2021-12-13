from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)
    
def dfs(dic,start):
  stack = [start]
  visited = []
  while stack:
    cur = stack.pop()
    visited.append(cur)
    for d in dic[cur]:
      if d not in visited:
        stack.append(d)
  return visited
print(len(set(dfs(dic,1)))-1)
