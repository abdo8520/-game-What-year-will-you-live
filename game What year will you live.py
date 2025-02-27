print('#'*50)
print("Welcome to the game What year will you live?")
print('#'*50)
name = input("please input your name: ")
age =int(input("please input your age: "))
tall =int(input("please input your tall: "))
wight =int(input("please input your wieght: "))
print("=========================================")
a = (tall // wight)*age+10
b = a + age
c= 2025+a
print(f"welcome, {name}")
print(f"you will live untill {c} and you will be {b}")
print("=========================================")
