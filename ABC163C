#最大公約数を求める問題　実際はmathのgcd関数を使わないとTLEになる

def gcd(p,q):
  if p%q==0:
    return q
  else:
    return gcd(q,p%q)
k=int(input())
s=0
for a in range(1,k+1):
  for b in range(1,k+1):
    for c in range(1,k+1):
      d=gcd(a,b)
      s+=gcd(d,c)
print(s)
