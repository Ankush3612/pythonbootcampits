# print("Ankush kumar")

# #to print your name using input
# name = input("Ankush kumar")
# print(name)

#find current age 
# bornyear=input("enter your born year")
# currentyear=input("enter current year")
# ageinyear=int(currentyear)-int(bornyear)
# print(ageinyear)

# #wap for currency convertor
# print("convert rupees into dollars")
# rupeesamount = int(input("enter the amount in Rs."))
# rsIntoDollar = (rupeesamount / 84) 
# print(rupeesamount," convert into dollar" , rsIntoDollar);    

# #wap for currency convertor
# print("convert dollar into rupees")
# dollaramount = int(input("enter the amount in dollar"))
# Dollarintors = (dollaramount * 84) 
# print(rupeesamount,"convert into dollar",Dollarintors);    

# #wap to check the you are eligible for voting or not
# userage = int(input("Enter your age"))

# #Wap to check the user eligible for job application
# #if gender is female and age is greater than 17
# #if gender is male then they can apply for privte job
# userage = int(input("Enter the user age"))
# usergender = (input("Entier you gender"))

# #method 1
# if(userage > 17 and usergender == "female"):
#     print("you are eligible for govt job")
# elif(userage > 17 and usergender == "male"):
#     print("you are eligible for private job")
# else:
#     print("you are not eligible for any job")

# #method 2
# if(userage > 17):
#     if(usergender == "female"):
#         print("your are eligible for govt job")
#     elif(usergender == "male"):
#         print("your are eligible for private job")
#     else:
#         print("your gender not exist")
# else:
#     print("your are not eligible any job"


# #Swithch conditon is the replacement of multipel if else block

# friendname = ["walt","jesse","mike"]
# print("before", friendname)

# #to add the new friend name in last 
# friendname.append("Laxmi sharma")
# print after adding name
# print("After",friendname)

# to add the name in specific position
# friendname.insert(0,"Laxmi Sharma")
# print("Add name at index 0", friendname)

# to remove the name from list 
# friendname.remove("Laxmi Sharma")
# print after removing name from the list
# print(friendname)
# to clear the list

# friendname.clear()
# print(friendname)

# friendname.pop(1)
# print(friendname)

# To sort the list
# friendname.sort()
# print(friendname)

# to print element is the given List
# for name in friendname:
#     print(name)

# to print the number 1 to 10
for no in range (1,12):
    print (no)


# to print the even number from 1 to 10 using for loop
# method 1
for evenno in range (2,21,3):
    print(evenno) 

#method 2
for no in range(1,11):
    if no % 2 ==0:
        print(no)

# set used to store the data and data is changeable
sets = {"pawan","ivan","anshu","ivan"}
sets.add("harsh")
sets.remove("harsh")
sets.remove("pawan")
sets.add("harsh")
print(sets)
print(type(sets))

# create  the list for friend name
# friend = {"sonal","suman","manish","shivam"}
# print(friend)
# friend.sort()
# print(friend)