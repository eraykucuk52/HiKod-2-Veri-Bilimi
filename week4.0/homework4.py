print("Give me your name: ")
name = input("> ")

print("Give me your age")
age = input("> ")

print("Give me your city")
city = input("> ")

print("Give me your job")
job = input("> ")

information = """
    Your Name:{}
    Your Age :{}
    Your City:{}
    Your Job :{}"""
print(information.format(name, age, city, job))