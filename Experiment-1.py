#Write a Python program to find the factorial of a number using while loop
def fact():
  num=int(input("Enter a number to find its factorial:"))
  fact,i=1,1
  if (num!=0):
    while(i<=num):
      fact=fact*i
      i+=1
    print(f"The factorial of {num} is {fact}")
  elif (num==1 or num==0):
    print(f"The factorial of {num} is {fact}") 


#Write a Python program to check whether a number is Prime or not
def check_prime():
  num= int(input("Enter a number to check whether its prime or not: "))
  flag=1
  if (num>1):
    for i in range(2,num-1):
      if (num % i)==0:
        flag=0
        break
  if (flag==0):
    print("It is not a prime")
  else:
    print("It is prime")


#Write a Python program to print alphabet pattern 'E'
def Display_E():
  L=["* * * * *","*","*","* * * * *","*","*","* * * * *"]
  for i in L:
    print(i)


#Write a python program to check whether the number is palindrome or not.
def check_palindrome():
  word=input("Enter a word to check whetehr it's palindrome or not:")
  rword= word[::-1]
  if (word==rword):
    print("It is a palindrome")
  else:
    print("It is not a palindrome")

fact()
check_prime()
check_palindrome()
Display_E()

#Write a python program to check whether the number is Armstrong number or not.