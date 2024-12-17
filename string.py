x="what's my name?"
print(x)

for x in "banana":
  print(x)

a = "hello world"
print("length ===", len(a))

txt = "The best things in life are free!"
print("free" in txt)

b = "Hello World!"
print(b[-2:-5])

print(b[:-5])
print(b[-2:])

print(b.upper())
print(b.lower())
print(b.capitalize())

b = "Hello   "
print(b.strip())

b = "Hello, World!"
print(b.replace("World","Kristina"))

z = b.split(",")
print(z)

print("Hello world")

name = input("Enter your name")

print("You have entered your name = " + name)  #string concant
print(f"You have entered your name = {name}")   #format string
print("you have entered your name = %s" % (name))  #Modulus string
