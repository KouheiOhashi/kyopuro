"コンビネーションは再帰を使う"

n,m,q=map(int,input().split())
a=[0]*q
b=[0]*q
c=[0]*q
d=[0]*q
A=[]
for i in range(q):
  a[i],b[i],c[i],d[i]=map(int,input().split())
def score(A):
  sum=0
  for (ai,bi,ci,di) in zip(a,b,c,d):
    if A[bi-1]-A[ai-1]==ci:
      sum+=di
  return sum
def fbs(A):
  if len(A)==n:
    return score(A)
  if len(A)>0:
    pre_last=A[-1]
  else:
    pre_last=0
  res=0
  for v in range(pre_last,m):
    A.append(v)
    res=max(res,fbs(A))
    A.pop()
  return res
 
print(fbs(A))
