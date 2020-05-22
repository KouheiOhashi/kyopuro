N,Y=map(int,input().split())
ls=[]

def judge(c,b):
  #print(c)
  if b!=(-1,-1,-1) and len(b)==3:
    return list(b)  #参照渡しを回避
  else:
    #print(a)
    return list(c)
def re(select):
  if len(select)==3:
    #print(select[0]*10000)
    if int(select[0])*10000+(int(select[1]-select[0]))*5000+(int(select[2]-select[1]))*1000==Y:
      #print(select)
      return select
    else:
      return (-1,-1,-1)
  if len(select)==0:
    a=0
  else:
    a=select[-1]
  b=[]
  for i in range(int(a),N+1):
    select.append(i)

    b=judge(b,re(select))

    select.pop()

  return b
print(re(ls))