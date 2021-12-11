import sys
import re

str = sys.stdin.readline().rstrip()

str = str.replace('c=','1').replace('c-','1').replace('dz=','1').replace('d-','1').replace('lj','1').replace('nj','1').replace('s=','1').replace('z=','1')

str = re.sub('[a-z]', '1',str)

print(str.count('1'))  
