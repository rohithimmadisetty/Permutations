import csv
import re
import itertools
import sys
row=[]
def cts(p):
    l=re.findall(r"\w",p)
    li=''.join(l)
    return li
with open(str(sys.argv[1])) as file:
 d = list(csv.reader(file))
for i in range(len(d)):
  d[i]=list(map(cts,d[i]))
#print(d)
res = list(itertools.product(*d))
#print(res)
result=[]
for i in res:
    s=""
    for j in i:
        s=s+j
    result.append(s)
#print(result)
print(','.join(result))