#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name="Guido"):
    print(f"Hello, {name}!")
    
  
    if name != "Guido":
        greet("Guido")

    


def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')

def add(num1, num2):
    return num1 + num2


def halve(number):
    if not isinstance(number, int) and not isinstance(number, float):
        return None

    return number / 2
