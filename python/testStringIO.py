import sys
from io import StringIO

print("============== std.out -> StringIO =============")
print("print to std.out")

sio = StringIO()

print("std.out is set to stringIO")

sys.stdout = sio

print("print to stringIO")

sys.stdout = sys.__stdout__

print("std.out is back")
print(sio.getvalue())

print("============== file -> StringIO =============")


