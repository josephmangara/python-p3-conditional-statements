#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        login = "Access granted"
    else :
        login = "Access denied"
    return login
print(admin_login("admin", "1254345"))
    

def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif temperature >= 40 and temperature < 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    return(f"It's {response} out there!")
print(hows_the_weather(55))

def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        sol = "FizzBuzz"
    elif num % 3 == 0 :
        sol = "Fizz"
    elif num  % 5 == 0:
        sol = "Buzz"
    else:
        sol = num
    return sol
    
print(fizzbuzz(13))

def calculator(operation, num1, num2):
    dict_map = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1/num2,
    }
    result = dict_map.get(operation, "Invalid operation!")
    if result == "Invalid operation!":
        dict_map = "None"
    return result
print(calculator("/",1,2))