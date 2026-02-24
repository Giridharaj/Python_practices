def circular_array(num):
  n=len(num)
  def direction_index(i):
    return (i+num[i])%n
  for i in range(n):
    slow,fast=i,i,
    direction=num[i]>0
    while True:
      n_s=direction_index(slow)
      n_f=direction_index(fast)
      n_f1=direction_index(n_f)
      if (num[n_s]>0!=direction) or (num[n_f]>0!=direction) or (num[n_f1]>0!=direction):
        break
      slow,fast=n_s,n_f1
      if(slow==fast):
        if(slow==direction_index(slow)):
          break
        return True
    return False
