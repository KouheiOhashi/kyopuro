s=input()
a=0
m={}
d=1
for i in range(len(s)):
  b=int(s[len(s)-1-i])*d+a
  b=b%2019
  a=b
  d=d*10%2019
  if b in m:
    m[b]+=1
  else:
    m[b]=1
if 0 in m:
  sum=m[0]
else:
  sum=0
for i in m:
  sum+=m[i]*(m[i]-1)/2
print(int(sum))
