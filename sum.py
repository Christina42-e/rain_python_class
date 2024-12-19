def sum(*args):
    result = 0
    for number in args:
        result += number
    return result

def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def exponential():
    pass

def print_name(name = "Kristina"):
   print(f"Hello {name}")


print(sum(1,2,3,4,5))
print_name()
print_name("Anne")