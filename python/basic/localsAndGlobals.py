a_string = "This is a global variable"
def foo():
     a_string = "test"
     print (locals())
foo() # 2
print (globals()) # doctest: +ELLIPSIS

