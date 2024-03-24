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

#Write a python program to check whether a number is a palindrome or not using a function

def check_palindrome(string):
  if string[::-1]==string:
    return "It is a palindrome"
  else:
    return "It is not a palindrome"

print((check_palindrome("malyalam")))