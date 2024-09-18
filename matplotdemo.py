import matplotlib.pyplot as pit

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

# pit.title("Student Graph")
# pit.xlabel("Student Performance")
# pit.ylabel("Semester")
# pit.plot(x,y)
# pit.show()

marks = [84,78,74,74]
year = [2019,2020,2021,2024]

pit.pie(marks)
pit.title("Student Performance in %")
pit.xlabel("year")
pit.ylabel("marks")
# pit.plot(year,marks)
pit.plot()
pit.show()
