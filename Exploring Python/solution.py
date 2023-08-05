def task1():
    name = "Farhan Masud"
    age = 25
    print("My name" + name + " and I am " + str(age))
def task2():
    num1 = int (input("Enter any integer number:"))
    num2 = float (input("Enter any float number:"))
    num1_int = float(num1)
    num2_float = int(num2)
    print("num1 :" + str(num1))
    print("num1_int :" + str(num1_int))
    print(" num2 :" + str(num2))
    print("num2_float :" + str(num2_float))
def task3():
    sentence = "Python Programming is fun!"
    print(" Length of " + sentence + " is : " + str(len(sentence)))
    print("8 character of" + sentence + " is :" + str(sentence[7]))
    substring = sentence[:6]
    print("I enjoy it !" + substring)
def task4():
    fruits =["apple", "banana", "cherry", "date"]
    fruits.append("grape")
    fruits.remove("banana")
    print(len(fruits))
    sliced_fruits = fruits[2:4]
    print(sliced_fruits)
    extra_fruits = ["kiwi", "lemon"]
    combined_fruits = sliced_fruits + extra_fruits
    print(combined_fruits)
def task5():
    num = int (input("Enter any integer number :"))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
        task5()
def task6():
    for num in range(1,11):
        print(num)
        sum = 0
        for num in range(1,101):
            sum = sum + num
            print(sum)
            task6()
def task7(n):
    return n * n
print(task7(7))
def is_prime(num):
    flag = False
    for n in range(2,num):
        if num % n == 0:
            flag = True
            break;
    return flag
print(is_prime(29))
def task8():
    student = {
        "Name" : "Farhan",
        "Age" : 25,
        "Grade" : "MSc"
    }
    student["Course"] = "Web Engg"
    for key, value in student.items():
        print(f"{key} : {value}")
        task8()
task7()            
is_prime()
task4()
task3()
task2()
task1()