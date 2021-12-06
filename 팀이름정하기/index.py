eName = input()
n = int(input())
list = [input() for i in range(n)]

list.sort()
percentage = []

for name in list:
  percentage.append(
    ((eName.count('L')+name.count('L')+eName.count('O')+name.count('O'))*
    (eName.count('L')+name.count('L')+eName.count('V')+name.count('V'))*
    (eName.count('L')+name.count('L')+eName.count('E')+name.count('E'))*
    (eName.count('O')+name.count('O')+eName.count('V')+name.count('V'))*
    (eName.count('O')+name.count('O')+eName.count('E')+name.count('E'))*
    (eName.count('V')+name.count('V')+eName.count('E')+name.count('E')))%100
  )

print(list[percentage.index(max(percentage))])