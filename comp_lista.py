
x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

print("Usando list comprehension")
z = [i**2 for i in x]
print(x)
print(y)

v = [i for i in x if i%2==1]
print(v)
