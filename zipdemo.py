from zipfile import *
f = ZipFile("zip1.zip","w",ZIP_DEFLATED)

f.write("abc.txt")
f.write("data.txt")
f.write("xyz.txt")

f.close()

print("Zip crated")
