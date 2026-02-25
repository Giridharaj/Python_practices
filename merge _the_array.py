def merge(num1,m,num2,n):
  if(n==0):
    return
  start=len(num1)
  end=start-1
  while(n>0 and m>0):
    if(num2[n-1]>=num1[m-1]):
      num1[end]=num2[n-1]
      n-=1
    else:
      num1[end]=num1[m-1]
      m-=1
    end-=1
  while(n>0):
    num1[end]=num2[n-1]
    n-=1
    end-=1
