import string

# print(str("wujian"))
# print(str("呉剣"))
# print(ascii("wujian"))
# print(ascii("呉剣"))
# print(repr("wujian"))
# print(repr("呉剣"))

# str.format()
print("============  str.format() ===============")
print()
s0 = "{} 's age is {}"
s1 = "{0} 's age is {1}"
s2 = "{0!a} 's age is {1}"
print(s0)
print("   -->   ",s0.format("呉剣",40))
print(s1)
print("   -->   ",s1.format("呉剣",40))
print(s2)
print("   -->   ",s2.format("呉剣",40))

print()

# %
print("============  %d %s ===============")
print()
s0 = "%s 's age is %d"
print(s0)
print("   -->   ",s0 % ("呉剣",40))


# string.Formatter
print("============  string.Formatter ===============")
print()

fmt = string.Formatter()
s0 = "{} 's age is {}"
s1 = "{0} 's age is {1}"
s2 = "{0!a} 's age is {1}"
print(s0)
print("   -->   ",fmt.format(s0,"呉剣",40))
print(s1)
print("   -->   ",fmt.format(s1,"呉剣",40))
print(s2)
print("   -->   ",fmt.format(s2,"呉剣",40))