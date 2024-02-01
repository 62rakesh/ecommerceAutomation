"""
Write a program to find prime number?

num = int(input("Enter a number:- "))

flag = False
if num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
    # write down factors
    for i in range(2, num):
        # print(i)
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(f"{num} is not a prime number")
        print(i, "times", num//i, "is", num)
    else:
        print(f"{num} is a prime number")
"""

"""
Example of Single level inheritance?
class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name of the person is {self.name}")
        print(f"{self.name} age is {self.age}")


class employee(person):
    def __init__(self, name, age, empID):
        self.empID = empID

        person.__init__(self, name, age)

    def details(self):
        print(f"{self.name} employee id is {self.empID}")


e = employee("Rakesh", 28, 123456)
e.display()
e.details()
"""


