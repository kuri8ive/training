import math
 
n = int(input())
tmp = int(input())
tmpmin = tmp
t1 = int(input())
if t1 < tmp: tmpmin = t1
ans = t1 - tmp
 
 
for i in range(2,n):
    tmp = int(input())
  
    if tmp - tmpmin > ans: ans = tmp - tmpmin
    if tmp < tmpmin: tmpmin = tmp
     
print(int(ans))  
