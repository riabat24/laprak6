def perkalian (a,b):
    for i in range (a):
        if i == a-1:
            print(b, end="=")
        else:
            print(b, end="+")
    hasil = a*b
    return hasil

  

print(perkalian(6,5))
print(perkalian(10,7))

