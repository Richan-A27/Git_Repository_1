#URK23CS1086 1
inventory={
    "gold":500,
    "pouch":['hint','twin','gemstone'],
    "backpack":['Xylophone','dagger','bedroll','bread loaf']
}
inventory['pouch']=['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']=inventory['gold']+50
for i in inventory:
  print(inventory[i])



#URK23CS1086 2
stockprice={
    "banana":[6,4],
    "apple":[0,2],
    "orange":[32,1.5],
    "pear":[15,3]
    }
for item in stockprice:
  print(f"{item}:{stockprice[item][0]}- ${stockprice[item][1]}")


total=0
for item in stockprice:
  total += stockprice[item][0]*stockprice[item][1]
print(f"the gross profit is ${total}")


#URK23CS1086 3
stock={
    "banana":6,
    "apple":0,
    "orange":32,
    "pear":15
    }

price={
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3
    }

def compute_bill(a,b):
  total=0
  for item in a:
    if b[item]>0:
      total+=a[item]
  return total

print("The total net value is:",compute_bill(price,stock))


#URK23CS1086 4
lloyd = {
"name": "Lloyd",
"homework": [90.0,97.0,75.0,92.0],
"quizzes": [88.0,40.0,94.0],
"tests": [75.0,90.0]
}
alice = {
"name": "Alice",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}
tyler = {
"name": "Tyler",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students=[lloyd,alice,tyler]

def average(a):
  total = float(sum(a))
  return total/len(a)

def get_average(student):
  homework= average(student["homework"])
  quizzes= average(student["quizzes"])
  tests= average(student['tests'])
  return homework*.1+quizzes*.3+tests*.6

def get_letter_grade(score):
    if score >= 90:
      return 'A'
    elif score >= 80:
      return 'B'
    elif score >= 70:
      return 'C'
    elif score >= 60:
      return 'D'
    else:
      return 'F'

def get_class_average(stud):
  result = []
  for i in stud:
    result.append(get_average(i))
  return int(average(result))


for i in students:
  for j in i.keys():
    print(j,":",i[j])
  print(f"Grade:{get_letter_grade(get_average(i))}\n")

print(f"Class Average:{get_class_average(students)}\n")
