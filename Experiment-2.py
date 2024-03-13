#Write a Python program to remove duplicate elements in a list.
def remove_dupicate(List):
  NL=[]
  for i in List:
    if i not in NL:
      NL.append(i)
  print(NL)

#Write a python program to print each and every element in reverse order.
def reverse_list(List):
  print(List[::-1])

reverse_list([1,2,3,4,5,6,7,8])

#store student details such as name, regno, cgpa as tuples in a list. Sort the student details by name , regno and cgpa and display sorted student details.
def Stu_details(no_of_students):
  SRecord=[]
  for i in range(no_of_students):
      name=(input(f"Enter student {i+1} name:"))
      regno=(input(f"Enter student {i+1} rollno:"))
      cgpa=(input(f"Enter student {i+1} cgpa:"))
      l=[name,regno,cgpa]
      SRecord.append(tuple(l))
      
  s=input("Do you want to sort the details by name,regno and cgpa? Y/N:")
  if s.lower()=="y":
      SRecord.sort()

  for i in SRecord:
    print(i)
Stu_details(3)

#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
def Uword_freq(list):
   word_counts = {}
   unique_words = set(l)
   for word in list:
      if word not in word_counts:
          word_counts[word] = 1
      else:
          word_counts[word] += 1

   print(f"The unique words in the list are: {unique_words}")
   print("The frequency of occurrence of each word in the list is:")
   for word in unique_words:
     print(f"{word}: {word_counts[word]}")