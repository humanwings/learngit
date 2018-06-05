import struct

i = 1930
f = 10.31
b = b'$A7   '
s = "呉剣吴剑"
l = True


sb = struct.pack(">ifs?", i, f, b, l )
print(sb)
sb = struct.pack(">i", i )
print(sb)
sb = struct.pack(">f", f )
print(sb)
sb = struct.pack(">s", b )
print(sb)
sb = struct.pack(">?", l )
print(sb)