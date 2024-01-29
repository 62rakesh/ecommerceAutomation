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