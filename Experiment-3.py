#Write a python program to check whether a number is perfect or not using a function.
def perfect(num):
  l=[]
  for i in range(num+1):
    if i%num==0:
      l.append(i)
  if num==sum(l):
    print(f"{num} is a perfect number")

  else:
    print(f"{num} is not a perfect number")


perfect(6)