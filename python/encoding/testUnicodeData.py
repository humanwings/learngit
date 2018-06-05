import sys
import unicodedata

print(unicodedata.unidata_version )

print(dec(sys.maxunicode))

print(chr(sys.maxunicode))

print(unicodedata.name(chr(sys.maxunicode)))