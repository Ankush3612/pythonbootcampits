# tuples can store the multiple data and data can't be change
# myTuple =("Ivan","Anshu","Anjali","Mani")
# print(myTuple)
# print(type(myTuple))

# print(myTuple[1])

# It shows us error
# myTuple[1] = "Khushi"
# print(myTuple)

# for name in myTuple:
#   print(name)
  
# Dictionary can store multiple data in key value pair
myDict = {
    "name":"Ankush Kumar",
    "email":"ankushkumarneps@gmail.com",
    "mob.":"9304442737"
} 

print(type(myDict))

for item in myDict:
  print(myDict[item])
  
# print{myDict.get("keys")}

myDict["name"] = "Aryan"
print(myDict)


# OOPS
# Class and Object
class Ankush:
  age = 20
  print("I am from Bihar")
  
# create object and pass class properties
ankush = Ankush()
print(ankush.age)


# currentYear = int(input("Enter current year " ))
# bornYear = int(input("Enter born year "))

class Agecalculator:
  # ageInYear = currentYear - bornYear
  dob = "26 Aug 2004"
   
# age = Agecalculator()
# print(age.ageInYear)


# Polymorphism method overloading
def age(dob1):
  print(dob1)
  
def age(dob,name):
  print(dob,name)
  
# x = age("26 Aug 2004")
y = age("26 Aug 2004","Ankush Kumar")