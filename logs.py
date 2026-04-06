
def decorator(func):
    def wrapper():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper

def hello():
    print("Привет")


hello = decorator(hello)
hello()

# @decorator
# def hello():
#     print("Привет")

# hello()
