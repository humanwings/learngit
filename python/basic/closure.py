def outer():
     x = 1
     def inner():
         print(x)
     return inner
foo = outer()
#print(dir(foo))
print(foo.__closure__)
