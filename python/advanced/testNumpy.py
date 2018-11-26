import numpy

a = numpy.arange(12)

print(type(a))
print(a)
print(a.shape)
a.shape = (3,4)

print(a)
print(a[2])

print(a[:,1])
print(a[:,1].shape)

b = a.transpose()
print(b)

a = numpy.arange(12)
print(a)