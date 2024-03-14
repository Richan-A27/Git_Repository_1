#Write a python program to check whether a number is perfect or not using a function.
def perfect(num):
  l=[]
  for i in range(1,num):
    if (num%i==0):
      l.append(i)
    
  if num==sum(l):
    print(f"{num} is a perfect number")
  else:
    print(f"{num} is not a perfect number")
  print(l)
perfect(5364)

